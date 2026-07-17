# Project maps

Committed config is repository-local:

**SSOT owner:** [Platform DNA](./PLATFORM-DNA.md), which ships schemas and seeds
or merges these maps during profile init.

| File | Purpose |
|------|---------|
| [`platform-repos.json`](../../platform-repos.json) | Current `base-docs` checkout only (`root: "."`) |
| [`platform-repos.example.json`](../../platform-repos.example.json) | Portable local-only example |
| [`legacy-repos.example.json`](../../legacy-repos.example.json) | Shape for optional legacy evidence configuration |

No committed map may assume sibling repositories, a fixed workspace directory,
a user home, or a drive letter. Each code/tests repository owns its own harness.

Project maps exist only in destination product hubs (`docs`, `fe`, `be`,
`tests`). MCP package repositories do not contain `platform-repos*.json`;
their local `/platform-ai` skill is for building and releasing that MCP.

External repositories are documentation references, not local path dependencies:

- Tests plans: [raintr91/base_test](https://github.com/raintr91/base_test)
- Portal reference: [raintr91/nuxt_4](https://github.com/raintr91/nuxt_4)
- Laravel reference: [raintr91/lara12](https://github.com/raintr91/lara12)
- ArtifactGraph: [raintr91/artifactgraph](https://github.com/raintr91/artifactgraph)
- Hubdocs: [raintr91/hubdocs](https://github.com/raintr91/hubdocs)

## Machine-local legacy evidence

Only `/legacy-spec` may need another checkout. Put that path in
`legacy-repos.local.json` (gitignored) on the member's machine:

```bash
cp legacy-repos.example.json legacy-repos.local.json
# Set the checkout root explicitly for this machine.
```

Agents must not guess paths or infer that repositories are siblings. Read only
the requested project entry from the local map. ArtifactGraph and Hubdocs are
installed tools; their `init` commands generate machine-local MCP config.

## Bootstrap and validation

```bash
platform-dna validate --type=docs --project-root=.
platform-dna init --type=docs --project-root=. --yes
```

The resolver:

- rejects `../`, home paths, drive paths and UNC paths in committed maps;
- seeds `platform-repos.json` + example with current `root: "."` only;
- seeds empty legacy maps for docs profiles;
- adds `platform-repos.local.json` and `legacy-repos.local.json` to
  `.gitignore`;
- preserves package-owned skill lists by merge rather than replacing the map.

Schemas live in
<https://github.com/raintr91/platform-dna/tree/main/templates/schemas>.
