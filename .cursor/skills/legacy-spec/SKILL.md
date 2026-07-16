---
name: legacy-spec
extractBundle: legacy-spec
description: /legacy-spec — legacy-dynamics on base-docs + Code bundles.
disable-model-invocation: true
---

# /legacy-spec — Legacy dynamics IR (archaeology 1 lần / module)

**Extracts:** `extractBundle: legacy-spec`

**SSOT docs hub:** `base-docs/product/legacy-dynamics/` · how-to `base-docs/platform/toolchain/legacy-dynamics.md`  
Template: `base-docs/product/legacy-dynamics/_template/_legacy.dynamics.yaml`

## Load policy

| Load | Do not load |
|------|-------------|
| Legacy source (minimal); `legacy/project-config.md` progressive | Writing under FE `docs/` |
| Write `base-docs/product/legacy-dynamics/{module}/_legacy.dynamics.yaml` + Code `*.bundle.yaml` | Full `platform-repos.json` dump |
| `legacy/evidence.md` — pointer only | Full repo scan |

## Workflow

1. Compact inventory: routes → controller → service → view.
2. Write/update **`base-docs/product/legacy-dynamics/{module}/_legacy.dynamics.yaml`** (`portal-legacy-dynamics/v1`).
3. Per function: Code under `base-docs/product/components/…/code/` (`*.bundle.yaml`, `specOrigin: legacy`).
4. Parity + context-orphan per `legacy/parity.md`.
5. **Không** `gen` / codegen tags on archaeology turn.
6. `pnpm legacy-dynamics:validate -- ../base-docs/product/legacy-dynamics/.../_legacy.dynamics.yaml` (from FE).
7. Handoff → `/bqa-grill-docs`.

Hub: [legacy-dynamics toolchain](../../base-docs/platform/toolchain/legacy-dynamics.md).
