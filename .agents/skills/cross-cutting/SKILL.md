---
name: cross-cutting
description: /cross-cutting — arc42 §08 enterprise concerns (security, obs, config…).
disable-model-invocation: true
extractBundle: architecture-core
---

# /cross-cutting — Cross-cutting (§08)

## Write

- Path: `architecture/08-cross-cutting/` — topic section or `{topic}.md`
- Template: `.cursor/extracts/tpl-cross-cutting.md`
- Require: Intent + Owner (or TBD) + Approach stub — **no AI waffle**

## Topics (seed)

Security · Logging · Observability · Caching · Messaging · Configuration · Exception · Validation · Localization · Authorization

## Do not

- Full OpenAPI / UI DSL / E2E plans
- Duplicate business journeys (those are `/journey`)

## MCP (optional)

If **hubdocs** connected: `hubdocs_route` for §08 topics · `hubdocs_validate_links` after new section.

Parent: `/architecture`
