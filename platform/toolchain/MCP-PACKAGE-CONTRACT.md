# MCP package contract

> Shared install, ownership and compatibility contract for Hubdocs,
> ArtifactGraph, Bundlekit, Processkit, Codegenkit and Testkit.

## Package manifest

Each package publishes a machine-readable `mcp-package.json`:

```json
{
  "schemaVersion": 1,
  "package": "@platform/bundlekit",
  "version": "0.1.0",
  "types": ["docs"],
  "requires": [],
  "optional": ["@platform/hubdocs", "@platform/artifactgraph"],
  "tools": ["bundle_split", "bundle_check"],
  "assets": [
    {
      "source": "harness/docs/skills/spec/SKILL.md",
      "target": ".cursor/skills/spec/SKILL.md",
      "type": "docs",
      "owner": "@platform/bundlekit"
    }
  ],
  "compatibility": {
    "node": ">=22",
    "toolApi": 1,
    "harnessApi": 1
  }
}
```

Rules:

1. One target asset has exactly one package owner.
2. `requires` is needed for correctness; `optional` only accelerates.
3. A profile installs a package subset; it never changes runtime ownership.
4. Package version and manifest hash are recorded on init.

## Install manifest

Project-local state lives in `.<package>/install-manifest.json`:

```json
{
  "schemaVersion": 1,
  "package": "@platform/bundlekit",
  "packageVersion": "0.1.0",
  "types": ["docs"],
  "toolApi": 1,
  "harnessApi": 1,
  "installedAt": "ISO-8601",
  "files": {
    ".cursor/skills/spec/SKILL.md": {
      "source": "harness/docs/skills/spec/SKILL.md",
      "sha256": "<installed-content-hash>"
    }
  }
}
```

## Lifecycle

### `init`

- Create missing managed files.
- Update only files still matching their previous installed hash.
- Report locally modified managed files as conflicts.
- `--force` may replace conflicts explicitly.
- Never write another toolkit's repo config. Platform DNA alone writes
  `platform-repos*.json`; Bundlekit alone writes `legacy-repos*.json`.
  Neither config contains toolkit/install inventory; installed skills/adapters
  are recorded in each toolkit's own install manifest.
- Never write or overwrite `*.local.json`.

### Upgrade

- Validate `toolApi` and `harnessApi` before syncing.
- Preserve local changes as conflicts.
- Assets removed from the new package become **stale**, not auto-deleted.
- Show the exact `prune` command.

### `prune`

- Delete only stale files whose current hash equals the old installed hash.
- Never delete modified files.
- Remove only this package's managed files/config entries; project maps are
  never prune targets.
- `--dry-run` is mandatory and default; deletion requires `--yes`.

### Uninstall

- Run safe prune first.
- Remove machine-local MCP entry for this package.
- Keep user-modified managed files and report them.
- Package binary uninstall is separate from project harness uninstall.

## Compatibility failures

- Unsupported `toolApi`/`harnessApi`: fail before file writes.
- Missing `requires`: fail with install command.
- Missing `optional`: continue and log one structured fallback event.
- Synced skill newer than tool: fail with package upgrade/re-init guidance.

## Portability

Committed manifests/templates may contain repo-relative paths or stable Git
URLs only. Machine executable paths and checkout roots stay in ignored MCP
configuration or `*.local.json`.
