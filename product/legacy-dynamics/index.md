# Legacy dynamics (archaeology)

Observed sequences / collaboration from legacy systems — **`_legacy.dynamics.yaml`**.

**Not** product journeys (`FLOW-*` under [`architecture/06-runtime/`](/architecture/06-runtime/)).

| Artifact | Path |
|----------|------|
| Module dynamics | `product/legacy-dynamics/{module}/_legacy.dynamics.yaml` |
| Template | [`_template/_legacy.dynamics.yaml`](./_template/_legacy.dynamics.yaml) |
| How-to | [`https://github.com/raintr91/Bundlekit/blob/main/docs/LEGACY-DYNAMICS.md`](../../https://github.com/raintr91/Bundlekit/blob/main/docs/LEGACY-DYNAMICS.md) |

| vs | Path | Skill |
|----|------|-------|
| Product journey | `architecture/06-runtime/journeys/` `FLOW-*` | `/journey` |
| Legacy dynamics | `product/legacy-dynamics/` | `/legacy-spec` |

```bash
pnpm legacy-dynamics:validate -- product/legacy-dynamics/.../_legacy.dynamics.yaml
```
