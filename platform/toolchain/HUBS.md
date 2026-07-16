# Docs + tests hubs (R2 / R3)

| Artifact | Repo |
|----------|------|
| C4 architecture + product Code (`W-*` / `API-*` design) | [`base-docs`](../../base-docs/) |
| E2E **plans** (`SC-*` / `TC-*` / suites) + `cases:render` | [`base-tests`](../../base-tests/) |
| App / codegen / Playwright **scripts** | **FE/code** repos |
| OpenAPI serve | **code** (design yaml on docs) |

```bash
cd ../base-docs && pnpm docs:dev          # design only (no testcase MD)
cd ../base-tests && pnpm cases:render     # plan YAML → MD
cd ../portal && pnpm testcase:gen --id W-AD-AUTH-001
```

Indexes: `base-docs/registries/docs-index.json` · `base-tests/registries/tests-index.json`

Plans handbook: [TESTS-HUB](./TESTS-HUB.md).
