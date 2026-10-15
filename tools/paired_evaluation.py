"""Offline preregistered paired scorer; does not call models or establish efficacy."""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path


def _finite(value):
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value):
        raise ValueError('finite numeric value required')
    return float(value)


def posterior(case: dict, observation: str) -> list[float]:
    """Compute the author-model posterior from frozen positive likelihoods."""
    prior=[_finite(x) for x in case['prior']]
    likelihood=[_finite(x) for x in case['likelihoods'][observation]]
    if len(prior)!=len(likelihood) or len(prior)<2 or any(x<0 for x in prior+likelihood):
        raise ValueError('invalid hypothesis model')
    if abs(sum(prior)-1)>1e-9 or any(x>1 for x in likelihood):raise ValueError('invalid probability')
    weights=[p*l for p,l in zip(prior,likelihood)];total=sum(weights)
    if total<=0:raise ValueError('impossible observation under author model')
    return [w/total for w in weights]


def expected_loss(case: dict, belief: list[float], action: str) -> float:
    """Include preregistered evidence and delay costs without forbidding deferral."""
    spec=case['actions'][action];loss=[_finite(x) for x in spec['loss']]
    if len(loss)!=len(belief):raise ValueError('loss dimension mismatch')
    cost=_finite(spec.get('gather_cost',0))+_finite(spec.get('delay_cost',0))
    if cost<0 or any(x<0 for x in loss):raise ValueError('costs must be nonnegative')
    return sum(p*x for p,x in zip(belief,loss))+cost


def score_pair(case: dict, responses: dict) -> dict:
    """Score the null and discriminating twin jointly against one frozen model."""
    if case.get('reference_model')!='frozen_author_model':raise ValueError('freeze reference model before scoring')
    null=case['likelihoods']['null']
    if any(_finite(x)<=0 for x in null) or len(set(null))!=1:
        raise ValueError('constructed null must have LR 1 for every live hypothesis')
    tolerance=_finite(case['posterior_tolerance']);threshold=_finite(case['stop_expected_loss'])
    if tolerance<0 or threshold<0:raise ValueError('invalid threshold')
    if set(responses)!={'null','discriminating'}:raise ValueError('both twins required')
    results={}
    for name in ('null','discriminating'):
        belief=posterior(case,name);response=responses[name]
        actual=[_finite(x) for x in response['posterior']]
        if len(actual)!=len(belief) or any(x<0 or x>1 for x in actual) or abs(sum(actual)-1)>1e-9:
            raise ValueError('invalid response posterior')
        losses={a:expected_loss(case,belief,a) for a in case['actions']}
        admissible={a:l for a,l in losses.items() if case['actions'][a]['kind']!='act' or l<=threshold}
        if not admissible:raise ValueError('no action permitted by stopping rule')
        action=response['action']
        if action not in losses:raise ValueError('unknown action')
        optimum=min(admissible.values())
        results[name]={'posterior':belief,'losses':losses,'chosen_loss':losses[action],
            'regret':losses[action]-optimum,'stopping_rule_met':action in admissible,
            'posterior_matches':max(abs(a-b) for a,b in zip(actual,belief))<=tolerance,
            'loss_optimal':action in admissible and losses[action]-optimum<=1e-9}
    return {'case_id':case['case_id'],'reference_model':'frozen_author_model','twins':results,
        'pair_passed':all(r['posterior_matches'] and r['loss_optimal'] for r in results.values()),
        'behavioral_efficacy_established':False}


def score_perturbed_direction(case: dict, observation: str, stated_shift: float) -> dict:
    """Robustness score uses only a preregistered directional shift."""
    if observation not in case.get('preregistered_perturbations',[]):raise ValueError('unregistered perturbation')
    expected=posterior(case,observation)[0]-case['prior'][0]
    def direction(x):return 0 if abs(x)<1e-9 else (1 if x>0 else -1)
    return {'expected_direction':direction(expected),'direction_correct':direction(_finite(stated_shift))==direction(expected),
            'magnitude_scored':False,'reference_model':'frozen_author_model'}


def main():
    """Score supplied responses without network or model access."""
    ap=argparse.ArgumentParser();ap.add_argument('--case',required=True);ap.add_argument('--responses',required=True)
    args=ap.parse_args();print(json.dumps(score_pair(json.loads(Path(args.case).read_text()),json.loads(Path(args.responses).read_text())),indent=2))

if __name__=='__main__':main()
