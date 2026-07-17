# Line codegen (Scriban)

> **R2/R3:** Product Code + architecture → [`base-docs`](../..) · E2E plans → [`base-tests`](https://github.com/raintr91/base_test) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> **.NET-native** — `./codegen/runners/generate` + `tools/LineDocs`. Không pnpm.

## Commands

```bash
cd <line-checkout>

./scripts/spec-split `base-docs` Product Code (prefer `--id`)
./scripts/docs-render
./scripts/docs-dev          # DocFX :8081

./codegen/runners/generate dry --spec `base-docs` Product Code (prefer `--id`)
./codegen/runners/generate write --spec `base-docs` Product Code (prefer `--id`)
dotnet test
```

Hub: [LINE-ARTIFACT-COMMANDS](./LINE-ARTIFACT-COMMANDS.md)
