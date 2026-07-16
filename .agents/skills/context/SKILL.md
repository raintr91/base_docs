---
name: context
description: /context — arc42 §03 Context; LND-* and CTX-* (MD + Mermaid).
disable-model-invocation: true
extractBundle: architecture-core
---

# /context — Overview / landscape (§03)

**Business layer:** Overview  
**Standards:** prose → **arc42**; diagrams → **C4** (`flowchart`, avoid Mermaid `C4Context`)

## Write

- Path: `architecture/03-context/`
- IDs: `LND-*`, `CTX-*` (D3: landscape lives here)
- Format: MD + Mermaid; prefer `flowchart`
- Template: `tpl-arc42-chapter.md` + pilot sections in `03-context/index.md`
- Keep text short (purpose, actors, boundary) — arc42 spirit, not every chapter

## Do not

- API schemas / UI DSL
- Put LND under `05-building-blocks`
- Duplicate CTR/CMP here

## Pilot

[`architecture/03-context/`](architecture/03-context/) · `LND-base` · `CTX-admin`

Parent router: `/architecture` · People: [Start now](../../../platform/guide/start-now.md)

## MCP (optional)

If **hubdocs** connected: `hubdocs_list_ids` kind `CTX`|`LND` · `hubdocs_route`.
