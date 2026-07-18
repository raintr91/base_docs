# MCP install profiles

A profile is a **recommended capability bundle** per lane — a convenience over
installing kits one by one. Every kit stays independently installable and works
standalone; the profile only automates typing several `init` commands.

- Per-kit independent install: [MCP-INSTALL](./MCP-INSTALL.md) (start here)
- Kit ownership: [MCP-OWNERSHIP](./MCP-OWNERSHIP.md)

**Resolver owner:** [Platform DNA](./PLATFORM-DNA.md).

```bash
platform-dna init --type=docs --project-root=/path/to/docs --yes
platform-dna init --type=fe --adapter=nuxt4 --project-root=/path/to/portal --yes
platform-dna init --type=be --adapter=laravel --project-root=/path/to/api --yes
platform-dna init --type=tests --project-root=/path/to/base-tests --yes
```

| `--type` | Recommended toolkits | Optional accelerators | Notes |
|----------|----------------------|-----------------------|-------|
| `docs` | hubdocs · bundlekit · processkit | **artifactgraph** (home) · codegraph | Registry / architecture hub |
| `fe` | codegenkit · testkit · processkit (impact subset) | codegraph · hubdocs (`HUBDOCS_ROOT`→docs) · artifactgraph (rare) | Set `CODEGENKIT_DOCS_ROOT`; AG stays on docs for full registries |
| `be` | codegenkit · processkit (impact) | codegraph · hubdocs · artifactgraph (rare) | Same pointer rule as FE |
| `tests` | testkit | artifactgraph (rare) | cases authoring |

> "Recommended toolkits" are capabilities a typical lane wants — not runtime
> dependencies. Install any subset directly (see [MCP-INSTALL](./MCP-INSTALL.md));
> each toolkit runs without the others.
>
> **Docs is the registry hub.** FE/BE use machine-local docs pointers
> (`CODEGENKIT_DOCS_ROOT`, optional `HUBDOCS_ROOT`). Install ArtifactGraph on
> docs by default (`--with=artifactgraph`); on FE/BE only when local tag hints
> are needed — AG does not follow the docs pointer.

> Platform DNA does **not** install into toolkit source checkouts. Specialist
> toolkits keep their own `init` / harness and toolkit-local `/platform-ai`.

## Codegenkit (FE + BE)

One package owns code generation. Lane and stack are chosen at init:

```bash
codegenkit init --type=fe --adapter=nuxt4 --yes
codegenkit init --type=be --adapter=fastapi --yes
```

Fullstack repos may init both profiles explicitly. Docs hub never gets
Codegenkit by default.

## Bundlekit

```bash
bundlekit init --type=docs --target=cursor --yes
```

Only `--type=docs` is implemented in Bundlekit 0.1.0.

## Resolver contract

- `profiles.json` is the executable recommended/optional toolkit manifest.
- Recommended toolkits are installed from canonical Git sources into
  `~/.platform-dna/packages`; `--no-install` requires preinstalled binaries.
- `--package-root toolkitId=/path` supports local toolkit development.
- FE/BE adapters are explicit and target markers are checked before mutation.
- DNA syncs only repo identity plus FE `/platform-base` for Nuxt/Next; each
  specialist toolkit syncs its own profile subset independently.
- `--dry-run` prints all package invocations without writing or cloning.
- Uninstall/prune and cross-version compatibility remain Phase 6 lifecycle
  verification (`T6.6`, `T6.7`), not resolver ownership gaps.
