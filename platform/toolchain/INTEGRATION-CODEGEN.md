# Integration codegen (Scriban)

> **R2/R3:** Product Code + architecture → [`base-docs`](../../base-docs/) · E2E plans → [`base-tests`](../../base-tests/) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> **.NET-native** — `./codegen/runners/generate` + `tools/IntegrationDocs`. Không pnpm.

## Commands

```bash
cd ~/workspace/integration

./scripts/spec-split `base-docs` Product Code (prefer `--id`)
./scripts/docs-render
./scripts/docs-dev          # DocFX :8082

./codegen/runners/generate dry --spec `base-docs` Product Code (prefer `--id`)
./codegen/runners/generate write --spec `base-docs` Product Code (prefer `--id`)
dotnet test
```

Hub: [INTEGRATION-ARTIFACT-COMMANDS](./INTEGRATION-ARTIFACT-COMMANDS.md)
