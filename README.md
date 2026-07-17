# base-docs

Platform **docs hub** (R2) — arc42 TOC + C4 views + product Code/common.

**Start now:** [`platform/guide/start-now.md`](./platform/guide/start-now.md) · Structure: [`SYSTEM-DOC-STRUCTURE.md`](./platform/guide/SYSTEM-DOC-STRUCTURE.md)

```bash
pnpm install
pnpm docs:dev
```

| Path | Role |
|------|------|
| `platform/` | Handbook |
| `architecture/01`…`12` | arc42 chapters (C4 IDs inside) |
| `architecture/06-runtime/journeys/` | `FLOW-*` curated sequences |
| `product/components/` | CMP-* + `code/W-*` / `code/API-*` |
| `product/common/code/` | Shared Code |
| `registries/docs-index.json` | Docs-side index (not FE codegen SSOT) |

Pilot: **CMP-01 Auth** · `W-AD-AUTH-001` · `API-AD-AUTH-001` · `FLOW-login`.

Maps: `platform-repos.json` (`role: docs`, `specRoots`).
