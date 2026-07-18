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
| [PROJECT-MAPS](./PROJECT-MAPS.md) | platform-repos / workspace |
| [DOCS-HUB](./DOCS-HUB.md) | R2 docs hub notes |
| [FEATURE-ARTIFACT-FLOWS](./FEATURE-ARTIFACT-FLOWS.md) | Artifact flows |
| [FEATURE-ARTIFACT-COMMANDS](./FEATURE-ARTIFACT-COMMANDS.md) | Commands |
| [FEATURE-ARTIFACT-LEGACY-DYNAMICS](./FEATURE-ARTIFACT-LEGACY-DYNAMICS.md) | Archaeology pointer |
| [legacy-dynamics](./legacy-dynamics.md) | Archaeology how-to |
| [ARTIFACTGRAPH](./ARTIFACTGRAPH.md) | MCP / graph |
| [HUBDOCS](./HUBDOCS.md) | Docs ID index MCP |
| [BUNDLEKIT](./BUNDLEKIT.md) | Bundle IR MCP (Phase 1) |
| [PROCESSKIT](./PROCESSKIT.md) | Business process trace + impact review MCP |
| [CODEGENKIT](./CODEGENKIT.md) | FE portal/unit codegen MCP |
| [TESTKIT](./TESTKIT.md) | Plans render + Playwright gen MCP |
| [PLATFORM-DNA](./PLATFORM-DNA.md) | Profile resolver + portable harness/maps bootstrap |
| [Toolkits (MCP)](/platform/guide/toolkits) | **Gộp** install · profiles · ownership · package contract · status |
| [CODEGRAPH](./CODEGRAPH.md) | CodeGraph |

### Stack bases (moved from code repos R2 sync)

| Doc | Base |
|-----|------|
| [FAST-API-*](./FAST-API-QUICKSTART.md) · [FAST-CODEGEN](./FAST-CODEGEN.md) | `fast-api-base` |
| [NEST-API-STRUCTURE](./NEST-API-STRUCTURE.md) · [BACKEND-CODEGEN](./BACKEND-CODEGEN.md) | `nuxt_nest` / `next_nest` BE |
| [REPO-SPLIT-MAP](./REPO-SPLIT-MAP.md) · [CONTRACT-PORTAL-FAST](./CONTRACT-PORTAL-FAST.md) | cross-stack |

`integration` và `line` không còn tài liệu trong docs hub — mỗi repo tự giữ
handbook/skill của mình. Xem git: [integration](https://github.com/raintr91/integration) ·
[line](https://github.com/raintr91/winform).

Templates: `templates/api/` · `templates/clients/`.  
Schemas: `schemas/backend-api.schema.json`.

Full list: browse this directory. FE/BE **codegen runners** stay in code repos (`portal:gen`, etc.).
