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

## v1.0

### Documentation and evaluation

- Added an optional Cognous stack integration note while preserving PRP's standalone operation.
- Added reproducible behavioral evaluation cases and a scoring protocol.
- Clarified separation among reasoning effort, evidence quality, institutional consequence, authorization, execution, and observation.
- No behavioral model evaluations are reported as executed by this change.
