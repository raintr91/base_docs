# Design phase — Pipeline cycle

> Chi tiết **Phase 1** · Overview màu: [FULL-CYCLE-PIPELINE-DIAGRAM](./FULL-CYCLE-PIPELINE-DIAGRAM.md) · Hub: [Toolchain index](./index.md)

Diagram tách nhỏ: [FEATURE-ARTIFACT-GRILL](./FEATURE-ARTIFACT-GRILL.md) · [FEATURE-ARTIFACT-BUNDLE-IR](./FEATURE-ARTIFACT-BUNDLE-IR.md)

Gam màu Design = **emerald** (khớp full-cycle). Architecture gate = **blue** (Phase 0).

---

## Architecture gate (Phase 0 — trước Design khi cần)

Chỉ khi **group / module boundary**, CTX/CTR mới, hoặc integrate hệ mới. Skip nếu CMP đã map `CTR-*`.

```mermaid
flowchart LR
  subgraph P0["0 Architecture"]
    direction TB
    NEED{"Boundary đổi?"}
    ARC["/architecture"]
    C4["/context · /containers · /decision"]
    FLOW["/journey nếu cross-system"]
    NEED -->|yes| ARC --> C4 --> FLOW
    NEED -->|no| SKIP["→ Design"]
  end

  classDef p0 fill:#DBEAFE,stroke:#1D4ED8,color:#1E3A8A
  classDef p0acc fill:#93C5FD,stroke:#1E40AF,color:#1E3A8A
  class NEED,ARC,C4,FLOW,SKIP p0
```

Skills: `/architecture` · `/hubdocs` (optional validate IDs). Journeys: `architecture/06-runtime/journeys/FLOW-*`.

---

## Design cycle (Phase 1)

```mermaid
flowchart TD
  subgraph IN["Entry"]
    LEG["/legacy-spec\ntrace + bundle"]
    SPEC["/spec\nspecOrigin: requirement"]
  end

  subgraph CORE["Bundle → grill → dry"]
    BUNDLE["*.bundle.yaml"]
    SPLIT["pnpm spec:split"]
    BQA["/bqa-grill-docs"]
    DEV["/dev-grill-docs\nbundle.gen"]
    DRY["portal:gen:dry\nir/spec.yaml"]
  end

  subgraph OUT["Prototype → scaffold handoff"]
    PR["/prototype"]
    GEN["portal:gen"]
    GP["/grill-prototype"]
    NEXT["Phase 2 Tests + API"]
  end

  GW["/grill-with-docs\noptional"]
  US["/update-spec"]

  LEG --> BUNDLE
  SPEC --> BUNDLE
  BUNDLE --> SPLIT --> BQA --> DEV --> DRY --> PR --> GEN --> GP --> NEXT
  DEV -.->|optional| GW --> DRY
  BQA -.->|gap| US
  DEV -.->|gap| US
  US --> BQA

  classDef entry fill:#A7F3D0,stroke:#047857,color:#064E3B
  classDef core fill:#D1FAE5,stroke:#059669,color:#064E3B
  classDef out fill:#ECFDF5,stroke:#10B981,color:#065F46
  classDef opt fill:#FEF3C7,stroke:#B45309,color:#78350F
  classDef gap fill:#FECDD3,stroke:#BE123C,color:#881337

  class LEG,SPEC entry
  class BUNDLE,SPLIT,BQA,DEV,DRY core
  class PR,GEN,GP,NEXT out
  class GW opt
  class US gap
```

Tint trong gam emerald: **Entry** đậm hơn · **Core** giữa · **Out** nhạt hơn · optional grill-with = amber (không phải bước default) · gap = rose.

---

## Ma trận lệnh

| Lệnh | Artifact |
|------|----------|
| `/architecture` … (Phase 0) | `architecture/**` CTX/CTR/ADR/`FLOW-*` — không bundle Code |
| `/legacy-spec` | `base-docs/product/legacy-dynamics/…/_legacy.dynamics.yaml` + Code bundle.legacy |
| `/spec` | bundle design v1, `specOrigin: requirement` |
| `/bqa-grill-docs` | design vs legacy ui vs common |
| `/dev-grill-docs` | `bundle.gen` → ir/spec codegen |
| `/grill-with-docs` | Reconcile — **không** default |
| `/prototype` | Chỉ đọc `ir/spec.yaml` |
| `pnpm docs:render` | bundle → `md/` |

## Lệnh script (design phase)

Xem [FEATURE-ARTIFACT-COMMANDS](./FEATURE-ARTIFACT-COMMANDS.md).

## Tag & gap (phase này)

| Doc | Khi nào đọc |
|-----|----------------|
| [TECH-DEBT-FLOW](./TECH-DEBT-FLOW.md) | Grill defer câu hỏi → `#tech-debt:{id}` · step 0 mỗi grill |
| [UPDATE-SPEC-FLOW](./UPDATE-SPEC-FLOW.md) | Gap sau grill/prototype → `#update:*` |
| [FEATURE-ARTIFACT-GRILL](./FEATURE-ARTIFACT-GRILL.md) | Chuỗi bqa → dev → dry |

Grill step 0 (nhẹ): CMP gắn `CTR-*` nào? Missing → Phase 0 `/containers` · `/component`, không bịa hierarchy trong bqa.

Sau `portal:gen:dry` pass → [Portal reference](https://github.com/raintr91/nuxt_4/blob/nuxt_v_3/docs/operational/PORTAL-CODEGEN.md) · [NEEDS-COMPONENT-FLOW](./NEEDS-COMPONENT-FLOW.md) (`#needs-component` trong `/prototype`).
