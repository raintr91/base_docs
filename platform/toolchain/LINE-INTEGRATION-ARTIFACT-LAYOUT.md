# Line + Integration artifact layout

> **R2/R3:** Product Code + architecture → [`base-docs`](../../base-docs/) · E2E plans → [`base-tests`](../../base-tests/) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> **Mỗi repo sở hữu spec riêng.** Portal chỉ giữ FE `ir/spec.yaml` (entities / ui). Không đặt `backend/`, `integration/`, hay line manifests trên portal.

## Feature folder (theo repo)

### portal — FE contract only

```text
`base-docs` Product Code (prefer `--id`)
  *.bundle.yaml              # FE bundle (optional)
  ir/spec.yaml               # entities · ui · testIds — contract:gen input
  generated/
    contract.manifest.json   # contract:gen
```

### fast-api-base — backend API

```text
`base-docs` Product Code (prefer `--id`)
  {function}.bundle.yaml
  ir/spec.yaml
  backend/01-backend-spec.yaml   # mirror — fast:gen input
  backend/02-openapi.yaml
  generated/
```

### line — client screens

```text
`base-docs` Product Code (prefer `--id`)
  {function}.bundle.yaml
  ir/spec.yaml               # clients.line
  generated/
    line.manifest.json
    LINE-HANDOFF.md
```

### integration — OT adapters

```text
`base-docs` Product Code (prefer `--id`)
  {function}.bundle.yaml
  ir/spec.yaml
  integration/01-integration-spec.yaml
  generated/
    integration.manifest.json
    INTEGRATION-HANDOFF.md
```

## Pilot paths

| Concern | Repo | Path |
|---------|------|------|
| Contract keys | portal | `factory/workforce/ir/spec.yaml` |
| FastAPI check-in | fast-api-base | `factory/workforce/` |
| Line kiosk | line | `factory/workforce/` |
| MES downtime | integration | `factory/mes/downtime/` |

## Skills (per repo)

| Repo | Skills path | Spec command |
|------|-------------|--------------|
| line | `~/workspace/line/.cursor/skills/` | `/line-spec` · `/grill-line-spec` |
| integration | `~/workspace/integration/.cursor/skills/` | `/integration-spec` · `/grill-integration-spec` |
| portal router | `.cursor/rules/team-flow-router.mdc` | pointers only |

Operational: `line/docs/operational/LINE-SPEC-WORKFLOW.md` · `integration/docs/operational/INTEGRATION-SPEC-WORKFLOW.md`

## Codegen owners

| Command | Repo |
|---------|------|
| `pnpm contract:gen` | portal |
| `./codegen/runners/generate write` | fast-api-base |
| `./codegen/runners/generate write` | line |
| `./codegen/runners/generate write` | integration |

Hub: [REPO-SPLIT-MAP](./REPO-SPLIT-MAP.md) · [factory-ai-stack](./factory-ai-stack.md)
