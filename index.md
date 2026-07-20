# Base Docs (R2)

Docs hub — **arc42** TOC (*why*) · **C4** views (*what*) · **Product Code** (*detail*).

**Team mới:** [Start now](/platform/guide/start-now) · [Doc structure](/platform/guide/SYSTEM-DOC-STRUCTURE)

| Area | Path | Format |
|------|------|--------|
| Handbook | `platform/` | MD |
| Architecture | `architecture/01`…`12` | MD + Mermaid |
| Components | `product/components/CMP-*` | README MD; Code under `code/` |
| Common | `product/common/code/` | Code tier |
| Structure | [`SYSTEM-DOC-STRUCTURE`](/platform/guide/SYSTEM-DOC-STRUCTURE) | Tree + standards |

## Pilot

- Context: `LND-base`, `CTX-admin` → [`03-context`](/architecture/03-context/)
- Building blocks: `CTR-admin-web`, `CTR-admin-api`, [CMP-01](/product/components/CMP-01-auth/)
- Journey: [`FLOW-login`](/architecture/06-runtime/journeys/FLOW-login)
- ADR: [ADR-001](/architecture/09-decisions/ADR-001-arc42-toc)

```bash
pnpm install
pnpm docs:dev
```

After the docs install profile generates the local harness, use **`/journey`**
for runtime journeys.
