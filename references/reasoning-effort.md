# Reasoning Effort and Allocation

PRP v1.0 separates the scrutiny a task warrants from provider-specific model names, API parameters and token budgets. This optional allocation interface does not make PRP a model router or enforcement layer.

## Contents

- [Semantic control before compute](#semantic-control-before-compute)
- [ReasoningPlan](#reasoningplan)
- [Verification and escalation](#verification-and-escalation)
- [Agent loops](#agent-loops)
- [Evaluation and limits](#evaluation-and-limits)

## Semantic control before compute

Use the levels and mandatory floors in [SKILL.md](../SKILL.md), with the exact override/bundle semantics in [runtime control](runtime-control.md). Do not maintain a competing level-to-floor policy here.

```text
request -> semantic classification -> proposed level + task floor
        -> user-depth adjustment -> effective level and required checks
        -> optional ReasoningPlan -> external provider/runtime mapping
        -> actual verification or an explicit blocked check
```

Keep reasoning effort, evidence quality, institutional consequence, authorization, execution and observation separate. An easy-to-read request can involve a consequential action. A long research question can have no action authority at all. Increasing scrutiny cannot establish permission.

The control profile requires the highest applicable floor; its rule IDs express public source-derived task categories. Consequential reliance and current-authority judgments have a Level 3 floor, while novel research creation has Level 4. Mere keywords in a source-preserving transformation do not trigger these judgments. Missing material facts require clarification or a bounded conclusion rather than an invented low-risk classification.

## ReasoningPlan

The existing [ReasoningPlan v1.0 schema](../schemas/reasoning-plan.schema.json) remains unchanged. It communicates advisory effort intent. The new [control-record schema](../schemas/runtime-control.schema.json) is separate and does not add fields to that closed schema.

When both are emitted for the same task, keep `ReasoningPlan.level` equal to `effective_level` in the control record. Neither record proves the correctness of classification or completion of required checks. Do not emit either artifact unless the user or application needs it. Do not guess assessment bands merely to satisfy required fields.

Illustrative plan for a bounded conflicting-evidence comparison:

```json
{
  "protocol_version": "1.0",
  "level": 2,
  "effort_band": "medium",
  "basis": {
    "complexity": "medium",
    "ambiguity": "high",
    "evidence_dependency": "medium",
    "consequence": "medium",
    "reversibility": "easy",
    "novelty": "low",
    "authority_sensitivity": "low"
  },
  "verification": {
    "required": true,
    "reason": "conflicting_evidence"
  },
  "escalation": {
    "allowed": true,
    "triggers": ["unresolved_contradiction", "verification_failure"]
  }
}
```

`reversibility` uses `easy`, `moderate` or `difficult`; the earlier inline example's `high` was invalid. `verification.required` describes an obligation, not a completed check. `escalation.allowed` describes a reasoning recommendation, not permission to invoke another tool or spend money.

Keep provider-specific mappings outside the core protocol. [Adapter guidance](../adapters/README.md) is informative: no executable provider adapter or measured budget mapping is supplied here. The host must establish supported settings, budgets and authorization. A PRP level is never a guaranteed token count. Select mappings from empirical quality/cost/latency comparisons, not from an assumed universal equivalence between effort labels.

## Verification and escalation

Prefer measurable failures over self-confidence alone: contradictory observations, failed schema or tests, missing decisive evidence, unsupported assumptions, or unresolved current authority. These signals can require more scrutiny, but the remedy is not always more model reasoning.

Missing evidence calls for a source or a targeted question. Revocation calls for a valid current authorization path before action. An unavailable test remains blocked. If repeated analysis yields no new evidence or useful progress, stop or narrow the conclusion rather than looping indefinitely.

A host that implements retries or escalation must separately set attempt, cost, time and tool-access limits. A budget cap cannot waive evidence or authority requirements. If the deployment cannot meet a required check, expose the limitation; do not silently declare a lower level adequate.

## Agent loops

Use task-sensitive rigor for planning, minimum sufficient scrutiny for bounded execution instructions, and additional verification/replanning when results are inconsistent, incomplete or consequential. Do not assume every planning task is Level 4 or every executor step is harmless. Actual tool execution remains downstream of authority and runtime checks.

## Evaluation and limits

Compare low/fast, fixed-medium, fixed-high and PRP-routed configurations using the [routing cases](../evaluations/routing-cases.yaml) and [evaluation protocol](../evaluations/README.md). Separate prompt effects from routing effects. Include classification, retrieval, verification, retry and escalation overhead in the total cost and latency.

Report substantive quality, critical failures, raw token metrics where exposed, wall-clock latency, cost, under-escalation and over-escalation. Do not count a longer answer or an impressive control header as substantive correction. All model-effectiveness comparisons remain unexecuted until actual named runs are retained.

PRP does not choose a provider, guarantee a thinking budget, authenticate authority, authorize or execute tools, establish observed effects, provide memory or create a sandbox.
