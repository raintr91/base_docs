# Tests hub (R3)

**SSOT plans:** sibling [`base-tests`](../../../base-tests/) — not next to Code bundles, not on FE.

| Artifact | Path |
|----------|------|
| Landscape / contexts / targets | `base-tests/landscape|contexts|targets/` |
| Scenarios `SC-*` | `base-tests/scenarios/CMP-*/` |
| Cases `TC-*` YAML | `base-tests/cases/W-*/` |
| Suites | `base-tests/suites/` |
| Vocabulary | `base-tests/catalog/test_case_vocabulary.txt` |
| Templates | `base-tests/templates/` |
| Render plan MD | `cd ../base-tests && pnpm cases:render` |
| Index | `base-tests/registries/tests-index.json` |

## Lanes

| Lane | Repo | Commands |
|------|------|----------|
| **Plans** | `base-tests` | `/testcase` · `/grill-testcase` · `pnpm cases:render` |
| **Design** | `base-docs` | `/spec` (bundle only — **no** testcase r1) · grill-docs |
| **Playwright** | FE (portal, …) | `/test` · `/grill-test` · `pnpm testcase:gen --id …` |

## Gen (plans → FE scripts)

```bash
# On FE:
pnpm testcase:gen --id TC-LOGIN-VALID
pnpm testcase:gen --id smoke
pnpm test:e2e
```

`testcase:gen` **reads** hub YAML → **writes** `tests/e2e/`. Do not treat FE specs as plan SSOT.

## Spec markdown links

Design `docs:render` does **not** emit testcase MD. Spec headers point here / `base-tests` ids. Review MD for cases: `pnpm cases:render` on the tests hub.

See also [HUBS](./HUBS.md).
