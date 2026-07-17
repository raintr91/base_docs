# Codegenkit

Independent MCP/harness for **FE and BE** code generation in one package.

Repository: <https://github.com/raintr91/codegenkit>

## Profiles

| Type | Role | Adapters |
|------|------|----------|
| `fe` | portal / client codegen | `nuxt4`, `nextjs`, `dotnet-line` (0.4.0) |
| `be` | `/api` + API unit codegen | `fastapi`, `laravel modules-v1`, `dotnet-integration` (0.4.0) |
| `docs` / `tests` | **forbidden** | — |

```bash
codegenkit init --type=fe --adapter=nuxt4 --docs-root=/path/to/docs-hub --yes
codegenkit init --type=fe --adapter=dotnet-line --yes
codegenkit init --type=be --adapter=fastapi --yes
codegenkit init --type=be --adapter=dotnet-integration --yes
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

Codegenkit 0.3.4 pins installers to immutable tag `v0.3.4`, requires docs-hub
`ir/spec.yaml` for FE `--id` generation (no bundle YAML fallback), and ships
`codegenkit common-registry` plus `schemas/common-registry.schema.json`.

FastAPI codegen/unitgen generates every selected entity and writes schema-v2
manifests with SHA-256 ownership. Existing unmanaged or locally modified files
block the batch unless `--force` is explicit; dry-run and unsafe
traversal/symlink paths perform zero writes. Ambiguous multi-entity endpoints
warn and receive isolated CRUD defaults rather than cross-wiring.

FE package rules are adapter-neutral and manifest-managed. Stack-specific
invariants, component splitting and import aliases remain product-owned.

Codegenkit 0.4.0 adds selectable .NET 8 adapters:

- FE `dotnet-line` — Line client pilot (`kiosk-check-in`) via `gen` / `gen:dry` / `registry`
- BE `dotnet-integration` — Integration gateway pilot (`mes-downtime`) via `api-gen` / `api-gen:dry` / `api-registry`

Both use `CODEGENKIT_ROOT` as the only write root and require the .NET 8 SDK
(`CODEGENKIT_DOTNET` or `dotnet`). Their main generation pass bundles test
outputs; separate unit-gen commands are unsupported. These are pilot-specific
engines, not generic .NET generators. Installers pin `v0.4.0`.