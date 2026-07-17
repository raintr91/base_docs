# Repo split map — Factory AI (4 repo)

> **R2/R3:** Product Code + architecture → [`base-docs`](../../base-docs/) · E2E plans → [`base-tests`](../../base-tests/) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> Mỗi runtime repo **sở hữu** spec bundle + ir + codegen + test của mình. Portal chỉ giữ **FE contract** (`ir/spec.yaml` entities) + app layers + E2E.

**Cập nhật:** 2026-07-10

---

## 1. Bốn repo product

| Repo | Path | Tech | Port | Vai trò |
|------|------|------|------|---------|
| **portal** | `~/workspace/portal` | Next.js · pnpm · VitePress | `:3000` | FE `src/` · `contract:gen` · `portal:gen` · E2E |
| **fast-api-base** | `~/workspace/fast-api-base` | FastAPI · Python + shell · MkDocs | `:4000` | API · `./codegen/runners/generate` · pytest (không E2E) |
| **line** | `~/workspace/line` | .NET 8 · DocFX | — | Line client · `./codegen/runners/generate` · xUnit |
| **integration** | `~/workspace/integration` | .NET 8 · DocFX | `:4100` | OT gateway · `./codegen/runners/generate` · xUnit |

Config: root [`platform-repos.json`](../../platform-repos.json) → group `factory-ai-stack`. Templates: `platform-repos.example.json`. Hub: [PROJECT-MAPS](./PROJECT-MAPS.md).

---

## 2. Ai sở hữu artifact gì

| Artifact | Owner | Path |
|----------|-------|------|
| FE bundle + `ir/spec.yaml` (entities, ui) | **portal** | `portal/`base-docs` / `--id`` |
| `@portal/models` (Zod) | **portal** | `packages/models/` · `pnpm contract:gen` |
| Next app + E2E | **portal** | `src/` · `tests/e2e/` |
| Backend bundle + `ir/spec.yaml` | **fast-api-base** | `fast/`base-docs` Product Code (prefer `--id`)` |
| `backend/01-backend-spec.yaml` | **fast-api-base** | mirror từ `spec:split` |
| `backend/02-openapi.yaml` | **fast-api-base** | `./codegen/runners/generate openapi` |
| Fast modules + pytest | **fast-api-base** | `src/app/modules/` |
| Line bundle + `clients.line` | **line** | `line/`base-docs` / `--id`` |
| Line generated C# | **line** | `src/Line.App/Generated/` |
| Integration bundle + adapter spec | **integration** | `integration/`base-docs` Product Code (prefer `--id`)` |
| Integration generated C# | **integration** | `src/Integration.*/Generated/` |

**Không đặt trên portal:** `backend/`, `integration/`, line/integration manifests, OpenAPI export.

**Contract keys:** Cùng tên field trên portal `entities` ↔ fast `requests/responses` ↔ line `Line.Contracts` ↔ integration presenter — [portal-contract-naming](../../.cursor/rules/portal-contract-naming.mdc).

---

## 3. Feature folder (mỗi repo)

```text
`base-docs` Product Code (prefer `--id`)
  {function}.bundle.yaml     # portal-feature-bundle/v1
  ir/spec.yaml               # pnpm spec:split
  ir/legacy.yaml
  ir/design.yaml
  generated/
  md/                        # pnpm docs:render
```

Line + integration: **cùng bundle schema** với portal (`scripts/spec/lib/bundle-ir.mjs`).

---

## 4. Lệnh theo repo

### portal

```bash
pnpm spec:split -- <base-docs …/bundle.yaml>
pnpm contract:gen --spec `base-docs` / `--id`
pnpm portal:gen --id W-AD-AUTH-001
pnpm test:e2e
```

### fast-api-base

```bash
./scripts/spec-split `base-docs` Product Code (prefer `--id`)
./codegen/runners/generate write --spec `base-docs` Product Code (prefer `--id`)
./codegen/runners/generate openapi --spec `base-docs` Product Code (prefer `--id`)
make test
```

> **Không pnpm** — codegen Python (`codegen/runners/fast_gen`); spec split Python (`tools/fast_spec`).

### line

```bash
./scripts/spec-split `base-docs` Product Code (prefer `--id`)
./codegen/runners/generate write --spec `base-docs` Product Code (prefer `--id`)
./scripts/docs-dev          # DocFX :8081
dotnet test
```

> **Không pnpm** — LineDocs + LineGen (C#) · DocFX · xUnit.

### integration

```bash
./scripts/spec-split `base-docs` Product Code (prefer `--id`)
./codegen/runners/generate write --spec `base-docs` Product Code (prefer `--id`)
./scripts/docs-dev          # DocFX :8082
dotnet test
```

> **Không pnpm** — IntegrationDocs + IntegrationGen (C#) · DocFX · xUnit.
---

## 5. Liên kết

| Doc | Repo |
|-----|------|
| [FEATURE-ARTIFACT-COMMANDS](./FEATURE-ARTIFACT-COMMANDS.md) | portal (hub) |
| [LINE-INTEGRATION-ARTIFACT-LAYOUT](./LINE-INTEGRATION-ARTIFACT-LAYOUT.md) | portal |
| `LINE-ARTIFACT-COMMANDS.md` · skills `.cursor/skills/` | **line** |
| `INTEGRATION-ARTIFACT-COMMANDS.md` · skills `.cursor/skills/` | **integration** |
| `FAST-CODEGEN.md` · MkDocs `./scripts/docs-dev` · skills | **fast-api-base** |
