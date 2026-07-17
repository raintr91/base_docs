# Testkit

Independent MCP/harness for tests-hub plans and FE Playwright generation.

Repository: <https://github.com/raintr91/Testkit>

## Profiles

| Type | Synced skills | Tools |
|------|---------------|-------|
| `tests` | `/testcase` `/grill-testcase` | `cases_render` `cases_check_*` |
| `fe` | `/test` `/grill-test` | `testcase_gen*` `e2e_registry_validate` |

```bash
testkit init --type=tests --yes
testkit init --type=fe --tests-root=/path/to/tests-hub --docs-root=/path/to/docs-hub --yes
```

Do not assume sibling `../base-tests` or `../base-docs`. ArtifactGraph is optional.

Testkit 0.2.4 pins installers to immutable tag `v0.2.4` (lockfile-enforced),
preflights every generated E2E output so writes stay under `tests/e2e`, and
drives `cases:check` through Ajv against the package-owned
`schemas/testcase.schema.json` (schema resolves from the package, not the
destination cwd).

Docs-hub `ir/spec.yaml` enrichment is optional: tests-only IDs resolve without
docs topology, and unavailable enrichment warns once while generation
continues. Deterministic goldens cover render, local coverage happy/gap,
generator output, and cross-root portability.

Testkit 0.2.0 tracks profile-owned files and supports safe lifecycle cleanup:

```bash
testkit status --project-root=/path/to/target
testkit prune --project-root=/path/to/target       # dry-run
testkit prune --project-root=/path/to/target --yes # unmodified stale only
```
