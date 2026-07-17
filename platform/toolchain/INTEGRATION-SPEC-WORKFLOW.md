# Integration spec workflow

> **R2/R3:** Product Code + architecture → [`base-docs`](../..) · E2E plans → [`base-tests`](https://github.com/raintr91/base_test) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> SSOT **trong repo integration**. **Không pnpm.**

## 1. Author bundle

Template: `docs/templates/integration-adapter.bundle.yaml` — **`portal-feature-bundle/v1`**.

```text
`base-docs` Product Code (prefer `--id`)
  {function}.bundle.yaml
  ir/spec.yaml · legacy.yaml · design.yaml
  integration/01-integration-spec.yaml   # mirror sau split
  generated/
`docs/features/` (stub only — SSOT on hubs) / md/…                       # ./scripts/docs-render
```

## 2. Split + render

```bash
./scripts/spec-split `base-docs` Product Code (prefer `--id`)
./scripts/docs-render
./scripts/docs-dev            # DocFX :8082
```

Mirror: `integration/01-integration-spec.yaml` (input `integration-gen`).

## 3. Grill + codegen

| Step | Command |
|------|---------|
| Audit keys ↔ fast client | `/grill-integration-spec` |
| Scaffold adapter | `./codegen/runners/generate write --spec …/01-integration-spec.yaml` |
| xUnit | `dotnet test` |
| Live chain | fast `mes_client` → `:4100` |

Hub: [INTEGRATION-ARTIFACT-COMMANDS](./INTEGRATION-ARTIFACT-COMMANDS.md)
