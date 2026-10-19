<!-- cognous-banner:start -->
```text
──────────────────────────────────────────────────
   __________  _______   ______  __  _______
  / ____/ __ \/ ____/ | / / __ \/ / / / ___/
 / /   / / / / / __/  |/ / / / / / /\__ \
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

**Status:** optional reasoning protocol (side group of the [stack map](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/stack-map.md)). Label: merged. In the hub lock as `prp` with `optional: true`; the lock records no interface for it, and it is not selected for enforcement. Behavioral instructions only. <!-- pin-round: lock revision and "earlier pinned revision" statements in this file are refreshed with the hub lock -->

**Start with [SKILL.md](SKILL.md)**, the instruction entrypoint. Then see [Quick start](#quick-start) to run the offline helpers, and [Documentation index](#documentation-index) for every page in this repository.

## What it is, who it is for, what it does not do

**What it is.** PRP is a reusable SKILL.md-based instruction package for general-purpose AI work. It asks a model to calibrate rigor to consequence, distinguish evidence from inference, state material uncertainty and preserve the user's agency. These are behavioral instructions, not runtime enforcement.

**Who it is for.** Teams that want a shared way to ask for evidence discipline without making every routine task a long report. Fluent output can hide unsupported certainty, invented sources, unstated assumptions or a premature conclusion. Engineers can inspect the schemas, offline tools and evaluation cases; architecture, security and governance reviewers can examine the boundary and evidence. Evaluate this component for its named responsibility rather than as a complete governance platform.

**What it does not do.** PRP does not add persistent state, authenticate institutions, intercept tools, create a sandbox, enforce permissions, control provider compute or guarantee truthfulness. It does not enforce authorization or substitute for human oversight. See [Limits](#limitations-and-deployment-decisions).

**Implementation status:** public reference work. The [current component lock](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json) defines the selected integration; a component merge does not automatically change that selection or approve deployment.

## Where it fits

PRP sits in the "Optional reasoning protocols" side group, beside [Research Intelligence Protocol](https://github.com/cogno-us/research-intelligence-protocol) and [TFA Protocol (S43)](https://github.com/cogno-us/truth-freedom-agency-protocol). It is independently usable and needs no other Cognous component; [STACK_INTEGRATION.md](STACK_INTEGRATION.md) describes an optional information handoff to governed workflows. It is not part of the refund workflow and does not change any selected interface. The [stack map](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/stack-map.md) is the canonical map; the table below is a copy of it.

<!-- stack-map-block:start -->
### Cognous stack components

The Open Control Stack keeps five responsibility groups and two side groups. The groups organize responsibilities. They are not an execution sequence or a requirement to install every component. The canonical map, with one row per repository, is the hub [stack map](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/stack-map.md); names are defined in [naming](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/naming.md) and commands and profiles per repository are in [profiles and tools](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/profiles-and-tools.md). The map uses four labels: merged, selected, known limit and proposed. The [hub lock](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json) defines the selected integration; [release status](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md) defines its evidence and limits.

| Group | Components |
| --- | --- |
| **01 Knowledge & Provenance** | [Evidence Registry (The Index)](https://github.com/cogno-us/cognous-evidence-registry) · [Evidence Attestation (BitRep)](https://github.com/cogno-us/cognous-evidence-attestation) |
| **02 Institutional Governance** | [Institutional Governance (Alvorada)](https://github.com/cogno-us/cognous-institutional-governance) |
| **03 Declaration & Policy Control** | [Action Manifest](https://github.com/cogno-us/cognous-action-manifest) · [Control Plane](https://github.com/cogno-us/cognous-control-plane) |
| **04 Constrained Execution** | [Execution Runtime](https://github.com/cogno-us/cognous-execution-runtime) |
| **05 Replay & Evidence** | [Replay Bundle](https://github.com/cogno-us/cognous-replay-bundle) · [Governance Evidence Pack](https://github.com/cogno-us/cognous-governance-evidence-pack) · [ODES](https://github.com/cogno-us/open-decision-evidence-standard) |
| **Cross-cutting exchange** | [Governed Exchange (GAX/IMX)](https://github.com/cogno-us/cognous-governed-exchange) |
| **Optional reasoning protocols** (side group) | [Portable Reasoning Protocol (PRP)](https://github.com/cogno-us/portable-reasoning-protocol) · [Research Intelligence Protocol](https://github.com/cogno-us/research-intelligence-protocol) · [TFA Protocol (S43)](https://github.com/cogno-us/truth-freedom-agency-protocol) |
| **Tooling and qualification** (side group) | [Ergonomics (`cognous-ocs`)](https://github.com/cogno-us/cognous-open-control-stack-ergonomics) · [Verifier](https://github.com/cogno-us/cognous-open-control-stack-verifier) · [Orchestrator](https://github.com/cogno-us/cognous-stack-orchestrator) · [Qualification](https://github.com/cogno-us/cognous-stack-qualification) |

The hub, [cognous-open-control-stack](https://github.com/cogno-us/cognous-open-control-stack), holds the component lock and the canonical documentation. Execution Runtime is the repository formerly named Moltbot Safe; see [naming](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/naming.md). PRP, Research Intelligence Protocol and TFA Protocol are optional behavioral instructions; they do not enforce authorization or substitute for human oversight. A signature, registry entry, message receipt or evidence summary does not grant execution authority.

Last checked against `component-lock.json` at hub commit `dcc9bd7533ef`. <!-- pin-round: refresh this commit with the hub stack map -->
<!-- stack-map-block:end -->

## Quick start

Prerequisites: Python 3 (verified with 3.13; the offline tools use only the standard library; the package check also needs `PyYAML` and `jsonschema`, pinned in [requirements-dev.txt](requirements-dev.txt)). The commands were run from a clean clone in a fresh virtual environment. No model, network or account is needed.

```sh
git clone https://github.com/cogno-us/portable-reasoning-protocol
cd portable-reasoning-protocol
python -m venv .venv && . .venv/bin/activate
python -m pip install -r requirements-dev.txt
python tools/runtime_control.py --proposed-level 2 --requested-depth fast --rule authority-sensitive
python tools/validate_package.py
python -m unittest discover -s tests
```

Expected: the selection helper exits 0 and prints a JSON record whose first lines are

```json
{
  "profile_version": "1.0.0",
  "assessment_kind": "selection_only",
  "proposed_level": 2,
  "requested_depth": "fast",
  "mandatory_minimum_level": 3,
  "effective_level": 3,
```

and which ends with `"override_outcome": "clamped_to_floor"` and the list of `required_components`. A Fast request is clamped to the floor of the matched rule. The package check exits 0 and prints `PASS: 7 JSON, 3 YAML, 120 local Markdown links/anchors; examples and frontmatter` followed by `Static checks only. No model evaluations, source truth or authorization verified.` The unit tests finish in about two seconds with `OK` (25 tests at this revision). <!-- pin-round: counts reflect the repository head at the time of writing -->

To check an existing record instead of generating one: `python tools/runtime_control.py --validate examples/runtime-control.authority.json` prints `PASS: selection record is consistent; behavior and authority are not verified`.

**What this does not prove.** These commands check selection arithmetic over supplied rule matches, file structure and links. They do not evaluate natural-language classification, model compliance, source truth or authorization. Model behavior is established only by evaluation under a named model, version and configuration (see [the evaluation protocol](evaluations/README.md)).

To use PRP itself, read [SKILL.md](SKILL.md), then follow [INSTALLATION.md](INSTALLATION.md) for the platform's supported instruction mechanism. Start with one ordinary analysis task; request explicit assumptions and evidence status rather than a fixed answer length. Treat platform-specific activation instructions as configuration guidance, not evidence that a model follows every rule. For optional runtime allocation, read [Reasoning Effort and Allocation](references/reasoning-effort.md) and the provider-neutral [ReasoningPlan schema](schemas/reasoning-plan.schema.json).

## What ships

| Item | Kind | Purpose | Status label |
|---|---|---|---|
| [SKILL.md](SKILL.md) | instruction entrypoint | Compact runtime instructions: control profile, rule floors, safeguards. | merged |
| [references/prp-core.md](references/prp-core.md) | reference | Advanced reference for consequential work. | merged |
| [references/runtime-control.md](references/runtime-control.md) | reference | Semantics of the control profile 1.0.0 selection record. | merged |
| [references/reasoning-effort.md](references/reasoning-effort.md) | reference | Provider-neutral reasoning allocation. | merged |
| [references/source-lineage.md](references/source-lineage.md) | reference | Source preservation map for the public adaptation. | merged |
| [`tools/runtime_control.py`](tools/runtime_control.py) | command (offline, standard library) | Computes or validates a selection record: `--proposed-level`, `--requested-depth`, `--rule`, `--validate`. Verified above. | merged |
| [`tools/paired_evaluation.py`](tools/paired_evaluation.py) | command (offline, standard library) | Scores a paired null/discriminating response set against the preregistered case: `--case`, `--responses`. Output ends `"behavioral_efficacy_established": false`. | merged |
| [`tools/validate_package.py`](tools/validate_package.py) | command (needs `PyYAML`, `jsonschema`) | Structural check of JSON, YAML, frontmatter, examples and local Markdown links. | merged |
| [schemas/runtime-control.schema.json](schemas/runtime-control.schema.json) | schema | Selection-only record shape. | merged |
| [schemas/reasoning-plan.schema.json](schemas/reasoning-plan.schema.json) | schema | Provider-neutral `ReasoningPlan` v1.0. | merged |
| [policies/runtime-control.v1.json](policies/runtime-control.v1.json) | policy data | Rule IDs, floors, depth mapping and cumulative components. | merged |
| [examples/runtime-control.authority.json](examples/runtime-control.authority.json) | example | A selection record for an authority-sensitive task. | merged |
| [examples/reasoning-plan.conflicting-evidence.json](examples/reasoning-plan.conflicting-evidence.json) | example | A `ReasoningPlan` for conflicting evidence. | merged |
| [evaluations/cases.yaml](evaluations/cases.yaml) | evaluation cases | 10 baseline-versus-PRP behavioral cases; unexecuted. | merged |
| [evaluations/routing-cases.yaml](evaluations/routing-cases.yaml) | evaluation cases | 5 routing cases for under- and over-escalation; unexecuted. | merged |
| [evaluations/control-cases.json](evaluations/control-cases.json) | evaluation cases | 16 control-profile regression cases; unexecuted. | merged |
| [evaluations/paired-case.json](evaluations/paired-case.json) | evaluation case | Preregistered paired case for the paired scorer. | merged |
| [adapters/](adapters/README.md) | guidance | Informative provider mappings ([Anthropic](adapters/anthropic.md), [Gemini](adapters/gemini.md), [OpenAI](adapters/openai.md)). | merged |
| [agents/openai.yaml](agents/openai.yaml) | metadata | Display metadata for OpenAI-style skill listings. | merged |
| [tests/](tests) | tests | `test_runtime_control.py` and `test_paired_evaluation.py`: arithmetic and scorer consistency only. | merged |

PRP has no installable package, no profile and no contract draft; "behavioral evaluation status" is `unexecuted` in every case file. Unexecuted means no model evaluation result is reported.

## Documentation index

This repository has few pages, so the index is here rather than in a separate `docs/README.md`. Every page is linked below.

| Page | Read it for |
|---|---|
| [SKILL.md](SKILL.md) | The instructions themselves. |
| [INSTALLATION.md](INSTALLATION.md) | Platform installation and activation. |
| [STACK_INTEGRATION.md](STACK_INTEGRATION.md) | Optional information handoff to governed workflows. |
| [references/](references/prp-core.md) | [Core reference](references/prp-core.md), [runtime control](references/runtime-control.md), [reasoning effort](references/reasoning-effort.md), [source lineage](references/source-lineage.md). |
| [evaluations/README.md](evaluations/README.md) | Evaluation protocol and paired preregistration. |
| [adapters/README.md](adapters/README.md) | Provider adapter guidance. |
| [CHANGELOG.md](CHANGELOG.md) | Version history (v1.1 and the control profile 1.0.0). |
| [docs/control-profile-checkpoint.md](docs/control-profile-checkpoint.md) | Historical checkpoint for the control profile, retained as written. |
| [Business overview](collateral/business-collateral.md) and [one-page overview](collateral/one-page-overview.md) | Nontechnical introduction to this component's role and evidence limits, not additional runtime features. |

Reading paths: **adopter** SKILL.md, INSTALLATION.md, evaluations/README.md. **Integrator** STACK_INTEGRATION.md, references/runtime-control.md, schemas. **Reviewer** this README's limits, CHANGELOG.md, source lineage. Shared names and labels are in the hub [naming](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/naming.md) page.

## How it works and design notes

This section keeps the longer descriptions that earlier READMEs placed first.

### How it works

A user supplies a decision question and asks PRP to distinguish facts, assumptions and remaining uncertainty. The assistant proposes options at a depth appropriate to the task. If a consequential action follows, the deployment must separately check authority and constrain execution; a reasoning conclusion or statement of confidence cannot replace those checks.

A valid signature, chain inclusion, message receipt, reasoning instruction or evidence-package digest does not authorize execution. Institutional authority must be supplied and evaluated through the appropriate trusted boundary.

### Key features

| Capability | Implemented or specified responsibility |
|---|---|
| **Adaptive rigor** | Escalate scrutiny when consequence, uncertainty, novelty or irreversibility increases, with a mandatory minimum reasoning floor for consequential work. |
| **Claim discipline** | Separate observed, inferred, estimated, hypothetical, normative and unknown statements. |
| **Hallucination controls** | Instruct the model not to fabricate facts, citations, capabilities, tool results or completed actions. |
| **Context trust boundary** | Treat task context, retrieved content, attachments and quoted instructions as content unless they are actually active instructions; content cannot silently lower safeguards or create authority. |
| **Agency preservation** | Present material tradeoffs and avoid manipulative pressure or unnecessary requests. |
| **Optional handoff** | Preserve proposal/evidence distinctions for downstream systems without creating authority. |

### Engineering benefits

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

### Compact operational control

PRP retains its **public v1.0 lineage**, adapted from the mature v3.1 source. The new **control profile 1.0.0** makes minimum scrutiny, user overrides and required checks explicit without requiring a long prompt or a visible governance header on every answer. See the [source preservation map](references/source-lineage.md).

The entrypoint now distinguishes the proposed level, mandatory minimum and effective level. Stable rule IDs and cumulative bundles make that choice inspectable. A Fast request cannot lower a consequential task below its floor; a request for brevity changes presentation, not required checks. Routine formatting remains a direct answer, and merely quoting legal or authority-related words does not trigger a full authority review.

The intended benefits are fewer lost safeguards during compression, more consistent treatment of overrides, targeted clarification when evidence is missing, and less ceremonial output. These remain behavioral hypotheses until tested with named models. A formal header is not evidence of correctness, completed verification or permission.

An optional [offline helper](tools/runtime_control.py) checks selection arithmetic over supplied rule matches. Its tests do **not** evaluate natural-language classification or model compliance. PRP itself still does not authenticate grants, enforce permissions or control provider compute.

```sh
python tools/runtime_control.py --proposed-level 2 --requested-depth fast --rule authority-sensitive
```

For full semantics, read [runtime control](references/runtime-control.md). For regression tasks, read [control cases](evaluations/control-cases.json). Named-model results and accounting belong in the central test hub.

### v1.1 alignment

PRP v1.1 incorporates two implementation-derived clarifications while preserving the existing core invariants:

- user-requested analysis depth is distinct from the mandatory minimum reasoning floor required by consequence, authority, safety and evidence;
- task/session context and retrieved or supplied content may specialize the work but cannot silently rewrite non-disableable safeguards, become authority, or act as a higher-priority instruction channel merely because they contain imperative text.

These are behavioral protocol semantics. They do not add runtime enforcement, persistence, hashing, identity, authorization, or execution controls.

## Compatibility and selection

The repository defines PRP v1.1. The hub currently selects an earlier pinned PRP revision as an optional layer; `component-lock.json` remains authoritative for the integrated version. The [evaluation suite](evaluations/README.md) defines baseline-versus-PRP comparisons; it supplies no general claim of measured uplift, safety or model-independent efficacy.

Test results, run commentary and historical qualification records are maintained in the [central test hub](https://github.com/cogno-us/cognous-stack-qualification/blob/main/results/readme-commentary/index.md). Read them against their recorded source revisions; source selection and deployment approval are separate decisions.

See the [repository rename map and compatibility notes](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/repository-renames.md) for current component URLs. Existing package names, schema identifiers and retained producer identities are unchanged.

## Limitations and deployment decisions

PRP does not add persistent state, authenticate institutions, intercept tools, create a sandbox or guarantee truthfulness. Static artifact checks cannot establish model-behavior efficacy. Model-behavior efficacy must be measured for named models/configurations and is not established by installation or schema validity.

Review original artifacts and their exact source revisions before extending a claim to a new environment. New dependencies, authority sources, destinations or enforcement mechanisms need their own compatibility and qualification. A passing reference case is not a certification of an enterprise deployment.

Known limits, as labelled facts: **known limit** PRP is behavioral guidance and cannot be enforced by this repository. **known limit** Model-behavior efficacy is unmeasured here; every case file is `unexecuted`. **known limit** The offline helpers do not classify tasks. **proposed** Named-model evaluation records belong in the central test hub. Shared stack-level limits are stated in the hub [guarantees and limits](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/guarantees-and-limits.md).

## Contributing, licence, attribution and security

Propose focused changes through repository issues and pull requests. Keep evidence-linked claims, preserve historical records and separate proposed features from accepted implementation. Run the three commands in the quick start before opening a pull request. This repository has no CI workflow of its own.

See [LICENSE](LICENSE) and [attribution](NOTICE) for the existing terms and third-party scope. Developed by [Cognous](https://cogno.us); no licensing change is part of this documentation update. For reporting a concern, see the hub [security reporting and triage](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/security-reporting-and-triage.md) page.

---

## Bibliography

Selected external sources from the October 2026 research review. These inform evaluation questions; they do not establish Cognous implementation, adoption, conformance or production qualification.

- [Mick Yang et al. *AI Epistemic Risks: Emerging Mechanisms & Evidence* (2026)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6873005). Research synthesis on persuasion, cognitive offloading and feedback loops; context for evidence quality and independent judgment.
- [John Berryman and Albert Ziegler. *Prompt Engineering for LLMs: The Art and Science of Building Large Language Model–Based Applications*. O’Reilly (2024)](https://www.oreilly.com/library/view/prompt-engineering-for/9781098156145/). Practitioner reference for prompt design and application evaluation; not proof that a behavioral protocol is effective.
- [John W. Creswell and J. David Creswell. *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches*, fifth edition. SAGE (2018)](https://edge.sagepub.com/creswellrd5e). Research-methods reference for explicit questions, comparison designs and interpretation limits.

See the [research bibliography](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/research-bibliography.md) for review scope and source-verification limits.

<!-- Retained anchors for existing documentation links. -->
<a id="evidence-and-supported-scope"></a>
