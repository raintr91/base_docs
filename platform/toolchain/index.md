# Toolchain

Handbook + how-to for Code IR (split/render/validate). **SSOT: this hub** (`base-docs`).

## Scripts (this repo)

Local fallback (still in-repo). Prefer **Bundlekit** after `bundlekit init --type=docs`:

```bash
pnpm spec:split -- product/components/…/code/W-*/….bundle.yaml
pnpm docs:render -- --yaml-root product/components --md-root product/components   # adjust flags as needed
pnpm docs:render:common
pnpm legacy-dynamics:validate -- product/legacy-dynamics/…/_legacy.dynamics.yaml
# or: bundlekit split|render|legacy-validate …
```

| Script | Path |
|--------|------|
| spec split/merge/normalize | `scripts/spec/` (fallback) · Bundlekit `engines/spec/` (SSOT package) |
| docs render | `scripts/docs/` (fallback) · Bundlekit `engines/docs/` |
| legacy-dynamics validate | `scripts/spec/legacy-dynamics-validate.mjs` |
| Templates | `templates/` |

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
| [MCP-OWNERSHIP](./MCP-OWNERSHIP.md) | Package ownership freeze |
| [MCP-INSTALL-PROFILES](./MCP-INSTALL-PROFILES.md) | `--type` install matrix |
| [MCP-SPLIT-TODO](./MCP-SPLIT-TODO.md) | Plan + checklist for independent MCP packages |
| [CODEGRAPH](./CODEGRAPH.md) | CodeGraph |

### Stack bases (moved from code repos R2 sync)

| Doc | Base |
|-----|------|
| [FAST-API-*](./FAST-API-QUICKSTART.md) · [FAST-CODEGEN](./FAST-CODEGEN.md) | `fast-api-base` |
| [INTEGRATION-*](./INTEGRATION-STRUCTURE.md) · [TEAM-AI-INTEGRATION](./TEAM-AI-INTEGRATION-WORKFLOW.md) | `integration` |
| [NEST-API-STRUCTURE](./NEST-API-STRUCTURE.md) · [BACKEND-CODEGEN](./BACKEND-CODEGEN.md) | `nuxt_nest` / `next_nest` BE |
| [LINE-*](./LINE-CLIENT-STRUCTURE.md) · [TEAM-AI-LINE](./TEAM-AI-LINE-WORKFLOW.md) | `line` |
| [REPO-SPLIT-MAP](./REPO-SPLIT-MAP.md) · [CONTRACT-PORTAL-FAST](./CONTRACT-PORTAL-FAST.md) | cross-stack |

Templates: `templates/api/` · `templates/integration/` · `templates/line/` · `templates/clients/`.  
Schemas: `schemas/backend-api.schema.json`.

Full list: browse this directory. FE/BE **codegen runners** stay in code repos (`portal:gen`, etc.).
