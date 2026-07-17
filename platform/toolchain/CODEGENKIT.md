# Codegenkit

Independent MCP/harness for **FE and BE** code generation in one package.

Repository: <https://github.com/raintr91/codegenkit>

## Profiles

| Type | Role | Adapters |
|------|------|----------|
| `fe` | portal / unit codegen | `nuxt4`, `nextjs` (shipped) |
| `be` | `/api` + API unit codegen | `fastapi`, `laravel modules-v1` (0.3.0) |
| `docs` / `tests` | **forbidden** | — |

```bash
codegenkit init --type=fe --adapter=nuxt4 --docs-root=/path/to/docs-hub --yes
codegenkit init --type=be --adapter=fastapi --yes
codegenkit init --type=fullstack --fe-adapter=nextjs --be-adapter=laravel --yes
```

Fullstack repos use the explicit combined profile. Choose technology at install
time; do not split a separate Apikit unless FE/BE lifecycle truly cannot share
the package.

## Local install

```bash
cd /path/to/codegenkit
pnpm install && pnpm test
```

Set `CODEGENKIT_DOCS_ROOT` or `--docs-root` for FE generation. No sibling docs
hub is assumed.

ArtifactGraph is optional for allowlist recommendation only. Executable gen
belongs to Codegenkit.

Codegenkit 0.3.0 replaced the Laravel placeholder with the recovered
registry-driven Artisan planner and unit generator. BE `init` also syncs the
selected adapter registries into the target repository with managed-conflict
checks.

Codegenkit 0.3.1 adds manifest-aware lifecycle commands:

```bash
codegenkit status --project-root=/path/to/code
codegenkit prune --project-root=/path/to/code       # dry-run
codegenkit prune --project-root=/path/to/code --yes # unmodified stale only
```

Codegenkit 0.3.3 pins installers to immutable tag `v0.3.3`, requires docs-hub
`ir/spec.yaml` for FE `--id` generation (no bundle YAML fallback), and ships
`codegenkit common-registry` plus `schemas/common-registry.schema.json`.