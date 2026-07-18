# Repo split map — Factory AI (4 repo)

> **R2/R3:** Product Code + architecture → [`base-docs`](../..) · E2E plans → [`base-tests`](https://github.com/raintr91/base_test) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> Mỗi runtime repo **sở hữu** spec bundle + ir + codegen + test của mình. Portal chỉ giữ **FE contract** (`ir/spec.yaml` entities) + app layers + E2E.

**Cập nhật:** 2026-07-10

---

## 1. Bốn repo product

| Repo | Path | Tech | Port | Vai trò |
|------|------|------|------|---------|
| **portal** | `<portal-checkout>` | Next.js · pnpm · VitePress | `:3000` | FE `src/` · `contract:gen` · `portal:gen` · E2E |
| **fast-api-base** | `<fast-api-base-checkout>` | FastAPI · Python + shell · MkDocs | `:4000` | API · `./codegen/runners/generate` · pytest (không E2E) |
| **line** | `<line-checkout>` | .NET 8 · DocFX | — | Line client · `./codegen/runners/generate` · xUnit |
| **integration** | `<integration-checkout>` | .NET 8 · DocFX | `:4100` | OT gateway · `./codegen/runners/generate` · xUnit |

Các repo runtime được checkout độc lập; docs hub không resolve chúng bằng sibling path. Repo URLs và policy: [PROJECT-MAPS](./PROJECT-MAPS.md).

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

**Contract keys:** Cùng tên field trên portal `entities` ↔ fast `requests/responses` ↔ line `Line.Contracts` ↔ integration presenter — [CONTRACT-FIELD-REGISTRY](./CONTRACT-FIELD-REGISTRY.md).

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

Line + integration use the same bundle schema owned by Bundlekit.

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
| artifact layout · commands · skills `.cursor/skills/` | **line** → [git](https://github.com/raintr91/winform) |
| artifact layout · commands · skills `.cursor/skills/` | **integration** → [git](https://github.com/raintr91/integration) |
| [FastAPI codegen git](https://github.com/raintr91/fast-api/blob/v3/docs/operational/FAST-CODEGEN.md) · MkDocs `./scripts/docs-dev` · skills | **fast-api-base** |
