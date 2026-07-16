# 03 — Context

status: active

arc42 context + C4 **landscape / system context**. MD + Mermaid only. **No API schemas / UI DSL.**

IDs: `LND-*`, `CTX-*` (D3: landscape lives here, not under building-blocks).

## LND-base

Platform base cluster: FE bases, BE bases, docs hub, tests hub, MCP tooling.

```mermaid
flowchart LR
  subgraph people [People]
    BA[BA / Grill]
    Dev[Dev]
    QA[QA]
  end
  subgraph hubs [Hubs]
    Docs[base-docs]
    Tests[base-tests]
  end
  subgraph runtime [Runtime bases]
    FE[FE / client]
    BE[BE / API]
  end
  BA --> Docs
  Dev --> Docs
  Dev --> FE
  Dev --> BE
  QA --> Tests
  Tests -.->|refs W-* CMP-*| Docs
  FE -->|codegen from Code| Docs
```

## CTX-admin

Admin product boundary: authenticated operators manage tenant/platform data via Admin Web; Admin API is the system of record behind the FE.

```mermaid
flowchart LR
  Op[Admin operator]
  Admin[Admin product]
  IdP[IdP / session]
  Op -->|Uses| Admin
  Admin -->|Authenticates| IdP
```

Out of scope at this tier: endpoint lists (see `CTR-*-api` + `code/API-*`).

## See also

- [05 Building blocks](/architecture/05-building-blocks/)
- Redirect stubs: [`/architecture/landscape/`](/architecture/landscape/) · [`/architecture/context/`](/architecture/context/)
