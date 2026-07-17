# Legacy dynamics module file

**Path (SSOT):** `product/legacy-dynamics/{module}/_legacy.dynamics.yaml`

Template: `product/legacy-dynamics/_template/_legacy.dynamics.yaml`
How-to: `platform/toolchain/legacy-dynamics.md`

Schema: `portal-legacy-dynamics/v1`

- `index` — functionId → slice metadata
- `slices` — observed facts per child function
- `refs` — `legacy://` URI map
- Evidence: pointer only (`legacy/evidence.md`)

Per-function `ir/legacy.yaml` uses `legacyRef: { module, function, slice }` when dynamics file exists.

**Not** product journeys `FLOW-*` (`architecture/06-runtime/journeys/` · `/journey`).

## Cross-repo paths

- `legacy.repo` = slug `projects.*.repo` trong platform-repos
- `evidence.file` / `refs.*.file` = path **relative** legacy project root
- `refs` keys: `legacy://{entity}/{action}`

## Stale dynamics

Legacy commit đổi → **không** auto re-mine. Trigger: `#legacy-recheck` → `/update-spec-legacy` → patch on **base-docs** + `bundle.legacy` → `spec:split` + `legacy-dynamics:validate`.
