# Toolchain

Handbook + how-to for Code IR (split/render/validate). **SSOT: this hub** (`base-docs`).

> **R2/R3 hub layout:** Product Code + architecture → [`base-docs`](../..) · E2E plans → [`base-tests`](https://github.com/raintr91/base_test) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [Hub split](https://github.com/raintr91/base_test/blob/main/docs/HUBS.md) · [Docs hub](https://github.com/raintr91/base_docs) · [Tests hub](https://github.com/raintr91/base_test/blob/main/docs/TESTS-HUB.md).

## Bundle IR commands

Run the docs install profile first. These `pnpm` commands are aliases to the
installed **Docskit** CLI:

```bash
pnpm spec:split -- product/components/…/code/W-*/….bundle.yaml
pnpm docs:render -- --yaml-root product/components --md-root product/components   # adjust flags as needed
pnpm docs:render:common
pnpm legacy-dynamics:validate -- product/legacy-dynamics/…/_legacy.dynamics.yaml
# direct CLI: docskit split|render|legacy-validate …
```

Engines and generated skills are owned by Docskit; this repository keeps only
product templates and the thin command aliases in `package.json`.

## Handbook (this folder)

| Doc | Topic |
|-----|-------|
| [Hub split](https://github.com/raintr91/base_test/blob/main/docs/HUBS.md) · [Tests hub handbook](https://github.com/raintr91/base_test/blob/main/docs/TESTS-HUB.md) | Docs/tests/code lane ownership |
| [Toolkits (MCP)](/platform/guide/toolkits) | **Hub** — catalog · install · profiles · ownership · package contract · status |
| [PROJECT-MAPS](./PROJECT-MAPS.md) | platform-repos / workspace |
| [FEATURE-ARTIFACT-COMMANDS](./FEATURE-ARTIFACT-COMMANDS.md) | Commands |
| [FEATURE-ARTIFACT-LEGACY-DYNAMICS](./FEATURE-ARTIFACT-LEGACY-DYNAMICS.md) | Archaeology pointer |

## Feature artifact flows

Mỗi file một concern, một Mermaid ngắn — không gộp toàn pipeline vào một diagram.
Overview màu: [FULL-CYCLE-PIPELINE-DIAGRAM](./FULL-CYCLE-PIPELINE-DIAGRAM.md) · Design + Architecture gate: [DESIGN-PHASE-DIAGRAM](./DESIGN-PHASE-DIAGRAM.md).

### Layout & IR

| Doc | Nội dung |
|-----|----------|
| [FEATURE-ARTIFACT-LAYOUT](./FEATURE-ARTIFACT-LAYOUT.md) | Cây thư mục `yaml/` · `md/` · `ir/` · `generated/` |
| [CODEGEN-LAYOUT](https://github.com/raintr91/codegenkit/blob/main/docs/CODEGEN-LAYOUT.md) | Global `codegen/` · `unitgen/` · `registries/` (platform-bases) |
| [CUSTOMIZE-TEMPLATES](https://github.com/raintr91/codegenkit/blob/main/docs/CUSTOMIZE-TEMPLATES.md) | Hướng dẫn tùy chỉnh Templates và Rules (Ghi đè, Override, Extend) |
| [ArtifactGraph (git)](https://github.com/raintr91/artifactgraph) | Local MCP gaps/tags/gen allowlist |
| [FEATURE-ARTIFACT-BUNDLE-IR](./FEATURE-ARTIFACT-BUNDLE-IR.md) | SSOT bundle → split/merge · `spec` vs `gen` |

### Team commands (AI)

| Doc | Nội dung |
|-----|----------|
| [FEATURE-ARTIFACT-LEGACY-DYNAMICS](./FEATURE-ARTIFACT-LEGACY-DYNAMICS.md) | `/legacy-spec` → trace + bundle.legacy |
| [FEATURE-ARTIFACT-GRILL](./FEATURE-ARTIFACT-GRILL.md) | `/bqa-grill-docs` → `/dev-grill-docs` → `/grill-with-docs` |
| [DESIGN-PHASE-DIAGRAM](./DESIGN-PHASE-DIAGRAM.md) | Design lane đến `/prototype` (+ Phase 0 Architecture gate) |
| [FEATURE-ARTIFACT-COMMANDS](./FEATURE-ARTIFACT-COMMANDS.md) | Lệnh `pnpm portal:*`, `spec:*`, `docs:render` |

### Pipeline theo phase

| Doc | Nội dung |
|-----|----------|
| [FULL-CYCLE-PIPELINE-DIAGRAM](./FULL-CYCLE-PIPELINE-DIAGRAM.md) | Overview màu Phase 0…4 |
| [TEST-PHASE-DIAGRAM](./TEST-PHASE-DIAGRAM.md) | E2E · `testcase:gen` |
| [UNIT-PHASE-DIAGRAM](./UNIT-PHASE-DIAGRAM.md) | Vitest · `portal:unit-gen` |
| [NEEDS-COMPONENT-FLOW](./NEEDS-COMPONENT-FLOW.md) | `#needs-component` gap loop |
| [NEEDS-TEST-FLOW](./NEEDS-TEST-FLOW.md) | needs-test gap loop |
| [NEEDS-UNIT-FLOW](./NEEDS-UNIT-FLOW.md) | `#needs-unit-test` gap loop |
| [BACKEND-PHASE-DIAGRAM](./BACKEND-PHASE-DIAGRAM.md) | API repo |
| [WIRE-PHASE-DIAGRAM](./WIRE-PHASE-DIAGRAM.md) | Integration |
| [UPDATE-SPEC-FLOW](./UPDATE-SPEC-FLOW.md) | Gap loop |

Per-toolkit deep docs live in each toolkit's own git repo (base-docs chỉ giữ
[Toolkits (MCP)](/platform/guide/toolkits) làm hub):
[Docskit](https://github.com/raintr91/docskit) ·
[Processkit](https://github.com/raintr91/Processkit) ·
[Codegenkit](https://github.com/raintr91/codegenkit) ·
[Testkit](https://github.com/raintr91/Testkit) ·
[ArtifactGraph](https://github.com/raintr91/artifactgraph) ·
[Platform DNA](https://github.com/raintr91/platform-dna) ·
[CodeGraph](https://github.com/colbymchenry/codegraph).

### Stack bases (moved from code repos R2 sync)

| Doc | Base |
|-----|------|
| [Portal codegen git](https://github.com/raintr91/nuxt_4/blob/nuxt_v_3/docs/operational/PORTAL-CODEGEN.md) · [Portal unit-gen roadmap](https://github.com/raintr91/nuxt_4/blob/nuxt_v_3/docs/operational/PORTAL-UNIT-GEN-ROADMAP.md) | `portal` reference; duplicated to `nextjs`, `next_nest`, `nuxt_nest` |
| [FastAPI quickstart git](https://github.com/raintr91/fast-api/blob/v3/docs/operational/FAST-API-QUICKSTART.md) · [FastAPI codegen git](https://github.com/raintr91/fast-api/blob/v3/docs/operational/FAST-CODEGEN.md) | `fast-api-base` |
| [Laravel API quickstart git](https://github.com/raintr91/lara12/blob/v3/docs/operational/BACKEND-API-QUICKSTART.md) · [Laravel API spec guide](https://github.com/raintr91/lara12/blob/v3/docs/operational/BACKEND_API_SPEC_GUIDE.md) | `api` reference |
| [Nest API structure git](https://github.com/raintr91/next_nest/blob/next_nest_v3/docs/operational/NEST-API-STRUCTURE.md) · [Nest codegen git](https://github.com/raintr91/next_nest/blob/next_nest_v3/docs/operational/BACKEND-CODEGEN.md) | `next_nest` reference; duplicated to `nuxt_nest` |
| [Laravel backend codegen git](https://github.com/raintr91/lara12/blob/v3/docs/operational/BACKEND-CODEGEN.md) | `api` reference |
| [REPO-SPLIT-MAP](./REPO-SPLIT-MAP.md) · [CONTRACT-PORTAL-FAST](./CONTRACT-PORTAL-FAST.md) | cross-stack |

`integration` và `line` không còn tài liệu trong docs hub — mỗi repo tự giữ
handbook/skill của mình. Xem git: [integration](https://github.com/raintr91/integration) ·
[line](https://github.com/raintr91/winform).

Templates: `templates/api/` · `templates/clients/`.  
Schemas: `schemas/backend-api.schema.json`.

Full list: browse this directory. FE/BE **codegen runners** stay in code repos (`portal:gen`, etc.).
