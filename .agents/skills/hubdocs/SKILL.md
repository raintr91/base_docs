---
name: hubdocs
description: /hubdocs — local MCP for arc42/C4 docs hub ID index.
disable-model-invocation: true
extractBundle: architecture-core
---

# /hubdocs — Docs hub MCP

Package: [raintr91/hubdocs](https://github.com/raintr91/hubdocs) · handbook: [`HUBDOCS.md`](../../../platform/toolchain/HUBDOCS.md)

SSOT = MD trong repo này. MCP chỉ index / validate / route.

## When to use

| Need | Tool |
|------|------|
| Layout / ID homes | `hubdocs_layout` |
| List IDs | `hubdocs_list_ids` |
| Open one ID | `hubdocs_get_element` |
| Refs from ID | `hubdocs_deps_of` |
| Who mentions ID | `hubdocs_dependents_of` |
| Missing FLOW/ADR/CMP file | `hubdocs_orphans` |
| Broken MD links | `hubdocs_validate_links` |
| Topic → chapter/skill | `hubdocs_route` |
| List journeys | `hubdocs_journeys` |

Prefer these **before** dumping whole `architecture/**` into context.

## Wire

```bash
curl -fsSL https://raw.githubusercontent.com/raintr91/hubdocs/main/install.sh | bash
cd /path/to/this/repo    # docs hub (có architecture/)
hubdocs init --yes
```

Update: chạy lại cùng lệnh `install.sh`. Restart agent sau `init`.

## Related skills

`/architecture` · `/journey` · `/context` · `/containers` · `/component` · `/decision` · `/deployment`

Plan / entry: [`start-now`](../../../platform/guide/start-now.md) · [`SYSTEM-DOC-STRUCTURE`](../../../platform/guide/SYSTEM-DOC-STRUCTURE.md)
