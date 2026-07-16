---
name: journey
description: /journey — product runtime journeys (FLOW-*) under arc42 §06; replaces /dynamics for new work.
disable-model-invocation: true
extractBundle: architecture-core
---

# /journey — Flow (`FLOW-*` / `*_flow`)

**Business layer:** Flow (optional node on the tree)  
**Standards:** 1–2 lines purpose OK (arc42-lite); body diagram → **C4 `sequenceDiagram`**. Skill name stays **`/journey`** — do not say *dynamics* on new docs trees.

## Write

- Path: `architecture/06-runtime/journeys/` — files `FLOW-*.md` (catalog: `06-runtime/index.md`)
- Format: **MD + Mermaid only** — `sequenceDiagram` preferred
- May reference Code IDs (`W-*`, `API-*`, `CTR-*`) on steps/diagram only
- Apply curated criteria (extract `tpl-journey.md` / `architecture-core.md`)
- Place at system (cross-surface) or document under a surface when app-local — still one `FLOW-*` file

## Do not

- Endpoint contracts → `product/components/.../code/API-*` or `shared/api-catalog`
- UI DSL → `code/W-*`
- Full backlog of every story — only ~10–20% core/hard/cross-system
- Confuse with `product/legacy-dynamics/` or `/flow-trace` (legacy)
- Name folders/nav **dynamics** for new work

## Aliases

- `/dynamics` → thin redirect to this skill (deprecated wording)
- `/flow-trace` → legacy extract path only — **not** product `FLOW-*`

## MCP (optional)

If **hubdocs** connected: `hubdocs_journeys`, `hubdocs_deps_of`, `hubdocs_orphans` before adding a journey.

Pilot: [`FLOW-login`](architecture/06-runtime/journeys/FLOW-login.md) · [Start now](../../../platform/guide/start-now.md)
