# Platform DNA

Executable profile resolver and portable harness bootstrap.

Repository: <https://github.com/raintr91/platform-dna>

## Ownership

- Repo-only `platform-repos` schema and seed policy.
- FE `/platform-base` for the Nuxt/Next adapters.
- `profiles.json`: recommended/optional toolkits and supported adapters.

Platform DNA does **not** own architecture, spec, process, codegen or test
skills. It invokes each owning toolkit's `init` with the selected subset.
It never installs into toolkit source repos (`hubdocs`, `bundlekit`, …).
Each toolkit keeps its own local `/platform-ai` for toolkit maintenance;
Platform DNA never syncs `/platform-ai` or lane/meta rules into destination
repos. Bundlekit separately owns `legacy-repos`.

## Install profiles

```bash
platform-dna init --type=docs --project-root=/path/to/docs --yes
platform-dna init --type=fe --adapter=nextjs --project-root=/path/to/fe --yes
platform-dna init --type=be --adapter=fastapi --project-root=/path/to/be --yes
platform-dna init --type=tests --project-root=/path/to/tests --yes
```

Use `--with=artifactgraph` for a declared optional accelerator,
`--package-root packageId=/path` for local package development, or
`--no-install` to reject missing package binaries.

## Safety

- Lane/adapter mismatch fails before package initialization.
- Targets with `mcp-package.json` or declared `role=tooling` are rejected.
- Empty new bases require explicit `--force`.
- Committed machine/sibling paths are rejected even when specialist packages
  are locally available.
- Managed meta-harness conflicts require review or explicit `--force`.
- `--dry-run` is non-mutating and prints the complete package invocation plan.

Platform DNA tracks only its `/platform-base` adapter asset. Project maps,
`.gitignore`, specialist assets and locally modified stale files are never
pruned:

```bash
platform-dna status --project-root=/path/to/hub
platform-dna prune --project-root=/path/to/hub       # dry-run
platform-dna prune --project-root=/path/to/hub --yes # unmodified stale only
```

Installed `/platform-base` is tracked in
`.platform-dna/install-manifest.json`; all other skills/rules stay with their
owning toolkit or destination repo.
