# Bundlekit MCP

Optional external MCP for **docs-hub bundle IR**: split/merge/check/normalize
bundles, render design Markdown, validate legacy-dynamics YAML, and sync owned
docs skills on init.

- Intended GitHub: [raintr91/bundlekit](https://github.com/raintr91/bundlekit)
- Dev: sibling checkout named `bundlekit` next to the docs hub (layout not assumed by portable docs)
- Plan SSOT: [MCP-SPLIT-TODO](./MCP-SPLIT-TODO.md)

| | ArtifactGraph | Hubdocs | Bundlekit |
|--|---------------|---------|-----------|
| Focus | registries / tags / parity | architecture + product IDs | bundle IR + design render |
| Required for `/spec`? | optional accelerator | optional accelerator | **yes after init** |

## Install / wire (owner-run)

```bash
cd /path/to/bundlekit
pnpm install && pnpm build

cd /path/to/docs-hub   # e.g. this base-docs checkout
bundlekit init --type=docs --target=cursor --yes
```

Linux (after publish):

```bash
curl -fsSL https://raw.githubusercontent.com/raintr91/bundlekit/main/install.sh | bash
```

MCP config from `init` is machine-local and gitignored. Do not commit absolute
paths.

## Owned skills

`/spec` · `/update-spec` · `/update-spec-legacy` · `/legacy-spec` ·
`/bqa-grill-docs` · `/dev-grill-docs` · `/grill-with-docs`

## Tools

`bundle_split` · `bundle_merge` · `bundle_check` · `bundle_split_all` ·
`bundle_normalize` · `docs_render` · `docs_render_common` ·
`legacy_dynamics_validate`

## Destination policy

This repository does not vendor Bundlekit engines. Its `pnpm spec:*`,
`pnpm docs:render*`, and `pnpm legacy-dynamics:validate` commands are thin
aliases to the installed `bundlekit` CLI. Run the docs install profile first.

## Docs

Package [`docs/INIT.md`](https://github.com/raintr91/bundlekit/blob/main/docs/INIT.md) ·
[`docs/INSTALL.md`](https://github.com/raintr91/bundlekit/blob/main/docs/INSTALL.md)
