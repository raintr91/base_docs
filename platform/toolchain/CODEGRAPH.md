# CodeGraph (agent code intelligence)

Local MCP tool: **`codegraph_explore`**. Upstream: [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) · rule SSOT: `.cursor/rules/codegraph.mdc`.

## Install (this machine)

**WSL (zsh)** — CLI for indexing Linux checkouts:

```bash
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh
# new shell or: source ~/.zshrc
codegraph version
```

**Windows (PowerShell)** — Cursor MCP + WinForms/station:

```powershell
irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex
codegraph install --target=cursor --yes
```

Restart Cursor after MCP install.

## Per-repo index

```bash
cd /path/to/repo
codegraph init          # creates .codegraph/ + full index
codegraph status
```

`.codegraph/` is **gitignored** — local only.

| Checkout | Where to `init` |
|----------|-----------------|
| Repository opened in WSL | WSL |
| Repository opened on Windows | Windows PowerShell |

Do **not** share one `.codegraph/` across Win + WSL for the same tree (`CODEGRAPH_DIR=.codegraph-win` if needed).

## Agent usage

1. Structural code → `codegraph_explore` (rule `codegraph.mdc` alwaysApply).
2. Cross-repo → require an explicit `projectPath` from the user or a machine-local
   `legacy-repos.local.json`; never infer sibling layout.
3. Spec/grill/legacy-spec → docs + IR first; CodeGraph only for source evidence.

## Sync

Rule lives in `.cursor/rules/codegraph.mdc` (per-repo; no cross-factory sync).
