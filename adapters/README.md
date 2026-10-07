# Provider Adapter Guidance

PRP v1.0 is provider-neutral. Provider adapters translate a semantic [ReasoningPlan](../schemas/reasoning-plan.schema.json) into controls exposed by a specific model/runtime.

These mappings are **informative**, not normative.

## Rules

1. Keep PRP levels independent from provider model names.
2. Do not encode current pricing or model availability into the PRP protocol.
3. Do not assume a fixed token count for a PRP level.
4. Benchmark mappings on the intended workload and model snapshot.
5. Prefer the smallest effort setting that preserves the required substantive quality.
6. Escalate on measurable failure where practical.
7. Record model/version, settings, latency, token usage, and outcome in evaluations.
8. Treat provider capabilities as implementation details, not PRP guarantees.

## Adapter contract

An adapter may accept:

- a `ReasoningPlan`;
- current provider/model capability metadata;
- deployment policy;
- latency/cost ceilings.

It may return:

- provider model selection;
- provider-specific effort/budget parameter;
- verification configuration;
- escalation policy.

It must not convert the plan into authorization or claim that an action occurred.

## Current provider notes

See:

- [OpenAI](openai.md)
- [Anthropic](anthropic.md)
- [Gemini](gemini.md)

These files intentionally avoid pinning exact product availability or prices. Revalidate provider controls before deployment.
