# Artifact layout — yaml / md / generated

> **R2/R3:** Product Code + architecture → [`base-docs`](../../base-docs/) · E2E plans → [`base-tests`](../../base-tests/) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> Một diagram · [FEATURE-ARTIFACT-FLOWS](./FEATURE-ARTIFACT-FLOWS.md)

```mermaid
flowchart TB
  subgraph yaml["`base-docs` Product Code (prefer `--id`)"]
    TRACE["product/legacy-dynamics/…/_legacy.dynamics.yaml"]
    subgraph fn["{function}/"]
      BUNDLE["{id}.bundle.yaml\nSSOT"]
      GEN["gen: optional\ncodegen/tags"]
      IR["ir/spec.yaml\nir/legacy.yaml\nir/design.yaml"]
      TEST["{id}.test.yaml"]
      GENOUT["generated/\nHANDOFF · manifests"]
    end
  end
  subgraph md["base-docs product md/"]
    MD["{id}.md + testcases/"]
  end
  BUNDLE -->|pnpm spec:split| IR
  BUNDLE -->|pnpm docs:render| MD
  IR -->|pnpm portal:gen| GENOUT
```

## Quy tắc path

| Path | Vai trò |
|------|---------|
| `base-docs/product/…/code/` (+ `--id`) | Feature specs — `portal:gen` / `docs:render` |
| `base-docs/product/legacy-dynamics/` | Module `_legacy.dynamics.yaml` (archaeology SSOT) |
| `docs/common/yaml/{function}/` | **Shared/common** component specs (dùng lại, ít thay đổi) — tách khỏi features, lệnh riêng |
| `*.bundle.yaml` | SSOT authoring — `spec`, `design`, `legacy`, `review` |
| `bundle.gen` | Dev-grill / portal:gen fields (tách khỏi design v1) |
| `ir/spec.yaml` | **Duy nhất** input `portal:gen` |
| `ir/legacy.yaml` · `ir/design.yaml` | Grill load — không portal:gen |
| `{function}/generated/` | HANDOFF, codegen/unit manifest — **cạnh bundle**, không trong `ir/` |
| `product/…/md/…` | BA review — derived từ bundle |

> **Common tách riêng features:** feature codegen quét `base-docs` Product Code. Common có lệnh riêng (`*::common`, `phase:common`) vì shared, ít đổi nhưng đổi là ảnh hưởng toàn dự án.

Pattern CRUD: `yaml/_patterns/admin-crud.pattern.yaml`
