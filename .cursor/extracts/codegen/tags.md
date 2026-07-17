# Portal Codegen Tags

Hub: `platform/toolchain/PORTAL-CODEGEN.md` · registry: `registries/design.registry.json`

## Who adds what

| Phase | Spec |
|-------|------|
| `/legacy-spec`, `/spec` | Design v1 — no `codegen`, gen `tags` |
| `/grill-with-docs` | `codegen`, `ui.*`, `tags` — see `codegen/readiness.md` |
| `/prototype` | `portal:gen` + HANDOFF; implement `#needs-ui` / `#needs-component` |

## Key blocks

`codegen.profile|entity|module|skip` · `ui.filters|columns|composition` · `api.endpoints[].action`

## Hashtags (summary)

| Tag | Use |
|-----|-----|
| `#shell: DataListPage` | List default |
| `#pattern: CRUD` | CRUD flow |
| `#ui:` / `#widget:` | shadcn / form field |
| `#needs-component: {slot}:MoXxx[:prop]` | Prototype implements — portal-gen HANDOFF |
| `#needs-ui:` | Registry planned widget |
| `#common:{id}` | Shared hook/service — `platform-common.registry.json` |
| `#needs-common:{id}` | Planned logic — HANDOFF |
| `#wire-only:` | Defer to `/wire` |
| `#gen:test-*` | Unit gen — FE checkout only |
| `#tech-debt:` | See `grill-tech-debt.md` |
| `#update:*` | `/update-spec` delta — cleared at `/wire` |

List grill default tags if missing: `#shell: DataListPage`, `#pattern: CRUD`, `#style: shadcn/ui`, `compact`, `flat`.

## Commands

These run in the **FE checkout**, not this docs hub:

```bash
pnpm portal:registry
pnpm portal:gen:dry --id <W-|CMP-|CTR-…>
pnpm portal:gen --id …
pnpm portal:unit-gen --id …
```

Detail tables: `platform-mark.md`. FE unit/design registries live in the code repo, not this docs hub.
