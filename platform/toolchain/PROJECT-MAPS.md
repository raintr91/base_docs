# Project maps

Project maps are local generated config, not repository content.

There are two independent repo-only configs:

| Generated file | Owner | Purpose |
|----------------|-------|---------|
| `platform-repos.json` | Platform DNA | Current checkout identity (lane/role) |
| `platform-repos.example.json` | Platform DNA | Portable current-repo baseline |
| `legacy-repos.json` | Bundlekit | Optional legacy evidence repo catalog |
| `legacy-repos.example.json` | Bundlekit | Empty portable legacy baseline |

Both configs contain **repos only**—never toolkits, skills, adapters, harness
profiles, or install state. Toolkit installation truth belongs in each
toolkit's `install-manifest.json`.

Platform DNA never writes `legacy-repos*`; Bundlekit never writes
`platform-repos*`. Other toolkits write neither.

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
platform-dna init      # wizard: agents → lane → adapter (khi cần)
```

CI/non-interactive giữ cờ dài: `platform-dna validate --type=docs --project-root=.`
rồi `platform-dna init --type=docs --project-root=. --yes`.

Platform DNA:

- rejects `../`, home paths, drive paths and UNC paths in generated portable maps;
- seeds `platform-repos.json` + example with current `root: "."` only;
- removes obsolete `harness` inventory from an existing platform map.

Bundlekit init seeds the empty portable legacy maps. Machine checkout roots stay
in ignored `legacy-repos.local.json`.

Schemas live with their owners: Platform DNA
[`platform-repos`](https://github.com/raintr91/platform-dna/tree/main/templates/schemas)
and Bundlekit
[`legacy-repos`](https://github.com/raintr91/bundlekit/tree/main/templates/schemas).
