---
name: artifactgraph
extractBundle: artifactgraph
description: /artifactgraph — local-first MCP gen/grill; setup on hub.
disable-model-invocation: true
---

# /artifactgraph

Package: [raintr91/artifactgraph](https://github.com/raintr91/artifactgraph)

**Setup / bootstrap:** `base-docs/platform/toolchain/ARTIFACTGRAPH.md` · INTERNALS · package `docs/INIT.md`  
**Rule:** `artifactgraph.mdc` (opt-in) · hooks: `artifactgraph-phase-hooks.md`

## Local-first

```text
rebuild(index) → analyze|grill|parity (LOCAL A/B/C)
  → artifactgraph_gen allowlist (docs/fe/unit/e2e)
  → cloudPromptSlice ONLY if #needs-* still missing
  → promote registry in product repo → rebuild + remember
```

| Local | Không cloud |
|-------|-------------|
| Match shell/common/unit/e2e từ index | “Common hay feature-only?” |
| `specSplit` / `docsRender` / `gen` / `unitGen` / `testcaseGen` | Dump full registry |
| Confirm / parity-drift A/B/C | Gen cả page vì thiếu 1 slot |
| Wire Mo* đã có registry | Viết registry từ cloud |

## Tools

`analyze` · `gaps` · `grill_check` · `parity_check` · `gen` · `remember` · `rebuild` · `status`

Gen = MCP allowlist hoặc `pnpm portal:gen` / `unit-gen` / `testcase:gen` — **không** bịa argv.
