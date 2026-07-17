# Team AI — line workflow

> **R2/R3:** Product Code + architecture → [`base-docs`](../..) · E2E plans → [`base-tests`](https://github.com/raintr91/base_test) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> Skills + lệnh chạy trong **`<line-checkout>`**. Spec SSOT: ``docs/features/` (stub only — SSOT on hubs) / yaml/`. Không pnpm.

| # | Skill | Output |
|---|-------|--------|
| 1 | `/line-spec` | `{function}.bundle.yaml` → `ir/spec.yaml` (`clients.line`) |
| 2 | `/grill-line-spec` | audit keys ↔ portal entities + fast OpenAPI |
| 3 | `./codegen/runners/generate write` | Generated VM/Service |
| 4 | `/line-prototype` | mock check-in green |
| 5 | `/grill-line-prototype` | AutomationId + VM audit |
| 6 | `/line-wire` | real fast envelope |
| 7 | `/grill-line-api` | contract-sync + smoke-wire |
| 8 | `/line-unit` | xUnit (`dotnet test`) |
| 9 | `/grill-line-unit` | coverage gaps |

Contract keys: portal `ir/spec.yaml` · portal `pnpm contract:gen` (FE only).

Commands: [LINE-ARTIFACT-COMMANDS](./LINE-ARTIFACT-COMMANDS.md)
