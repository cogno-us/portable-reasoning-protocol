# Changelog

## v1.1 — 2026-10-07

### Protocol semantics

- Added an explicit distinction among requested depth, automatic depth, mandatory reasoning floor, and effective depth.
- Clarified that user requests for less rigor cannot reduce reasoning beneath the minimum required for truth, safety, legality, authority, consequence, or material evidentiary quality.
- Added a context and instruction trust boundary for task/session instructions, retrieved material, attachments, quoted text, tool output, and supplied documents.
- Clarified that retrieved or supplied content is evidence or task context, not an active instruction channel merely because it contains imperative language.
- Clarified that task context cannot silently rewrite non-disableable safeguards, lower the mandatory floor, create authority, grant permission, or promote unsupported claim modes.
- Added behavioral regression cases for mandatory-floor preservation and task-context attempts to disable PRP safeguards.
- No runtime enforcement, persistence, provider, identity, authorization, or execution capability is claimed by this release.

### Public control profile 1.0.0 integrated with v1.1

- Preserved the merged v1.1 mandatory-floor and context trust-boundary semantics. The control-profile version is separate from the public protocol version.

- Made proposed, minimum and effective levels explicit, with stable rule IDs, a depth-request mapping, constrained overrides and cumulative required components.
- Kept core safeguards and the routine-task fast path in a compact entrypoint; expanded detail is progressively loaded.
- Restored the source's force for material negative records when context permits and mandatory available verification; blocked checks cannot be reported as completed.
- Added a source hash and a 28-section preservation map. Public v1.0 is a renumbered adaptation of the mature v3.1 source, not an older static-only protocol.
- Identified rule IDs, record shape, numeric depth mapping and offline calculation as new public operationalization, not recovered private application machinery.
- Added a selection-only schema, dependency-free offline calculator, deterministic tests and 16 unexecuted behavioral regression cases.
- Corrected the allocation reference's invalid inline reversibility value; the existing ReasoningPlan v1.0 schema is unchanged.
- Updated README benefits and limits without claiming measured behavioral or compute improvement.
- This is a behavioral instruction/profile revision, not merely formatting. No invariant, licensing term, stack dependency or authority boundary is relaxed.

### Earlier reasoning-allocation proposal

- Added optional provider-neutral ReasoningPlan v1.0, example and informative provider notes.
- Added routing cases and fixed-effort comparisons; model runs remain unexecuted.

### Earlier documentation-only integration batch

- Added optional stack integration, baseline behavioral cases and evaluation rubric.
- Preserved reasoning/evidence/consequence/authorization/execution/observation distinctions.
- That earlier batch did not alter runtime Skill instructions. This control-profile revision does.
