# Processkit

Independent MCP/harness package for brownfield business-process tracing and
code-change impact review.

Repository: <https://github.com/raintr91/Processkit>

## Profiles

| Type | Synced skills |
|------|---------------|
| `docs` | `/business-process-trace`, `/business-impact-review`, deprecated `/flow-trace` redirect |
| `fe`, `be` | `/business-impact-review` |

## Local install/init

```bash
cd /path/to/Processkit
pnpm install
pnpm test

cd /path/to/target
processkit init --type=docs --target=cursor --yes
```

`init` merges Processkit into machine-local `.cursor/mcp.json`, syncs only the
selected profile, and merges package-owned skill IDs into
`platform-repos.json`. Docs init seeds empty portable `legacy-repos.json` and
example files only when missing. Machine roots remain in ignored
`legacy-repos.local.json`; Processkit never writes local maps.

## Tools

- `business_process_validate`: process step/evidence/reference schema checks.
- `business_impact_validate`: impact-report structure and evidence checks.
- `business_diff_scope`: changed-file/symbol/risk hints; not a call-graph engine.

CodeGraph, Hubdocs and ArtifactGraph are optional accelerators. Without them,
the skills use targeted repository search/model analysis and report unresolved
gaps.

Processkit 0.3.0 tracks profile-owned harness files and ships the reference
missing-optional evidence contract. Fallback runs emit one deduplicated
`processkit.missing-optional` event with measured `fileReads` and
`contextBytes`; they do not estimate token savings.

```bash
processkit status --project-root=/path/to/target
processkit prune --project-root=/path/to/target       # dry-run
processkit prune --project-root=/path/to/target --yes # unmodified stale only
```
