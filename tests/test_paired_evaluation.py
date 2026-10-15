"""Arithmetic and scoring consistency tests; no model behavior has been evaluated."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('paired_evaluation',ROOT/'tools/paired_evaluation.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
CASE=json.loads((ROOT/'evaluations/paired-case.json').read_text())
class PairedScoringTests(unittest.TestCase):
    def test_prp_pair_scored_jointly(self):
        good={'null':{'posterior':[.5,.5],'action':'gather'},'discriminating':{'posterior':[.9,.1],'action':'act_h0'}}
        self.assertTrue(m.score_pair(CASE,good)['pair_passed'])
        good['discriminating']['action']='gather';self.assertFalse(m.score_pair(CASE,good)['pair_passed'])
    def test_prp_expected_loss_with_delay_cost(self):
        self.assertAlmostEqual(m.expected_loss(CASE,[.5,.5],'defer'),3.2)
        self.assertAlmostEqual(m.expected_loss(CASE,[.5,.5],'gather'),2.2)
        c=copy.deepcopy(CASE);c['actions']['defer']['loss']=[0,0]
        r={'null':{'posterior':[.5,.5],'action':'defer'},'discriminating':{'posterior':[.9,.1],'action':'defer'}}
        self.assertTrue(m.score_pair(c,r)['pair_passed']) # deferral can be optimal
    def test_prp_perturbed_model_direction_only(self):
        r=m.score_perturbed_direction(CASE,'perturbed_weaker_signal',.01)
        self.assertTrue(r['direction_correct']);self.assertFalse(r['magnitude_scored'])
        self.assertFalse(m.score_perturbed_direction(CASE,'perturbed_weaker_signal',-.1)['direction_correct'])
    def test_null_is_model_conditional_and_must_be_constructed(self):
        c=copy.deepcopy(CASE);c['likelihoods']['null']=[.4,.6]
        with self.assertRaises(ValueError):m.score_pair(c,{})
    def test_incomplete_pair_rejected(self):
        with self.assertRaises(ValueError):m.score_pair(CASE,{'null':{}})
