# Anthropic adapter notes

Map PRP's semantic effort requirement to the thinking controls supported by the selected Anthropic model/runtime.

Guidance:

- treat token budgets or thinking modes as provider-specific implementation settings;
- find the smallest setting that reaches the required quality on the target evaluation set;
- avoid spending extended thinking on deterministic clerical work;
- escalate after measurable verification failure where appropriate;
- record model/version, configured budget, observed usage, latency, and substantive outcome.

A PRP level is not a fixed Anthropic thinking-token budget.
