# Fast artifact — lệnh script

> **R2/R3:** Product Code + architecture → [`base-docs`](../..) · E2E plans → [`base-tests`](https://github.com/raintr91/base_test) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> Chạy trong `<fast-api-base-checkout>`. **Python + shell** — không pnpm / không Node / không E2E.

| Lệnh | Mục đích |
|------|----------|
| `./scripts/spec-split <bundle.yaml>` | `portal-feature-bundle/v1` → `ir/*` + `backend/01-backend-spec.yaml` |
| `./scripts/spec-split --check <bundle.yaml>` | Verify IR |
| `./scripts/spec-split-all` | Glob mọi `*.bundle.yaml` |
| `./scripts/spec-merge <bundle.yaml>` | `ir/*` → bundle SSOT |
| `./scripts/docs-render` | bundle → ``docs/features/` (stub only — SSOT on hubs) / md/` |
| `./scripts/docs-dev` | MkDocs Material preview `:8001` (thay VitePress) |
| `./scripts/docs-build` | Static site → `site/` |
| `./codegen/runners/generate registry` | Validate `registries/codegen.registry.json` |
| `./codegen/runners/generate dry --spec …/backend/01-backend-spec.yaml` | Plan scaffold |
| `./codegen/runners/generate write --spec …` | Write `src/app/modules/...` |
| `./codegen/runners/generate openapi --spec …` | Export `backend/02-openapi.yaml` |
| `./unitgen/runners/generate write --spec …` | pytest scaffold |
| `./registries/validate-common validate` | Validate `registries/common.registry.json` |
| `./registries/validate-common show` | Print common registry |
| `make test` / `.venv/bin/pytest` | API + yaml contract — **không Playwright** |

## Docs preview

```bash
./scripts/docs-render && ./scripts/docs-dev
# mở http://localhost:8001
```

## Pilot

```bash
./scripts/spec-split `base-docs` Product Code (prefer `--id`)
./codegen/runners/generate write --spec `base-docs` Product Code (prefer `--id`)
make test
```

Portal hub: [FEATURE-ARTIFACT-COMMANDS](./FEATURE-ARTIFACT-COMMANDS.md)
