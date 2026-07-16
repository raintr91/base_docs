---
name: spec
extractBundle: spec-requirement
description: /spec — author design bundle only (no testcase plans). Plans → base-tests /testcase.
disable-model-invocation: true
---

# /spec — Function detail (design)

**Business layer:** Function (screen `W-*` / API `API-*` inside a module)  
**Standards:** **C4 only** — do **not** open new arc42 chapters for one screen.

**Extracts:** `extractBundle: spec-requirement` → `.cursor/extracts/extract-registry.json`

Template: `base-docs/templates/feature.bundle.yaml` · rules: `base-docs/templates/bundle-authoring.md`  
Tree: [`platform/guide/SYSTEM-DOC-STRUCTURE.md`](../../../platform/guide/SYSTEM-DOC-STRUCTURE.md) · [Start now](../../../platform/guide/start-now.md)

## Scope

**In:** Code bundle / `--id` under `product/components/CMP-*/code/`, `pnpm spec:split`, `pnpm docs:render` (design MD only), harness notes.

**Out:** E2E plans → **`base-tests` `/testcase`**. Legacy → `/legacy-spec`. UI → `/prototype` after grill-docs. Overview/CTR → `/architecture` children.

## Workflow

1. Confirm **module (`CMP-*`) exists** and surface/CTR is known — else stop for lead/owner.
2. If bundle exists, verify gaps: actors, fields, validations, routes, actions, API contracts, edge cases, acceptance.
3. If new, draft from user bullets — `*.bundle.yaml` with `specOrigin: requirement` under `code/W-*` or `code/API-*`.
4. Incremental blocks per extracts when needed.
5. Apply common UI / spec-split extracts.
6. `pnpm spec:split -- <bundle>` then `pnpm docs:render` (**no** testcase MD emit).
7. Update `.harness/progress.md` when present.
8. Handoff plans: open **base-tests** → `/testcase` from acceptance.

## Output

- `spec` / `design` only (see `bundle-authoring.md`)
- **Không** author `TC-*` / `*.test.yaml` here (R3)

## Rules

- Do not edit FE production code or Playwright.
- Do not run `portal:gen` / `testcase:gen`.
- Vague spec → `/bqa-grill-docs` before `/prototype`.
- No arc42 chapter prose for a single function — stay C4/code-level.

## Done

- Design bundle coherent · split + docs:render pass · plans handoff → `/testcase` on tests hub.
