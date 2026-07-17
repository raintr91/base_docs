# Integration artifact — lệnh script

> **R2/R3:** Product Code + architecture → [`base-docs`](../..) · E2E plans → [`base-tests`](https://github.com/raintr91/base_test) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> Chạy trong `<integration-checkout>`. **.NET-native** — không pnpm / không Node.
> Spec SSOT: ``docs/features/` (stub only — SSOT on hubs) / yaml/`. Docs site: **DocFX** (`./scripts/docs-dev` `:8082`).

| Lệnh | Mục đích |
|------|----------|
| `./scripts/spec-split <bundle.yaml>` | bundle → `ir/*` + `integration/01-integration-spec.yaml` |
| `./scripts/spec-split --check <bundle.yaml>` | Verify IR |
| `./scripts/spec-split-all` | Glob mọi `*.bundle.yaml` |
| `./scripts/spec-merge <bundle.yaml>` | `ir/*` → bundle SSOT |
| `./scripts/docs-render` | bundle → ``docs/features/` (stub only — SSOT on hubs) / md/` (IntegrationDocs C#) |
| `./scripts/docs-dev` | DocFX preview `:8082` (thay VitePress) |
| `./scripts/docs-build` | Static site → `_site/` |
| `./codegen/runners/generate registry` | Validate registry |
| `./codegen/runners/generate dry --spec …/01-integration-spec.yaml` | Plan Scriban |
| `./codegen/runners/generate write --spec …/01-integration-spec.yaml` | Write `src/Integration.*/Generated/` |
| `dotnet test` | xUnit only (thay vitest) |

## Pilot

```bash
./scripts/spec-split `base-docs` Product Code (prefer `--id`)
./scripts/docs-render
./codegen/runners/generate write --spec `base-docs` Product Code (prefer `--id`)
dotnet test
```

Fast chain: `<fast-api-base-checkout>` · `pytest tests/test_mes_integration_chain.py`

Hub portal: [FEATURE-ARTIFACT-COMMANDS](./FEATURE-ARTIFACT-COMMANDS.md)
