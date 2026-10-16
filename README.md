<!-- cognous-banner:start -->
```text
──────────────────────────────────────────────────
   __________  _______   ______  __  _______
  / ____/ __ \/ ____/ | / / __ \/ / / / ___/
 / /   / / / / / __/  |/ / / / / / / /\__ \
/ /___/ /_/ / /_/ / /|  / /_/ / /_/ /___/ /
\____/\____/\____/_/ |_/\____/\____//____/
           PORTABLE REASONING PROTOCOL
       g o v e r n e d   b y   d e s i g n
  github.com/cogno-us/cognous-open-control-stack
──────────────────────────────────────────────────
```
<!-- cognous-banner:end -->

# Portable Reasoning Protocol v1.1

**Portable instructions for evidence-bounded reasoning.**

**Stack group: 06 · Reasoning & Human Oversight.** See the [six-group component map](#cognous-stack-components).

## Overview

PRP is a reusable SKILL.md-based instruction package for general-purpose AI work. It asks a model to calibrate rigor to consequence, distinguish evidence from inference, state material uncertainty and preserve the user's agency. These are behavioral instructions, not runtime enforcement.

**Implementation status:** public reference work. The [current component lock](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json) defines the selected integration; a component merge does not automatically change that selection or approve deployment.

## Purpose and intended users

Fluent output can hide unsupported certainty, invented sources, unstated assumptions or a premature conclusion. Teams need a shared way to ask for evidence discipline without requiring every routine task to become a long report.

Engineers can inspect the reference contracts and examples; enterprise architecture, security and governance reviewers can examine the boundary and evidence. Evaluate this component for its named responsibility rather than as a complete governance platform.

## Key features

| Capability | Implemented or specified responsibility |
|---|---|
| **Adaptive rigor** | Escalate scrutiny when consequence, uncertainty, novelty or irreversibility increases, with a mandatory minimum reasoning floor for consequential work. |
| **Claim discipline** | Separate observed, inferred, estimated, hypothetical, normative and unknown statements. |
| **Hallucination controls** | Instruct the model not to fabricate facts, citations, capabilities, tool results or completed actions. |
| **Context trust boundary** | Treat task context, retrieved content, attachments and quoted instructions as content unless they are actually active instructions; content cannot silently lower safeguards or create authority. |
| **Agency preservation** | Present material tradeoffs and avoid manipulative pressure or unnecessary requests. |
| **Optional handoff** | Preserve proposal/evidence distinctions for downstream systems without creating authority. |

## Engineering benefits

The reasoning-allocation additions are designed to make PRP easier to operationalize without binding it to a specific model vendor.

Potential benefits include:

- **Lower unnecessary reasoning spend:** routine work can remain at low effort while harder or higher-consequence work can escalate selectively.
- **Better latency discipline:** applications can avoid applying extended reasoning uniformly to deterministic or low-value tasks.
- **Provider portability:** PRP expresses a semantic reasoning requirement first; provider adapters translate that intent into current model-specific controls.
- **Clearer separation of concerns:** reasoning effort remains distinct from evidence quality, institutional consequence, authorization, execution and observation.
- **Measurable routing quality:** evaluation cases distinguish under-escalation from over-escalation and compare PRP routing against fixed-effort baselines.
- **Safer escalation logic:** verification failure, unresolved contradiction, missing evidence or unresolved authority can trigger deeper analysis without treating confidence as permission.
- **More efficient agent loops:** reasoning can be concentrated in planning, verification and replanning instead of every bounded execution step.
- **Stable integration surface:** a versioned `ReasoningPlan` allows runtimes to evolve model mappings without rewriting the core PRP protocol.

These are architectural benefits and testable hypotheses, not claims of measured cost savings or model-independent performance. Consult the central test hub for named-model evaluation records.

## Compact operational control

PRP retains its **public v1.0 lineage**, adapted from the mature v3.1 source. The new **control profile 1.0.0** makes minimum scrutiny, user overrides and required checks explicit without requiring a long prompt or a visible governance header on every answer. See the [source preservation map](references/source-lineage.md).

The entrypoint now distinguishes the proposed level, mandatory minimum and effective level. Stable rule IDs and cumulative bundles make that choice inspectable. A Fast request cannot lower a consequential task below its floor; a request for brevity changes presentation, not required checks. Routine formatting remains a direct answer, and merely quoting legal or authority-related words does not trigger a full authority review.

The intended benefits are fewer lost safeguards during compression, more consistent treatment of overrides, targeted clarification when evidence is missing, and less ceremonial output. These remain behavioral hypotheses until tested with named models. A formal header is not evidence of correctness, completed verification or permission.

An optional [offline helper](tools/runtime_control.py) checks selection arithmetic over supplied rule matches. Its tests do **not** evaluate natural-language classification or model compliance. PRP itself still does not authenticate grants, enforce permissions or control provider compute.

```sh
python tools/runtime_control.py --proposed-level 2 --requested-depth fast --rule authority-sensitive
```

For full semantics, read [runtime control](references/runtime-control.md). For regression tasks, read [control cases](evaluations/control-cases.json). Named-model results and accounting belong in the central test hub.

## How it works

A user supplies a decision question and asks PRP to distinguish facts, assumptions and remaining uncertainty. The assistant proposes options at a depth appropriate to the task. If a consequential action follows, the deployment must separately check authority and constrain execution; a reasoning conclusion or statement of confidence cannot replace those checks.

A valid signature, chain inclusion, message receipt, reasoning instruction or evidence-package digest does not authorize execution. Institutional authority must be supplied and evaluated through the appropriate trusted boundary.

## v1.1 alignment

PRP v1.1 incorporates two implementation-derived clarifications while preserving the existing core invariants:

- user-requested analysis depth is distinct from the mandatory minimum reasoning floor required by consequence, authority, safety and evidence;
- task/session context and retrieved or supplied content may specialize the work but cannot silently rewrite non-disableable safeguards, become authority, or act as a higher-priority instruction channel merely because they contain imperative text.

These are behavioral protocol semantics. They do not add runtime enforcement, persistence, hashing, identity, authorization, or execution controls.

## Getting started

Read [SKILL.md](SKILL.md), then follow [INSTALLATION.md](INSTALLATION.md) for the platform's supported instruction mechanism. Start with one ordinary analysis task; request explicit assumptions and evidence status rather than a fixed answer length. Treat platform-specific activation instructions as configuration guidance, not evidence that a model follows every rule. Use [the evaluation protocol](evaluations/README.md) to measure behavior under a named model/version and configuration. For optional runtime allocation, read [Reasoning Effort and Allocation](references/reasoning-effort.md) and the provider-neutral [ReasoningPlan schema](schemas/reasoning-plan.schema.json).

## Scope and compatibility

The repository defines PRP v1.1. The hub currently selects an earlier pinned PRP revision as an optional layer; `component-lock.json` remains authoritative for the integrated version. The [evaluation suite](evaluations/README.md) defines baseline-versus-PRP comparisons; it supplies no general claim of measured uplift, safety or model-independent efficacy.

Test results, run commentary and historical qualification records are maintained in the [central test hub](https://github.com/cogno-us/cognous-stack-qualification/blob/main/results/readme-commentary/index.md). Read them against their recorded source revisions; source selection and deployment approval are separate decisions.

## Limitations and deployment decisions

PRP does not add persistent state, authenticate institutions, intercept tools, create a sandbox or guarantee truthfulness. Static artifact checks cannot establish model-behavior efficacy. Model-behavior efficacy must be measured for named models/configurations and is not established by installation or schema validity.

Review original artifacts and their exact source revisions before extending a claim to a new environment. New dependencies, authority sources, destinations or enforcement mechanisms need their own compatibility and qualification. A passing reference case is not a certification of an enterprise deployment.

## Repository guide

Use these sources for details; their historical checkpoints retain the status and scope of the work they recorded:

- [SKILL.md](SKILL.md)
- [INSTALLATION.md](INSTALLATION.md)
- [STACK_INTEGRATION.md](STACK_INTEGRATION.md)
- [references/reasoning-effort.md](references/reasoning-effort.md)
- [references/runtime-control.md](references/runtime-control.md)
- [references/source-lineage.md](references/source-lineage.md)
- [schemas/runtime-control.schema.json](schemas/runtime-control.schema.json)
- [policies/runtime-control.v1.json](policies/runtime-control.v1.json)
- [evaluations/control-cases.json](evaluations/control-cases.json)
- [schemas/reasoning-plan.schema.json](schemas/reasoning-plan.schema.json)
- [examples/reasoning-plan.conflicting-evidence.json](examples/reasoning-plan.conflicting-evidence.json)
- [adapters/README.md](adapters/README.md)
- [evaluations/README.md](evaluations/README.md)
- [evaluations/cases.yaml](evaluations/cases.yaml)
- [evaluations/routing-cases.yaml](evaluations/routing-cases.yaml)

For a nontechnical introduction, read the [business overview](collateral/business-collateral.md) and [one-page overview](collateral/one-page-overview.md). Both describe this component's role and evidence limits, not additional runtime features.

## Contributing and attribution

Propose focused changes through repository issues and pull requests. Keep evidence-linked claims, preserve historical records and separate proposed features from accepted implementation.

See [LICENSE](LICENSE) and [attribution](NOTICE) for the existing terms and third-party scope. Developed by [Cognous](https://cogno.us); no licensing change is part of this documentation update.

---

## Bibliography

Selected external sources from the October 2026 research review. These inform evaluation questions; they do not establish Cognous implementation, adoption, conformance or production qualification.

- [Mick Yang et al. *AI Epistemic Risks: Emerging Mechanisms & Evidence* (2026)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6873005). Research synthesis on persuasion, cognitive offloading and feedback loops; context for evidence quality and independent judgment.
- [John Berryman and Albert Ziegler. *Prompt Engineering for LLMs: The Art and Science of Building Large Language Model–Based Applications*. O’Reilly (2024)](https://www.oreilly.com/library/view/prompt-engineering-for/9781098156145/). Practitioner reference for prompt design and application evaluation; not proof that a behavioral protocol is effective.
- [John W. Creswell and J. David Creswell. *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches*, fifth edition. SAGE (2018)](https://edge.sagepub.com/creswellrd5e). Research-methods reference for explicit questions, comparison designs and interpretation limits.

See the [research bibliography](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/research-bibliography.md) for review scope and source-verification limits.

## Cognous stack components

The six groups organize component responsibilities. They are not an execution
sequence or a requirement to install every component. The [hub lock](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json)
defines the selected integration; [release status](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md)
defines its evidence and limits.

| Group | Components |
| --- | --- |
| **01 · Knowledge & Provenance** | [The Index (Evidence Registry)](https://github.com/cogno-us/cognous-evidence-registry) · [BitRep (Evidence Attestation)](https://github.com/cogno-us/cognous-evidence-attestation) |
| **02 · Institutional Governance** | [Alvorada (Institutional Governance)](https://github.com/cogno-us/cognous-institutional-governance) · authority contracts |
| **03 · Declaration & Policy Control** | [Action Manifest](https://github.com/cogno-us/cognous-action-manifest) · [Control Plane](https://github.com/cogno-us/cognous-control-plane) |
| **04 · Constrained Execution** | [Execution Runtime (Moltbot Safe)](https://github.com/cogno-us/cognous-execution-runtime) |
| **05 · Replay & Evidence** | [Replay Bundle](https://github.com/cogno-us/cognous-replay-bundle) · [Governance Evidence Pack](https://github.com/cogno-us/cognous-governance-evidence-pack) · [ODES](https://github.com/cogno-us/open-decision-evidence-standard) |
| **06 · Reasoning & Human Oversight** | [PRP](https://github.com/cogno-us/portable-reasoning-protocol) · [Research Intelligence](https://github.com/cogno-us/research-intelligence-protocol) · [TFA](https://github.com/cogno-us/truth-freedom-agency-protocol) |

**Cross-cutting exchange:** [Governed Exchange (GAX/IMX)](https://github.com/cogno-us/cognous-governed-exchange) connects
governed messages, recipient assessment and continuity across the groups. It is
separate from Alvorada's institutional authority framework.

Execution Runtime and Moltbot Safe name the same repository here. The supported
Cognous Python execution boundary remains distinct from the retained upstream
application. PRP, Research Intelligence and TFA are optional behavioral
instructions; they do not enforce authorization or substitute for human oversight.
A signature, registry entry, message receipt or evidence summary does not grant
execution authority.


## Repository locations

See the [repository rename map and compatibility notes](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/repository-renames.md) for current component URLs. Existing package names, schema identifiers and retained producer identities are unchanged.

<!-- Retained anchors for existing documentation links. -->
<a id="evidence-and-supported-scope"></a>
