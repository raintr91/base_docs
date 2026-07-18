# Docs hub — agent instructions

## Terminology (speak this way)

| Say | Means | Examples |
|-----|-------|----------|
| **Repo** | Destination product checkout the team shares and updates | `base-docs`, `base-tests`, `portal`, `api`, `nextjs`, … |
| **Toolkit** | Independent MCP package / CLI that installs skills into a repo | Hubdocs, Bundlekit, Processkit, Codegenkit, Testkit, ArtifactGraph, Platform DNA, CodeGraph |

Do **not** call a toolkit a “repo” in conversation (even though each toolkit also
has its own Git repository for package source). “Repo” = artifact hubs
(docs / tests / code). “Toolkit” = the tools members install onto those hubs.

## Docs lane (this repo)

The repository does not vendor package-owned Cursor skills. On a fresh clone,
install only the toolkits your lane needs — each toolkit is independent. Read
the per-toolkit catalog in
[`platform/toolchain/MCP-INSTALL.md`](./platform/toolchain/MCP-INSTALL.md)
(convenience lane bundles: [`MCP-INSTALL-PROFILES.md`](./platform/toolchain/MCP-INSTALL-PROFILES.md)).
Each toolkit's `init` then materializes its own `.cursor/` skills and local MCP wiring.

People entry: [`platform/guide/start-now.md`](./platform/guide/start-now.md)  
Tree + standards: [`platform/guide/SYSTEM-DOC-STRUCTURE.md`](./platform/guide/SYSTEM-DOC-STRUCTURE.md)

| Command | Skill |
|---------|-------|
| `/architecture` | arc42 router → chapter / business layer |
| `/context` | §03 LND/CTX (overview, actors, operational areas) |
| `/containers` | §05 C4 runtime containers (`CTR-*`) + CMP index |
| `/component` | `product/components/CMP-*` (module) |
| `/journey` | §06 `FLOW-*` (`/dynamics` = deprecated alias) |
| `/deployment` | §07 stub-first DEP |
| `/cross-cutting` | §08 |
| `/decision` | §09 ADR |
| `/hubdocs` | Optional local arc42/C4 Markdown index |
| `/spec` · grill · `/legacy-spec` · `/update-spec*` | Feature Code lane |
| `/business-process-trace` | Brownfield cross-system process trace |
| `/flow-trace` | Deprecated alias → `/business-process-trace` |

Architecture plan / entry: [`platform/guide/start-now.md`](./platform/guide/start-now.md) · [`SYSTEM-DOC-STRUCTURE.md`](./platform/guide/SYSTEM-DOC-STRUCTURE.md)

Implementation (`/prototype` `/api` `/wire` `/test` `/unit`) → **code** repos (portal, api, …).

Handbook: `platform/toolchain/` · Installed skills (local/generated): `.cursor/skills/`
