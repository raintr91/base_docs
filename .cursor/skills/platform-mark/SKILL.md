---
name: platform-mark
extractBundle: platform-mark
description: /platform-mark — member marks tags/registries after grill confirm.
disable-model-invocation: true
---

# /platform-mark

Member annotation sau grill A/B/C — **không** bulk `/spec` / `/dev-grill-docs`.

**Hub policy:** `platform/toolchain/PLATFORM-MARK.md`
Technical marks SSOT: `product/shared/integrations/*`, `product/shared/data-model/derived-data.md`

## Registries (code)

| Layer | File | Tags |
|-------|------|------|
| UI | `registries/design.registry.json` | `#needs-component:` `#needs-ui:` `#shell:` |
| Logic | `registries/common.registry.json` | `#common:*` `#needs-common:*` |

Executable registry validation is **FE Codegenkit** (or product scripts on the
FE checkout). On docs hub:

```text
if ArtifactGraph available:
  artifactgraph_allowlist_check(registryValidate|commonRegistry)
  artifactgraph_recommend_command → hand off to FE
else:
  note pending FE registry validate; do not invent local shell fallbacks
```

## Workflow (ngắn)

1. Feature `ir/spec.yaml` + registries (optional `artifactgraph_analyze`)
2. Một mark / concern; member đã confirm ở grill
3. Upsert registry · planned → HANDOFF · implemented → promote path
4. `artifactgraph_remember` subject sau confirm B

## Do not

- Auto-tag không hỏi member  
- Mo* vào `common.registry` (chỉ design registry)  
- Full contract rewrite  
- Treat `artifactgraph_gen` as required (deprecated shim)

## Handoff

FE Codegenkit / product: `portal:gen:dry --id …` after marks change, when that
lane is available. Missing Codegenkit is a pending handoff, not a docs failure.
