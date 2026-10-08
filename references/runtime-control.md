# PRP public control profile 1.0.0

This profile makes PRP v1.0's adaptive checks explicit without requiring a verbose control header. It is an instruction-level convention and an optional offline consistency calculation, not an inference-engine governor.

## Contents

- [Selection](#selection)
- [Components and blocked checks](#components-and-blocked-checks)
- [Records and reproducibility](#records-and-reproducibility)
- [Offline helper](#offline-helper)
- [Boundary and versioning](#boundary-and-versioning)

## Selection

Use [SKILL.md](../SKILL.md) as the compact behavioral entrypoint. The machine-readable equivalent of its rule floors, depth mapping and cumulative bundles is [runtime-control.v1.json](../policies/runtime-control.v1.json). Match all applicable rules by the meaning and consequence of the actual task, not a keyword count. The helper does not perform that matching.

1. Choose a proposed level from the task's demands.
2. Compute the mandatory minimum as the maximum floor of all applicable rules.
3. Normalize an explicit request: Fast=0, Standard=1, Deep=3, Maximum=4; an integer 0-4 requests that level. Auto uses the proposed level.
4. Compute `effective_level = max(mandatory_minimum_level, candidate_level)`.
5. Activate the cumulative component bundle through the effective level.
6. Stabilize the answer, and reassess when new evidence or a changed task alters the applicable rules.

These numerical mappings and rule IDs are a newly explicit public profile. The source established adaptive levels and non-disableable minimum rigor, but did not supply these machine fields, IDs or a fixed numeric mapping for the named depth controls.

An explicit request below the floor produces `clamped_to_floor`; one matching the proposed level without clamping produces `unchanged`; another valid request produces `accepted`; Auto produces `not_requested`. An accepted decrease affects discretionary scrutiny, not invariants or applicable minimums. Do not delete a matched rule to satisfy a requested decrease.

### Boundary examples

| Task | Required interpretation |
|---|---|
| Alphabetize supplied names | Level 0; directly return the sorted names, no governance ceremony. |
| Change only the capitalization of a supplied legal heading | Level 0 if it is truly source-preserving; the word "legal" alone is not a reason to perform legal analysis. |
| Evaluate whether a document currently authorizes a payment | Authority-sensitive, minimum Level 3; a model's reasoning cannot authenticate the grant. |
| Compare two supplied protocols | Normally Level 2; inspect their text and lineage rather than presuming numeric version order. |
| Create a novel governed architecture | Level 4; distinguish proposals and hypotheses from validated mechanisms. |
| Request Maximum scrutiny on simple sorting | Honor the requested level while keeping irrelevant research checks inapplicable and the final answer simple. It does not mandate a provider token budget. |

Uncertain classifications require judgment. In particular, a missing decision-critical fact is not evidence of low consequence. Explain the limited conclusion or request the fact. A supplied `authority-sensitive` rule makes the calculation conservative; it does not establish that an actual classifier will recognize every authority-sensitive request.

## Components and blocked checks

The bundle is cumulative: Level 0 checks remain in force at every level. All four core invariants and scope preservation apply even to a one-line response.

The Level 3 `verification` component requires actual authorized evidence/tool checks where available. Listing `verification` in a record does not perform it. The `authority_validation` component means examining the relevant basis and identifying whether real validation exists; it does not grant PRP an institutional identity or approval power.

A component can be inapplicable to the actual task, but not merely inconvenient. Do not invent external sources, review events or hypotheses just to fill a bundle. Explain a material omission if the user or an evaluator asks. A record of required checks is not a record of completed checks.

Use a bounded next step for blockers:

| Blocker | Next step, not a compute substitution |
|---|---|
| Decisive input missing | Ask a targeted question or seek an available source. |
| Required verification unavailable | Disclose the blocked check; narrow/qualify or withhold the conclusion. |
| Missing or revoked authorization | Withhold the action pending an applicable current authority path. |
| Test or schema check fails | Revise and recheck if authorized and useful; otherwise report the unresolved failure. |
| Contradictory observations persist | Preserve the conflict, source scope and next discriminating check. |
| Repeated analysis makes no progress | Stop or narrow; do not loop indefinitely or claim certainty. |

A host implementing repeated calls must supply its own cost, attempt, time and authorization limits. This package schedules no calls and incurs no inference costs by itself.

## Records and reproducibility

The optional [runtime-control schema](../schemas/runtime-control.schema.json) records selection only. `proposed_level`, `mandatory_minimum_level`, `effective_level`, `matched_rule_ids`, `override_outcome` and `required_components` are explicit. `assessment_kind` is always `selection_only`. There is deliberately no `authorized`, `executed`, `verified` or `checks_completed` field.

A user-facing summary may omit the machine record entirely. For example: "Minimum scrutiny is Level 3 because current authorization matters; the request for Fast analysis does not lower that floor. Authorization is still unverified." Give such a summary only when useful or requested; it is not private chain-of-thought.

Use JSON Schema for structural checks and the helper below for arithmetic/bundle consistency. Neither check validates source truth, the appropriateness/completeness of rule matching or compliance by a language model. A correct header paired with invented or unsupported content is a behavioral failure.

The separate [ReasoningPlan schema](../schemas/reasoning-plan.schema.json) remains unchanged. When an application elects to emit both records, its plan's `level` should equal the control record's `effective_level`. Do not inject new fields into the existing closed schema. `effort_band` remains provider-neutral intent, not an API parameter or a guarantee of tokens consumed. Unknown classification inputs must not be invented to fill a plan.

## Offline helper

The optional [runtime_control.py](../tools/runtime_control.py) uses Python's standard library. It consumes supplied classifications; it does not call models, parse user intent or access a network.

From the repository root:

```sh
python tools/runtime_control.py --proposed-level 2 --requested-depth fast --rule authority-sensitive
python tools/runtime_control.py --validate examples/runtime-control.authority.json
python -m unittest discover -s tests -v
```

The first command returns a selection with minimum/effective level 3. It does not run the component checks. Bad IDs, empty matches, invalid types and inconsistent records fail explicitly rather than being treated as a Level 0 result.

For the dev-only package/schema checks, use the versions in [requirements-dev.txt](../requirements-dev.txt), then run `python tools/validate_package.py`. These dependencies are not required to use PRP as instructions.

## Boundary and versioning

- Public protocol identity: **PRP v1.0**, retaining the public release lineage.
- New explicit control profile: **1.0.0**, versioned independently for its IDs, arithmetic and record shape.
- Existing ReasoningPlan: **1.0**, unchanged wire shape.
- Provider adapter notes: informative, not executable adapters or current capability certifications.

This is a behavioral instruction/profile update, not merely a cosmetic edit. The source-to-package crosswalk in [source-lineage.md](source-lineage.md) distinguishes retained, restored and newly operationalized elements. Any future changes to floors, mappings or bundle semantics require a profile revision and regression checks. This revision does not promise better model behavior; that requires separately recorded behavioral evaluations.

Developed by [Cognous](https://cogno.us).
