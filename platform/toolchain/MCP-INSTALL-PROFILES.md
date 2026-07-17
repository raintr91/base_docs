# MCP install profiles

`--type` selects a **required package set** for the current repository. Packages
remain independently installable; the profile only coordinates defaults.

**Resolver owner:** [Platform DNA](./PLATFORM-DNA.md).

```bash
platform-dna init --type=docs --project-root=/path/to/docs --yes
platform-dna init --type=fe --adapter=nuxt4 --project-root=/path/to/portal --yes
platform-dna init --type=be --adapter=laravel --project-root=/path/to/api --yes
platform-dna init --type=tests --project-root=/path/to/base-tests --yes
```

| `--type` | Required | Optional accelerators | Notes |
|----------|----------|-----------------------|-------|
| `docs` | hubdocs · **bundlekit** · processkit | artifactgraph · codegraph | No FE/BE gen skills |
| `fe` | codegenkit · testkit · processkit (impact subset) | artifactgraph · codegraph · hubdocs | `--adapter=nuxt4\|nextjs` |
| `be` | codegenkit · processkit (impact) | artifactgraph · codegraph · hubdocs | `--adapter=fastapi\|laravel\|…` |
| `tests` | testkit | artifactgraph | cases authoring |

> Platform DNA does **not** install into MCP tooling repos. Specialist packages
> keep their own `init` / harness.

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

- `profiles.json` is the executable required/optional package manifest.
- Missing required packages are installed from canonical Git repositories into
  `~/.platform-dna/packages`; `--no-install` requires preinstalled binaries.
- `--package-root packageId=/path` supports local package development.
- FE/BE adapters are explicit and target markers are checked before mutation.
- DNA syncs only meta rules/maps; each specialist package syncs its own profile
  subset.
- `--dry-run` prints all package invocations without writing or cloning.
- Uninstall/prune and cross-version compatibility remain Phase 6 lifecycle
  verification (`T6.6`, `T6.7`), not resolver ownership gaps.
