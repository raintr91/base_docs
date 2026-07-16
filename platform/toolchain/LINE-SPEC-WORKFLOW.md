# Line spec workflow

> **R2/R3:** Product Code + architecture → [`base-docs`](../../base-docs/) · E2E plans → [`base-tests`](../../base-tests/) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> Đối xứng portal `/spec` — nhưng SSOT nằm **trong repo line**. **Không pnpm.**

## 1. Author bundle

Template: `docs/templates/line-client.bundle.yaml` — **`portal-feature-bundle/v1`**.

```text
`base-docs` Product Code (prefer `--id`)
  {function}.bundle.yaml
  ir/spec.yaml · legacy.yaml · design.yaml
  generated/
`docs/features/` (stub only — SSOT on hubs) / md/…            # ./scripts/docs-render
```

`contractRef.portalIrSpec` — audit keys vs portal entities.

## 2. Split + render

```bash
./scripts/spec-split `base-docs` Product Code (prefer `--id`)
./scripts/spec-split --check `base-docs` Product Code (prefer `--id`)
./scripts/docs-render
./scripts/docs-dev            # DocFX :8081
```

## 3. Grill + codegen (Scriban)

| Step | Command |
|------|---------|
| Audit keys ↔ fast OpenAPI | `/grill-line-spec` |
| Scaffold screen | `./codegen/runners/generate write --spec …/ir/spec.yaml` |
| Mock lane | `/line-prototype` |
| Wire fast | `/line-wire` |
| xUnit | `/line-unit` → `dotnet test` |

## 4. Không làm trên portal

- Không author `clients.line` trong portal `ir/spec.yaml`
- Không đặt `line.manifest.json` trên portal

Hub: [LINE-ARTIFACT-COMMANDS](./LINE-ARTIFACT-COMMANDS.md)
