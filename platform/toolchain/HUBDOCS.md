# Hubdocs MCP

Optional external MCP for **arc42 × C4 docs hubs**: index architecture/product
IDs, dependencies, orphans, links, and chapter routes. Markdown in the current
project remains the source of truth. Hubdocs also owns/syncs the architecture
skill family (`/architecture` … `/dynamics`) via `hubdocs harness install`.

- GitHub: [raintr91/hubdocs](https://github.com/raintr91/hubdocs)
- No sibling checkout or fixed workspace layout is assumed.
- ArtifactGraph is optional only (registries/tags). Hubdocs never requires it;
  ArtifactGraph must not own architecture Markdown.

| | ArtifactGraph (nội bộ) | Hubdocs |
|--|----------------------|---------|
| Focus | registries / tags / allowlisted gen | architecture + product **IDs**, links, chapter route |
| SSOT | product `registries/` | docs hub `architecture/` + `product/` MD |

## Install / wire agents (owner-run)

```bash
curl -fsSL https://raw.githubusercontent.com/raintr91/hubdocs/main/install.sh | bash
cd /path/to/a/docs-project
hubdocs init --yes
# interactive: hubdocs init
```

Windows: `irm https://raw.githubusercontent.com/raintr91/hubdocs/main/install.ps1 | iex`

Requires **Node ≥ 22**. Project-local `hubdocs init` selects the current docs
project; Hubdocs does not default to `base-docs`.

MCP config do `hubdocs init` sinh chứa path của máy hiện tại, vì vậy được
gitignore và phải tạo lại sau khi clone; không copy config từ máy khác.

Docs: package [`docs/INIT.md`](https://github.com/raintr91/hubdocs/blob/main/docs/INIT.md) · [`docs/INSTALL.md`](https://github.com/raintr91/hubdocs/blob/main/docs/INSTALL.md)

Hubdocs 1.0.1 tracks only its direct-copy harness assets; shared extract
registry and project map remain outside prune ownership:

```bash
hubdocs status --project-root=/path/to/docs
hubdocs prune --project-root=/path/to/docs       # dry-run
hubdocs prune --project-root=/path/to/docs --yes # unmodified stale only
```

## Skill

`/hubdocs` · also hooked from `/architecture`, `/journey`, `/context`, …

## Tools

`hubdocs_list_ids` · `hubdocs_get_element` · `hubdocs_deps_of` · `hubdocs_dependents_of` · `hubdocs_orphans` · `hubdocs_validate_links` · `hubdocs_route` · `hubdocs_journeys` · `hubdocs_layout`

## Later (only if pain)

Structurizr MCP (C4 hierarchy rename đau). **No** Mermaid MCP · **No** Kroki backlog.
