---
name: decision
description: /decision — arc42 §09 ADRs (ADR-*); product/system decisions.
disable-model-invocation: true
extractBundle: architecture-core
---

# /decision — ADRs (§09)

## Write

- Path: `architecture/09-decisions/` — `ADR-{NNN}-{slug}.md` + index table
- Template: `.cursor/extracts/tpl-adr.md`
- Link Related: `CMP-*` / `CTR-*` / `FLOW-*` as needed

## Do not

- Put ADRs back under `product/shared/adr` (redirect stub only)
- Move `api-catalog` / `data-model` into §09
- Platform process howto → `platform/` handbook

## Pilot

[ADR-001](architecture/09-decisions/ADR-001-arc42-toc.md)

Parent: `/architecture`

## MCP (optional)

If **hubdocs** connected: `hubdocs_list_ids` kind `ADR` · `hubdocs_validate_links` after new ADR.
