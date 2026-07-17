# Platform DNA

Executable profile resolver and portable harness bootstrap.

Repository: <https://github.com/raintr91/platform-dna>

## Ownership

- `/platform-ai` in docs profiles.
- Profile-specific `platform-ai.mdc` and `team-flow-router.mdc`.
- Shared harness-state, contract-naming and agent-discipline assets.
- `profiles.json`: required/optional packages and supported adapters.
- Portable `platform-repos` / `legacy-repos` schemas and seed policy.

Platform DNA does **not** own architecture, spec, process, codegen or test
skills. It invokes each owning package's `init` with the selected subset.
It never installs into MCP tooling repos (`hubdocs`, `bundlekit`, …).

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

Platform DNA 0.1.3 tracks only DNA-owned harness files. Product maps,
`.gitignore`, specialist assets and locally modified stale files are never
pruned:

```bash
platform-dna status --project-root=/path/to/hub
platform-dna prune --project-root=/path/to/hub       # dry-run
platform-dna prune --project-root=/path/to/hub --yes # unmodified stale only
```

Platform DNA 0.1.5 pins its installers to `v0.1.5` and publishes the canonical
docs/FE lane-boundary rules. Installed `platform-ai`, router, harness-state and
contract-naming files are tracked in `.platform-dna/install-manifest.json`;
specialist Codegenkit/Testkit rules remain owned by those packages.
