# 05 — Building blocks

status: active

C4 **containers** + index of **components**. MD + Mermaid only.  
**SSOT for CMP + Code remains under `product/`** — do not duplicate `code/` here.

## CTR-admin-web

Admin SPA / Nuxt (or Next) client. Runs Playwright E2E; reads specs from docs hub Code tier.

## CTR-admin-api

Admin HTTP API. Owns auth session/token validation for admin actors.

```mermaid
flowchart TB
  Web[CTR-admin-web]
  Api[CTR-admin-api]
  Db[(DB)]
  Web -->|HTTPS JSON| Api
  Api --> Db
```

| Container | Role | Code refs |
|-----------|------|-----------|
| `CTR-admin-web` | FE | `W-AD-*` |
| `CTR-admin-api` | BE | `API-AD-*` |

## Components (index)

| ID | Name | Path |
|----|------|------|
| [CMP-01](/product/components/CMP-01-auth/) | Auth | `product/components/CMP-01-auth/` |

## See also

- [06 Runtime](/architecture/06-runtime/)
- Redirect: [`/architecture/containers/`](/architecture/containers/)
