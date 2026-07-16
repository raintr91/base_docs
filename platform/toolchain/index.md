# Toolchain

Handbook + how-to for Code IR (split/render/validate). **SSOT: this hub** (`base-docs`).

## Scripts (this repo)

```bash
pnpm spec:split -- product/components/…/code/W-*/….bundle.yaml
pnpm docs:render -- --yaml-root product/components --md-root product/components   # adjust flags as needed
pnpm docs:render:common
pnpm legacy-dynamics:validate -- product/legacy-dynamics/…/_legacy.dynamics.yaml
```

| Script | Path |
|--------|------|
| spec split/merge/normalize | `scripts/spec/` |
| docs render | `scripts/docs/` |
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
