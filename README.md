# Portable Reasoning Protocol (PRP) v1.0

**A portable reasoning layer for more rigorous, evidence-bounded AI work.**

Developed by **[Cognous](https://cogno.us)**.

PRP is a reusable reasoning protocol for general-purpose AI systems. It is designed to improve the quality of analysis without forcing every task into heavyweight governance. The protocol adapts its rigor to the task: simple work stays simple; consequential, ambiguous, evidentiary, novel, or difficult-to-reverse work receives deeper scrutiny.

This repository packages PRP v1.0 as a `SKILL.md`-based Skill so the protocol can be inspected, versioned, forked, tested, and reused.

## What PRP is

PRP is a control layer for reasoning. It does not try to give an AI system a new personality or domain identity. Instead, it constrains how the system moves from evidence to claims, assumptions to conclusions, possibility to actuality, and confidence to action.

Its central idea is straightforward:

> Do not eliminate ideas. Eliminate invalid transitions between ideas, evidence, claims, and actions.

PRP applies more rigor when the cost of error rises and less when the task is routine. Reasoning depth and answer length are treated as separate controls, so a short answer can still be produced from high-rigor analysis.

## Who it is for

PRP is intended for people who use general-purpose AI for work where reasoning quality matters, including:

- founders and executives;
- analysts and consultants;
- researchers and scientists;
- product and engineering teams;
- legal, policy, risk, and governance professionals;
- enterprise AI teams;
- educators and students doing analytical work;
- anyone using AI for consequential decisions, synthesis, research, planning, or evaluation.

It is also useful for teams that want a shared reasoning standard without forcing a single output style or domain-specific workflow.

## What problems it addresses

General-purpose language models can produce fluent answers even when the underlying reasoning is weak. Common failure modes include:

- unsupported certainty;
- fabricated facts, citations, or actions;
- hidden assumptions;
- conflating inference with observation;
- treating possibility as probability or probability as actuality;
- confusing correlation with causation;
- scope drift;
- silently changing premises;
- collapsing legitimate alternatives too early;
- applying too much process to trivial work;
- applying too little scrutiny to consequential work;
- mistaking coherence for correctness.

PRP turns these failure modes into explicit reasoning constraints.

## Core benefits

### Adaptive rigor

PRP selects the minimum sufficient reasoning depth for the task. Routine transformations can remain lightweight, while scientific, legal, financial, safety-critical, patent, publication, or high-novelty work can escalate automatically.

### Better epistemic discipline

Material claims are treated according to their evidentiary status: observed, verified, inferred, estimated, hypothetical, speculative, metaphorical, fictional, normative, or unknown.

### Stronger hallucination control

The protocol explicitly prohibits invention of facts, citations, sources, laws, policies, capabilities, tool results, actions, files, messages, people, or verification.

### Clearer assumptions and uncertainty

PRP distinguishes what is known from what is assumed, inferred, estimated, or unresolved. When evidence weakens, confidence should fall rather than rhetoric increasing.

### User agency preservation

The system is instructed to preserve the user's decision space, present tradeoffs honestly, avoid manipulative pressure, and refrain from substituting model judgment for human authority.

### Scope and authority discipline

PRP prevents local preferences, organizational rules, temporary assumptions, or domain-specific constraints from silently becoming universal truths. It also distinguishes expertise, capability, permission, and authorization.

### Proportionality

The protocol is designed to avoid both under-analysis and over-governance. A clerical task should not receive a research memo; a consequential decision should not receive an unexamined guess.

## How adaptive reasoning works

PRP uses five reasoning levels.

| Level | Mode | Typical use |
|---|---|---|
| 0 | Direct Execution | Formatting, extraction, rewriting, deterministic clerical work |
| 1 | Standard Reasoning | Routine analysis, summaries, low-risk planning |
| 2 | Governed Analysis | Strategy, comparison, architecture, multi-source synthesis, ambiguous decisions |
| 3 | High-Rigor Reasoning | Legal, financial, scientific, patent, regulatory, safety-critical, publication work |
| 4 | Research & Architecture | Theory creation, formal research, high-novelty system design, canonical intellectual work |

The protocol escalates based on consequence, ambiguity, evidence dependency, irreversibility, novelty, external exposure, authority implications, and potential harm from error.

## The four core invariants

PRP is anchored by four rules:

1. **Say what is true.** Preserve epistemic integrity and distinguish verified information from inference.
2. **Extract nothing.** Do not manipulate through guilt, fear, dependency, validation pressure, or artificial urgency.
3. **Protect the other party's next move.** Preserve agency, alternatives, and reversibility.
4. **Do not trade truth for fluency, confidence, or completeness.** Prefer partial accuracy to polished fabrication.

A fifth cross-cutting constraint is **scope preservation**: local rules, assumptions, or preferences stay local unless there is evidence and authority to generalize them.

## Claim modes and type discipline

PRP requires material propositions to retain their correct status. An estimate should not become a measurement. A metaphor should not become a literal mechanism. A hypothesis should not become a fact because it is compelling.

The protocol also guards against silent category conversion, including:

- possibility → probability;
- probability → actuality;
- correlation → causation;
- analogy → identity;
- evidence → interpretation;
- prediction → observation;
- simulation → execution;
- confidence → correctness;
- coherence → truth;
- capability → permission.

## What PRP does not do

PRP does **not**:

- alter model weights;
- make a probabilistic model deterministic;
- guarantee factual correctness;
- replace primary-source verification;
- create legal, medical, financial, scientific, or institutional authority;
- expose or require private chain-of-thought;
- turn every interaction into a compliance workflow;
- substitute a model's decision for the user's.

It is an instruction- and Skill-level reasoning discipline. Its purpose is to reduce invalid reasoning paths and make errors easier to detect, not to claim perfect control.

## Repository structure

```text
portable-reasoning-protocol/
├── SKILL.md
├── README.md
├── INSTALLATION.md
├── STACK_INTEGRATION.md
├── CHANGELOG.md
├── agents/
│   └── openai.yaml
├── evaluations/
│   ├── README.md
│   └── cases.yaml
└── references/
    └── prp-core.md
```

`SKILL.md` is intentionally compact. It acts as the runtime control plane. The advanced public protocol lives in `references/prp-core.md` and can be loaded when a task requires deeper rigor.

## Installation

See **[INSTALLATION.md](INSTALLATION.md)** for platform-specific instructions for:

- ChatGPT
- Claude
- Gemini
- GitHub Copilot

The guide distinguishes native Agent Skill installation from compatibility approaches on platforms that use a different customization mechanism.

## Using PRP

Typical requests include:

- `Apply PRP to this decision.`
- `Analyze this using maximum rigor but keep the answer concise.`
- `Use PRP to compare these two architectures.`
- `Separate verified facts, inference, and speculation.`
- `Stress-test this recommendation for hidden assumptions and contradictions.`
- `Treat this as publication-grade analysis.`
- `Give me the decision first, then the evidence and material caveats.`

Where the host supports skill triggering, PRP can also be selected automatically when its description matches the task.

## User controls

PRP separates analysis from presentation. Users can request different combinations such as:

- **Fast + concise** for routine work;
- **Deep + concise** for executive decisions;
- **Maximum + exhaustive** for research or publication;
- **Deep + essential caveats** when time is limited;
- **Standard + explicit assumptions** when transparency matters more than length.

Visible brevity never disables truthfulness, hallucination control, material uncertainty, source integrity, scope integrity, or authority discipline.

## Example: ordinary decision

**Request**

> Compare these two vendors using PRP. Keep it to one page.

**Expected behavior**

PRP should identify the decision objective, distinguish sourced facts from inference, expose material assumptions, compare alternatives against the user's actual criteria, flag missing evidence that could change the decision, and remain concise.

## Example: high-rigor research

**Request**

> Use maximum rigor. Determine whether this evidence supports a causal claim and identify the strongest alternative explanations.

**Expected behavior**

PRP should escalate the task, classify evidence quality, separate observation from interpretation, test causality rather than correlation, preserve competing hypotheses, identify discriminating evidence, and avoid manufacturing certainty.

## Example: creative or hypothetical work

PRP is not designed to suppress imagination. Fictional, hypothetical, metaphorical, visual, and speculative propositions remain admissible when correctly typed within the relevant world model.

A surreal proposition can be valid in fiction while unsupported as a claim about ordinary physical reality. PRP constrains invalid transitions between those contexts; it does not erase the underlying concept.

## Design philosophy

PRP treats reasoning as movement through a constrained possibility space. A reasoning step should remain relevant, evidentially bounded, scope-correct, reconstructable, and consistent with active definitions.

When multiple branches remain admissible, preserve the important alternatives. When a branch becomes unsupported, contradictory, irrelevant, or unauthorized, stop promoting it. When new evidence changes the answer, revise the conclusion rather than rewriting the historical record.

This approach is intended to make model outputs more inspectable and decision-useful without requiring identical wording or rigid procedural ceremony.

## Relationship to enterprise systems

The public PRP Skill operates at the instruction and workflow layer. That makes it useful for individual and team reasoning, experimentation, education, and benchmarking.

Production enterprise systems may require additional mechanisms such as persistent state, policy enforcement, observability, provenance, access control, auditability, runtime interception, and deterministic execution controls. Those capabilities are outside the scope of this Skill.

## Optional Cognous stack integration

PRP remains independently usable and has no mandatory dependency on the Cognous Open Source Stack.

See **[STACK_INTEGRATION.md](STACK_INTEGRATION.md)** for the optional handoff model. It explains how PRP can preserve claim status, uncertainty, competing explanations, source/tool attribution, and action-state distinctions before a downstream authority or runtime system makes its own decision.

The integration note explicitly keeps separate:

- reasoning effort;
- evidence quality;
- institutional consequence;
- authorization state;
- execution status;
- observation status.

Reasoning rigor does not grant permission, and PRP does not authenticate authority or prove that an external effect occurred.

## Versioning

This public package is **PRP v1.0**.

The v1.0 designation marks the first public Skill release. Future changes should distinguish:

- editorial changes;
- implementation changes;
- behavioral changes;
- changes to core invariants.

Behavioral and invariant changes should receive explicit version increments and testing.

## Contributing and testing

Useful contributions include:

- benchmark tasks;
- adversarial examples;
- ambiguity tests;
- hallucination tests;
- evidence-conflict tests;
- authority and scope tests;
- comparisons across model families;
- tests of over-governance versus under-governance;
- examples where PRP changes a conclusion rather than merely changing presentation.

A strong benchmark should test whether the protocol changes reasoning quality, not whether it merely produces more structured prose.

The repository now includes a reproducible **[behavioral evaluation suite](evaluations/README.md)** with canonical cases in **[evaluations/cases.yaml](evaluations/cases.yaml)**. The suite separates substantive decision correction from formatting compliance and requires baseline-versus-PRP runs to record model/version, settings, inputs, outputs, and evaluator provenance.

Behavioral cases are marked **unexecuted** unless an actual model run is recorded. Static/package validation does not establish behavioral effectiveness.

## Important limitation

PRP is an instruction-layer protocol. Model behavior can still vary with model version, tool availability, retrieval results, context, system instructions, decoding behavior, and host-platform constraints.

Use PRP to improve reasoning discipline, not as evidence that an answer is correct merely because PRP was applied.

---

**Portable Reasoning Protocol (PRP) v1.0**  
Developed by **[Cognous](https://cogno.us)**  
Governed reasoning infrastructure for AI systems.
