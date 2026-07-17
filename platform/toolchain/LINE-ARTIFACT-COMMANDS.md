# Line artifact — lệnh script

> **R2/R3:** Product Code + architecture → [`base-docs`](../..) · E2E plans → [`base-tests`](https://github.com/raintr91/base_test) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> Chạy trong `<line-checkout>`. **.NET-native** — không pnpm / không Node.
> Spec SSOT: ``docs/features/` (stub only — SSOT on hubs) / yaml/`. Docs site: **DocFX** (`./scripts/docs-dev` `:8081`).

| Lệnh | Mục đích |
|------|----------|
| `./scripts/spec-split <bundle.yaml>` | `portal-feature-bundle/v1` → `ir/{spec,legacy,design}.yaml` |
| `./scripts/spec-split --check <bundle.yaml>` | Verify IR |
| `./scripts/spec-split-all` | Glob mọi `*.bundle.yaml` |
| `./scripts/spec-merge <bundle.yaml>` | `ir/*` → bundle SSOT |
| `./scripts/docs-render` | bundle → ``docs/features/` (stub only — SSOT on hubs) / md/` (LineDocs C#) |
| `./scripts/docs-dev` | DocFX preview `:8081` (thay VitePress) |
| `./scripts/docs-build` | Static site → `_site/` |
| `./codegen/runners/generate registry` | Validate `registries/codegen.registry.json` |
| `./codegen/runners/generate dry --spec …/ir/spec.yaml` | Plan Scriban scaffold |
| `./codegen/runners/generate write --spec …/ir/spec.yaml` | Write `src/Line.App/Generated/` |
| `./scripts/contract-sync --openapi <fast>/backend/02-openapi.yaml` | Keys ↔ `Line.Contracts` |
| `./scripts/smoke-wire.sh` | Curl fast check-in |
| `dotnet test` | xUnit only (thay vitest) |

## Pilot

```bash
./scripts/spec-split `base-docs` Product Code (prefer `--id`)
./scripts/docs-render
./codegen/runners/generate write --spec `base-docs` Product Code (prefer `--id`)
dotnet test
```

Hub portal: [FEATURE-ARTIFACT-COMMANDS](./FEATURE-ARTIFACT-COMMANDS.md)
