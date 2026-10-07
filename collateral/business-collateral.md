# Portable Reasoning Protocol v1.0 — Business Collateral

## 1. Executive Summary

PRP is a reusable SKILL.md-based instruction package for general-purpose AI work. It asks a model to calibrate rigor to consequence, distinguish evidence from inference, state material uncertainty and preserve the user's agency. These are behavioral instructions, not runtime enforcement.

## 2. The Business Problem

Fluent output can hide unsupported certainty, invented sources, unstated assumptions or a premature conclusion. Teams need a shared way to ask for evidence discipline without requiring every routine task to become a long report.

## 3. The Component in One View

| Capability | Practical role |
|---|---|
| Adaptive rigor | Escalate scrutiny when consequence, uncertainty, novelty or irreversibility increases. |
| Claim discipline | Separate observed, inferred, estimated, hypothetical, normative and unknown statements. |
| Hallucination controls | Instruct the model not to fabricate facts, citations, capabilities, tool results or completed actions. |
| Agency preservation | Present material tradeoffs and avoid manipulative pressure or unnecessary requests. |
| Optional handoff | Preserve proposal/evidence distinctions for downstream systems without creating authority. |

## 4. Who Should Evaluate It

Engineers can inspect the reference contracts and examples; enterprise architecture, security and governance reviewers can examine the boundary and evidence. Evaluate this component for its named responsibility rather than as a complete governance platform.

## 5. A Bounded Workflow

A user supplies a decision question and asks PRP to distinguish facts, assumptions and remaining uncertainty. The assistant proposes options at a depth appropriate to the task. If a consequential action follows, the deployment must separately check authority and constrain execution; a reasoning conclusion or statement of confidence cannot replace those checks.

This is a reference use case. Adopting the format or running the example does not establish a production deployment, institutional acceptance or measured business benefit.

## 6. Relationship to the Stack

This component contributes **portable instructions for evidence-bounded reasoning**. The [Cognous Open Control Stack](https://github.com/cogno-us/cognous-open-control-stack) connects declared proposals, independent authority, constrained execution and retained review evidence. Components remain separately owned and versioned; the [selected lock](https://github.com/cogno-us/cognous-open-control-stack/blob/5737267d94d2b445735c95e8480a31de73a2abe8/component-lock.json) determines which revisions participate in the supported integration.

A valid signature, chain inclusion, message receipt, reasoning instruction or evidence-package digest does not authorize execution. Institutional authority must be supplied and evaluated through the appropriate trusted boundary.

## 7. What the Evidence Supports

The hub selects a pinned PRP v1.0 instruction artifact as an optional layer. Its recorded checks are static artifact/JSON checks only. The [evaluation suite](../evaluations/README.md) defines baseline-versus-PRP comparisons; it supplies no general claim of measured uplift, safety or model-independent efficacy.

The [accepted hub evidence](https://github.com/cogno-us/cognous-open-control-stack/blob/5737267d94d2b445735c95e8480a31de73a2abe8/examples/control-plane-store-adoption/qualification-summary.json) supports bounded synthetic integration at its exact pins. Aggregate test totals do not establish deployment benefit, compliance or independent real-world verification. The [support ledger](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md) distinguishes the standard reference, separate protected-worker campaign and unqualified production work.

## 8. What It Does Not Establish

PRP does not add persistent state, authenticate institutions, intercept tools, create a sandbox or guarantee truthfulness. The hub performs static artifact checks only. Model-behavior efficacy must be measured for named models/configurations and is not established by installation or schema validity.

## 9. Evaluation Questions

- Which exact input, output and source revision will the receiving system consume?
- Who supplies trusted authority or evidence, and which assumptions remain outside this component?
- Can a reviewer trace the result to retained sources, including rejected or missing information?
- Which documented checks were actually executed in the intended environment?
- What deployment-specific work is required before relying on the result?

## 10. Why Open Reference Material Matters

Public formats, source, examples and evidence allow reviewers to inspect the claimed boundary and reproduce its checks. They also expose what has not been tested. Openness supports review; it does not substitute for independent assurance or operating responsibility.

## 11. Practical Next Step

Follow the [README](../README.md) and select one bounded use case. Inspect its inputs and expected outputs, reproduce the documented checks where prerequisites are available, and record failures and unresolved assumptions alongside passes. Use the [one-page overview](one-page-overview.md) for initial stakeholder orientation.

## 12. Status and Attribution

This collateral summarizes merged public material at repository `44bbd1ee9d9feba1e73c3fa54862b690c571daa2` and the accepted hub baseline `5737267d94d2b445735c95e8480a31de73a2abe8`. It does not anticipate pending branches. The protected-worker result applies only to its recorded Linux/bubblewrap fixture; live OpenShell and logical-intent prevention are not hub-supported at this snapshot.

[Cognous](https://cogno.us) · [Source repository](https://github.com/cogno-us/portable-reasoning-protocol) · [Stack responsibilities](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/architecture.md). Existing licenses and third-party notices remain controlling.
