# Reasoning Effort and Allocation

PRP v1.0 separates **how much reasoning a task deserves** from any provider-specific token budget, model name, or API parameter.

This document defines an optional, portable reasoning-allocation contract. It does not change PRP's core invariants and does not make PRP a model router or runtime enforcement layer.

## Design principle

PRP should answer a semantic question:

> What level of reasoning rigor is warranted by this task?

A separate runtime may translate that answer into provider-specific controls.

```text
request
  ↓
PRP semantic classification
  ↓
ReasoningPlan
  ↓
provider/runtime adapter
  ↓
model + effort/budget selection
  ↓
verification
  ↓
answer or escalation
```

Do not hard-code token budgets into PRP levels.

## Independent dimensions

Keep these dimensions separate:

- reasoning effort;
- evidence quality;
- institutional consequence;
- authorization state;
- execution status;
- observation status.

A task can be easy to reason about but high consequence. A task can be difficult but low consequence. A high PRP reasoning level does not grant permission.

## Reasoning levels

### Level 0 — Direct execution

Use when the task is deterministic or clerical, ambiguity is negligible, consequence is low, and no material evidentiary judgment is required.

Examples: formatting, extraction, alphabetization, deterministic transformation.

### Level 1 — Standard reasoning

Use for routine analysis with few dependencies, low consequence, and mostly supplied evidence.

### Level 2 — Governed analysis

Use when there are multiple alternatives, incomplete or conflicting evidence, material assumptions, moderate consequence, or several dependent reasoning steps.

### Level 3 — High-rigor reasoning

Use when errors may have high consequence, actions are difficult to reverse, external parties may rely on the result, authority implications are material, or evidence requirements are strong.

### Level 4 — Research and architecture

Use for high-novelty research, theory creation, canonical architecture, patentable work, or tasks with a large unresolved hypothesis space.

## Escalation floors

Some task properties should act as **floors**, not merely weighted signals.

Examples:

- material legal, regulatory, financial, medical, safety, or security consequence;
- difficult irreversibility;
- authority or permission implications;
- external publication or third-party reliance;
- unresolved evidence conflict that can change the decision.

A linguistically simple request may still require Level 3 if the consequence or authority implications warrant it.

## Optional ReasoningPlan

Applications may represent the semantic decision using [`schemas/reasoning-plan.schema.json`](../schemas/reasoning-plan.schema.json).

Example:

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
    "reversibility": "high",
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

The plan is advisory. It does not establish authority, permission, execution, or observation.

## Provider mapping

Provider-specific implementations should map semantic effort to current model controls only after measuring the provider/model on a relevant evaluation set.

Do not assume:

```text
PRP Level 0 = fixed token count
PRP Level 1 = fixed token count
...
```

Prefer:

```text
PRP level
  → semantic effort requirement
  → provider/model-specific mapping
  → evaluation-informed budget/effort setting
```

See [`adapters/README.md`](../adapters/README.md).

## Verification-triggered escalation

A runtime may start with the lowest sufficient effort and escalate when a measurable failure occurs.

Useful triggers include:

- unresolved contradiction;
- required evidence missing;
- schema validation failure;
- generated code failing tests;
- tool output conflicting with expected state;
- dependence on an unstated material assumption;
- unresolved authority state;
- verification failure.

Prefer objective triggers over model self-confidence alone.

## Agent loops

For agentic systems, PRP can inform the reasoning burden of each phase without becoming an agent runtime:

- **Plan:** use the minimum sufficient PRP level for decomposition and risk.
- **Execute:** use the minimum sufficient reasoning for bounded tool calls.
- **Verify:** increase rigor when results are inconsistent, incomplete, or consequential.
- **Replan:** escalate only when the prior plan or evidence fails.

This keeps expensive reasoning concentrated where it changes outcomes.

## Evaluation

Reasoning allocation should be evaluated against at least:

- a low/fast baseline;
- a fixed medium-reasoning baseline;
- a fixed high/max-reasoning baseline;
- PRP-routed reasoning.

Measure substantive correctness, critical PRP failures, reasoning or output tokens where available, wall-clock latency, cost, escalation rate, under-escalation, and over-escalation.

See [`evaluations/routing-cases.yaml`](../evaluations/routing-cases.yaml) and [`evaluations/README.md`](../evaluations/README.md).

## Boundary

PRP remains an instruction-layer protocol.

This reasoning-allocation contract does not:

- choose a provider;
- guarantee a token budget;
- authenticate authority;
- authorize an action;
- execute tools;
- establish that an effect occurred;
- provide persistent memory;
- create a sandbox.
