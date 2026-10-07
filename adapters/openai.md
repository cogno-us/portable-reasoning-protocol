# OpenAI adapter notes

Map PRP's semantic effort requirement to the reasoning controls supported by the selected OpenAI model/runtime.

Guidance:

- keep provider-specific reasoning effort outside the PRP core protocol;
- use lower effort for routine tasks when evaluation supports it;
- increase effort for materially ambiguous, consequential, or multi-step tasks;
- measure reasoning-token usage, latency, and substantive quality where the API exposes them;
- do not assume that a current effort label or model name will remain stable across releases.

A PRP level is not an OpenAI API parameter. The adapter owns that mapping.
