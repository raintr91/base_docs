# Toolchain

Handbook + how-to for Code IR (split/render/validate). **SSOT: this hub** (`base-docs`).

## Bundle IR commands

Run the docs install profile first. These `pnpm` commands are aliases to the
installed **Bundlekit** CLI:

```bash
pnpm spec:split -- product/components/…/code/W-*/….bundle.yaml
pnpm docs:render -- --yaml-root product/components --md-root product/components   # adjust flags as needed
pnpm docs:render:common
pnpm legacy-dynamics:validate -- product/legacy-dynamics/…/_legacy.dynamics.yaml
# direct CLI: bundlekit split|render|legacy-validate …
```

Engines and generated skills are owned by Bundlekit; this repository keeps only
product templates and the thin command aliases in `package.json`.

## Handbook (this folder)

| Doc | Topic |
|-----|-------|
| [Hub split](https://github.com/raintr91/base_test/blob/main/docs/HUBS.md) · [Tests hub handbook](https://github.com/raintr91/base_test/blob/main/docs/TESTS-HUB.md) | Docs/tests/code lane ownership |
| [Toolkits (MCP)](/platform/guide/toolkits) | **Hub** — catalog · install · profiles · ownership · package contract · status |
| [PROJECT-MAPS](./PROJECT-MAPS.md) | platform-repos / workspace |
| [FEATURE-ARTIFACT-FLOWS](./FEATURE-ARTIFACT-FLOWS.md) | Artifact flows |
| [FEATURE-ARTIFACT-COMMANDS](./FEATURE-ARTIFACT-COMMANDS.md) | Commands |
| [FEATURE-ARTIFACT-LEGACY-DYNAMICS](./FEATURE-ARTIFACT-LEGACY-DYNAMICS.md) | Archaeology pointer |

Per-toolkit deep docs live in each toolkit's own git repo (base-docs chỉ giữ
[Toolkits (MCP)](/platform/guide/toolkits) làm hub):
[Hubdocs](https://github.com/raintr91/hubdocs) ·
[Bundlekit](https://github.com/raintr91/Bundlekit) ·
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
