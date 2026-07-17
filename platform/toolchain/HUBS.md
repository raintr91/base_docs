# Docs + tests hubs (R2 / R3)

| Artifact | Repo |
|----------|------|
| C4 architecture + product Code (`W-*` / `API-*` design) | [`base-docs`](../..) |
| E2E **plans** (`SC-*` / `TC-*` / suites) + `cases:render` | [`base-tests`](https://github.com/raintr91/base_test) |
| App / codegen / Playwright **scripts** | **FE/code** repos |
| OpenAPI serve | **code** (design yaml on docs) |

```bash
cd <base-docs-checkout> && pnpm docs:dev          # design only (no testcase MD)
cd <base-tests-checkout> && pnpm cases:render     # plan YAML → MD
cd <portal-checkout> && pnpm testcase:gen --id W-AD-AUTH-001
```

Indexes: `base-docs/registries/docs-index.json` · `base-tests/registries/tests-index.json`

Plans handbook: [TESTS-HUB](./TESTS-HUB.md).
