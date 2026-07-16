---
name: containers
description: /containers — arc42 §05 Building blocks; CTR-* views + CMP index links.
disable-model-invocation: true
extractBundle: architecture-core
---

# /containers — Surfaces / building blocks (§05)

**Business layer:** Surfaces (web · client · api)  
**Standards:** prose → **arc42**-lite; diagrams → **C4** `CTR-*`

## Write

- Path: `architecture/05-building-blocks/`
- IDs: `CTR-*` (description + flowchart + Code refs table)
- Prefer naming surfaces: `*-web`, `*-api`, client equivalents — not “tenant” unless multi-tenant is the topic
- CMP: **index/link only** → `product/components/CMP-*` (use `/component` for README)
- Format: MD + Mermaid only

## Do not

- Embed OpenAPI / UI DSL
- Create `code/` under `05`
- Invent containers without lead ID

## Pilot

[`architecture/05-building-blocks/`](architecture/05-building-blocks/) · `CTR-admin-web` · `CTR-admin-api`

Parent router: `/architecture` · CMP skill: `/component` · [Start now](../../../platform/guide/start-now.md)

## MCP (optional)

If **hubdocs** connected: `hubdocs_list_ids` kind `CTR` · `hubdocs_dependents_of`.
