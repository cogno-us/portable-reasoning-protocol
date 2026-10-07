# Portable Reasoning Protocol v1.0 — One-Page Overview

## Purpose

PRP is a reusable SKILL.md-based instruction package for general-purpose AI work. It asks a model to calibrate rigor to consequence, distinguish evidence from inference, state material uncertainty and preserve the user's agency. These are behavioral instructions, not runtime enforcement.

## Problem

Fluent output can hide unsupported certainty, invented sources, unstated assumptions or a premature conclusion. Teams need a shared way to ask for evidence discipline without requiring every routine task to become a long report.

## What It Provides

- **Adaptive rigor:** Escalate scrutiny when consequence, uncertainty, novelty or irreversibility increases.
- **Claim discipline:** Separate observed, inferred, estimated, hypothetical, normative and unknown statements.
- **Hallucination controls:** Instruct the model not to fabricate facts, citations, capabilities, tool results or completed actions.
- **Agency preservation:** Present material tradeoffs and avoid manipulative pressure or unnecessary requests.

## Where It Fits

A user supplies a decision question and asks PRP to distinguish facts, assumptions and remaining uncertainty. The assistant proposes options at a depth appropriate to the task. If a consequential action follows, the deployment must separately check authority and constrain execution; a reasoning conclusion or statement of confidence cannot replace those checks.

A valid signature, chain inclusion, message receipt, reasoning instruction or evidence-package digest does not authorize execution. Institutional authority must be supplied and evaluated through the appropriate trusted boundary.

## Evidence and Limits

The [accepted hub lock](https://github.com/cogno-us/cognous-open-control-stack/blob/5737267d94d2b445735c95e8480a31de73a2abe8/component-lock.json) selects this component at `cb137f028e92448a56e785e3d4ea074b444fa225`. Read the component's [README](../README.md) for version-specific acceptance and the [hub support ledger](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md) for the executed scope. Component acceptance is not automatic adoption of newer revisions or production qualification.

PRP does not add persistent state, authenticate institutions, intercept tools, create a sandbox or guarantee truthfulness. The hub performs static artifact checks only. Model-behavior efficacy must be measured for named models/configurations and is not established by installation or schema validity.

## Practical Next Step

Choose one bounded example and follow the [README](../README.md). Compare expected and observed results and retain uncertainty. The [business collateral](business-collateral.md) supplies evaluation questions and the component's wider context.

[Cognous](https://cogno.us) · [Source](https://github.com/cogno-us/portable-reasoning-protocol) · [All stack components](https://github.com/cogno-us/cognous-open-control-stack). Existing licenses and notices apply.
