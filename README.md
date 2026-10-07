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

## Overview

PRP is a reusable SKILL.md-based instruction package for general-purpose AI work. It asks a model to calibrate rigor to consequence, distinguish evidence from inference, state material uncertainty and preserve the user's agency. These are behavioral instructions, not runtime enforcement.

**Implementation status:** this README describes merged public reference work. Component acceptance, selection in the hub and execution of a qualification are separate facts. The selected revision for this component is `cb137f028e92448a56e785e3d4ea074b444fa225`; the [hub lock](https://github.com/cogno-us/cognous-open-control-stack/blob/5737267d94d2b445735c95e8480a31de73a2abe8/component-lock.json) is the source of that integration choice.

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

## How it works

A user supplies a decision question and asks PRP to distinguish facts, assumptions and remaining uncertainty. The assistant proposes options at a depth appropriate to the task. If a consequential action follows, the deployment must separately check authority and constrain execution; a reasoning conclusion or statement of confidence cannot replace those checks.

A valid signature, chain inclusion, message receipt, reasoning instruction or evidence-package digest does not authorize execution. Institutional authority must be supplied and evaluated through the appropriate trusted boundary.

## v1.1 alignment

PRP v1.1 incorporates two implementation-derived clarifications while preserving the existing core invariants:

- user-requested analysis depth is distinct from the mandatory minimum reasoning floor required by consequence, authority, safety and evidence;
- task/session context and retrieved or supplied content may specialize the work but cannot silently rewrite non-disableable safeguards, become authority, or act as a higher-priority instruction channel merely because they contain imperative text.

These are behavioral protocol semantics. They do not add runtime enforcement, persistence, hashing, identity, authorization, or execution controls.

## Getting started

Read [SKILL.md](SKILL.md), then follow [INSTALLATION.md](INSTALLATION.md) for the platform's supported instruction mechanism. Start with one ordinary analysis task; request explicit assumptions and evidence status rather than a fixed answer length. Treat platform-specific activation instructions as configuration guidance, not evidence that a model follows every rule. Use [the evaluation protocol](evaluations/README.md) to measure behavior under a named model/version and configuration.

## Evidence and supported scope

The hub selects a pinned PRP v1.1 instruction artifact as an optional layer. Its recorded checks are static artifact/JSON checks only. The [evaluation suite](evaluations/README.md) defines baseline-versus-PRP comparisons; it supplies no general claim of measured uplift, safety or model-independent efficacy.

The accepted [hub persistence-generation evidence](https://github.com/cogno-us/cognous-open-control-stack/blob/5737267d94d2b445735c95e8480a31de73a2abe8/examples/control-plane-store-adoption/qualification-summary.json) records 915 Python tests in each of two repetitions, 35 matrix entries satisfying their gates and 120 separate mocked OpenShell tests. Those are aggregate hub results, not a per-component test count or a claim of production readiness. Optional behavioral layers receive static checks only. The [support ledger](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md) separates implementation, execution and adoption.

## Limitations and deployment decisions

PRP does not add persistent state, authenticate institutions, intercept tools, create a sandbox or guarantee truthfulness. The hub performs static artifact checks only. Model-behavior efficacy must be measured for named models/configurations and is not established by installation or schema validity.

Review original artifacts and their exact source revisions before extending a claim to a new environment. New dependencies, authority sources, destinations or enforcement mechanisms need their own compatibility and qualification. A passing reference case is not a certification of an enterprise deployment.

## Repository guide

Use these sources for details; their historical checkpoints retain the status and scope of the work they recorded:

- [SKILL.md](SKILL.md)
- [INSTALLATION.md](INSTALLATION.md)
- [STACK_INTEGRATION.md](STACK_INTEGRATION.md)
- [evaluations/README.md](evaluations/README.md)
- [evaluations/cases.yaml](evaluations/cases.yaml)

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

[Stack hub](https://github.com/cogno-us/cognous-open-control-stack) · [Selected pins](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json) · [Evidence and limits](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md)

Component links are navigation, not a requirement to install every component. The hub lock determines its supported integration.

| Component | Responsibility |
|---|---|
| [Cognous Action Manifest](https://github.com/cogno-us/cognous-action-manifest) | Declare the action before evaluating permission |
| [Cognous Control Plane](https://github.com/cogno-us/cognous-control-plane) | Evaluate proposals against authority and preserve the decision record |
| [Cognous Replay Bundle](https://github.com/cogno-us/cognous-replay-bundle) | Reconstruct what the retained records support |
| [Cognous Governance Evidence Pack](https://github.com/cogno-us/cognous-governance-evidence-pack) | Turn traceable runtime records into reviewable governance evidence |
| [Open Decision Evidence Standard](https://github.com/cogno-us/open-decision-evidence-standard) | Portable decision evidence across system and organizational boundaries |
| [Cognous Governed Exchange](https://github.com/cogno-us/cognous-governed-exchange) | Governed exchange and continuity for a bounded synthetic workflow |
| [Cognous Execution Runtime](https://github.com/cogno-us/cognous-execution-runtime) | Constrained execution beneath independent current authorization |
| [Cognous Evidence Attestation](https://github.com/cogno-us/cognous-evidence-attestation) | Verify issuer signatures under explicit trust assumptions |
| [Cognous Evidence Registry](https://github.com/cogno-us/cognous-evidence-registry) | A local blockchain reference for claims, evidence commitments and lifecycle history |
| [Research Intelligence Protocol v1.0](https://github.com/cogno-us/research-intelligence-protocol) | Disciplined discovery and cross-domain abstraction, kept separate |
| [TFA Protocol (S43)](https://github.com/cogno-us/truth-freedom-agency-protocol) | Truth · Freedom · Agency |
| [Cognous Institutional Governance](https://github.com/cogno-us/cognous-institutional-governance) | Alvorada: authority, challenge and correction for institutions |

## Repository locations

See the [repository rename map and compatibility notes](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/repository-renames.md) for current component URLs. Existing package names, schema identifiers and retained producer identities are unchanged.
