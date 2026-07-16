# Hubdocs MCP

Local MCP for **arc42 × C4 docs hubs**: index architecture/product IDs, deps, orphans, links, chapter route.

- GitHub: [raintr91/hubdocs](https://github.com/raintr91/hubdocs)
- Package version: **v0.1.0**
- Plan tick: hubdocs MCP done (see [HUBDOCS](./HUBDOCS.md) body)

| | ArtifactGraph (nội bộ) | Hubdocs |
|--|----------------------|---------|
| Focus | registries / tags / allowlisted gen | architecture + product **IDs**, links, chapter route |
| SSOT | product `registries/` | docs hub `architecture/` + `product/` MD |

## Install / wire agents

```bash
curl -fsSL https://raw.githubusercontent.com/raintr91/hubdocs/main/install.sh | bash
cd /path/to/this/repo          # docs hub (có architecture/)
hubdocs init --yes
# interactive: hubdocs init
```

Windows: `irm https://raw.githubusercontent.com/raintr91/hubdocs/main/install.ps1 | iex`

Requires **Node ≥ 22**. Env `HUBDOCS_ROOT` = absolute path to this docs hub (must contain `architecture/`).

Docs: package [`docs/INIT.md`](https://github.com/raintr91/hubdocs/blob/main/docs/INIT.md) · [`docs/INSTALL.md`](https://github.com/raintr91/hubdocs/blob/main/docs/INSTALL.md)

## Skill

`/hubdocs` · also hooked from `/architecture`, `/journey`, `/context`, …

## Tools

`hubdocs_list_ids` · `hubdocs_get_element` · `hubdocs_deps_of` · `hubdocs_dependents_of` · `hubdocs_orphans` · `hubdocs_validate_links` · `hubdocs_route` · `hubdocs_journeys` · `hubdocs_layout`

## Later (only if pain)

Structurizr MCP (C4 hierarchy rename đau). **No** Mermaid MCP · **No** Kroki backlog.
