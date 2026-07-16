# Team AI — integration workflow

> Skills + lệnh trong **`~/workspace/integration`**. Không pnpm.

| # | Skill | Output |
|---|-------|--------|
| 1 | `/integration-spec` | `{function}.bundle.yaml` → `integration/01-integration-spec.yaml` |
| 2 | `/grill-integration-spec` | keys ↔ fast `mes_client` expect |
| 3 | `./codegen/runners/generate write` | Generated adapter layers |
| 4 | `/integration-code` | manual follow-up + DI |
| 5 | `/integration-unit` | xUnit (`dotnet test`) |
| 6 | Wire fast | `MES_BASE_URL=http://127.0.0.1:4100` |
| 7 | `/grill-integration` | mes_client chain audit |

Commands: [INTEGRATION-ARTIFACT-COMMANDS](./INTEGRATION-ARTIFACT-COMMANDS.md)
