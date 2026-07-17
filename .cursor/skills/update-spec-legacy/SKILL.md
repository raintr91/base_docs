---
name: update-spec-legacy
extractBundle: update-spec-legacy
description: /update-spec-legacy — delta from legacy evidence.
disable-model-invocation: true
---

# /update-spec-legacy — Legacy delta patch

**Extracts:** `extractBundle: update-spec-legacy` → `.cursor/extracts/extract-registry.json`

## Load policy

| Load | Do not load |
|------|-------------|
| `_legacy.dynamics.yaml` on **base-docs** — **one slice** for target function | Full module re-archaeology |
| `bundle.legacy` delta | `codegen/*`, `test/*`, prototype |
| Evidence pointer from trace/refs | Legacy repo (unless `#legacy-recheck`) |

## Workflow

1. Receive delta from `/update-spec` or grill gap.
2. Patch trace slice + `bundle.legacy` (behaviors, fields, ui) with confidence.
3. **Micro-read** legacy file/symbol only when tagged `#legacy-recheck`.
4. `bundle_split` + `legacy_dynamics_validate` if trace changed (CLI: `bundlekit split` / `bundlekit legacy-validate`; fallback pnpm scripts).
5. Handoff → `/bqa-grill-docs` or `/dev-grill-docs` per section touched.

## Accelerators (optional)

```text
if CodeGraph available: micro-read symbol evidence for #legacy-recheck
else: targeted file read only

if ArtifactGraph available: parity slice
else: model review from patched legacy evidence
```

## Done

- Delta backed by evidence pointer or explicit `openQuestions`.
- No full bundle replacement unless user confirms scope explosion.
