# System doc structure — Operating Model và Architecture

Cấu trúc tài liệu biểu diễn một hệ thống theo hai góc nhìn bổ trợ:

- **Business Operating Model:** actor nào vận hành hệ thống, thuộc operational area nào và sử dụng capability nào.
- **Technical Architecture:** runtime container nào triển khai capability và chúng giao tiếp với nhau như thế nào.

`Web`, `Client` và `API` là technical channel/container, không phải business operational area.

**People entry:** [Start now](./start-now.md)  
**IDs / codegen stay:** `CMP-*` · `W-*` · `API-*` · `CTR-*` · `FLOW-*`

---

## 1. Business operating model

```text
overview/                         # purpose, scope, actors, external systems
  operational-areas/              # Admin · Workforce · Shop-floor · Plant integration

surfaces/                         # bề mặt tương tác — không phải operational area
  common?/                        # scope toàn hệ thống — node động, ẩn khi rỗng
    flows/                        # FLOW-* dùng chung
    data-model/                   # DB / data
    integrations/                 # cross-service flow
  admin-web/                      # ví dụ một surface
    common?/                      # scope surface — node động
      flows/  data-model/  integrations/
    modules/                      # business capabilities = CMP-*
      common?/                    # scope module — node động
        flows/  data-model/  integrations/
      functions/                  # screen W-* / API contract API-*
  line-client-hmi/                # cùng cấu trúc common? → modules → functions
  integration-gateway/            # …

architecture/
  context/                        # actors + system boundary
  containers/                     # Portal, Client, API service, Gateway
  runtime/                        # curated FLOW-*
  deployment/                     # placement/topology
```

Đây là **logical navigation model**, không phải yêu cầu tạo các thư mục vật lý tương ứng. `common?` là node **động**: xuất hiện ở scope nào có artifact dùng chung (system / surface / module) và ẩn khi rỗng. Module giữ một SSOT dưới `product/components/`; surface và operational area liên kết tới Module thay vì sao chép Module; `FLOW-*` cũng giữ một SSOT dù được điều hướng qua nhiều node `common?`.

```mermaid
flowchart LR
  A["Actor / Persona"] --> O["Operational area"]
  O --> C["Interaction channel"]
  O --> S["Surface<br/>Admin Web · Line/HMI · Gateway"]
  S --> M["Module · CMP-*"]
  M --> F["Function"]
  F --> W["Screen · W-*"]
  F --> API["API contract · API-*"]
  S -. "scope: system / surface / module" .-> CO["Common? · dynamic<br/>FLOW-* · Data · Integrations"]
  M -. "scope: module" .-> CO

  classDef business fill:#DBEAFE,stroke:#1D4ED8,color:#1E3A8A
  classDef surface fill:#CFFAFE,stroke:#0E7490,color:#164E63
  classDef product fill:#D1FAE5,stroke:#047857,color:#064E3B
  classDef detail fill:#FEF3C7,stroke:#B45309,color:#78350F
  classDef flow fill:#EDE9FE,stroke:#6D28D9,color:#4C1D95
  class A,O,C business
  class S surface
  class M product
  class F,W,API detail
  class CO flow
```

Các quan hệ trong Operating Model là many-to-many:

- One persona may use several channels.
- One channel may serve several operational areas.
- One surface repeats the same `Common? → Modules → Functions` structure.
- One module may support Admin, Workforce, and Shop-floor without being duplicated.
- A Function may expose a screen, an API contract, or both.

### Vocabulary

| Term | Meaning | Do not confuse with |
|------|---------|---------------------|
| **Operational area** | Nhóm hoạt động nghiệp vụ: Admin, Workforce, Shop-floor, Plant Integration | Runtime container |
| **Persona / actor** | Người hoặc hệ thống thực hiện hoạt động: admin, worker, PLC… | Channel |
| **Interaction channel** | Điểm tương tác: Web Portal, Line Client, HMI, Gateway | Operational area |
| **Surface** | Bề mặt tương tác gom Module/Function: Admin Web, Line/HMI, Gateway | Operational area · Container |
| **Common** | Node động chứa artifact dùng chung (FLOW-*, data, integration) theo scope system/surface/module | Module riêng lẻ |
| **Module** | Năng lực nghiệp vụ (`CMP-*`) | Một folder framework |
| **Function** | Hành vi chi tiết; có màn (`W-*`), API contract (`API-*`), hoặc cả hai | API runtime service |
| **Container** | Runtime deployable/process: Portal, Line Client, Backend API, Integration Gateway | Operational area |
| **Flow** | Câu chuyện curated (`FLOW-*` / `*_flow`) | Legacy `dynamics` |

---

## 2. Quan hệ giữa Operating Model và C4 Architecture

```mermaid
flowchart TB
  subgraph Business["Business operating model"]
    OA["Operational areas<br/>Admin · Workforce · Shop-floor · Plant"]
    MOD["Modules · CMP-*"]
    FUN["Functions<br/>Screen W-* · API contract API-*"]
    OA --> MOD --> FUN
  end

  subgraph C4["Technical architecture"]
    CTX["System Context<br/>actors · external systems"]
    CTR["Containers<br/>Portal · Client · API service · Gateway"]
    CMP["Components<br/>runtime responsibilities"]
    CTX --> CTR --> CMP
  end

  OA -. "implemented by" .-> CTR
  MOD -. "allocated to" .-> CMP
  FUN -. "served through" .-> CTR
```

Thuật ngữ “API” xuất hiện ở hai cấp độ với ý nghĩa khác nhau:

- **Backend API service** là C4 Container (`CTR-*`).
- **API endpoint/contract** là Function detail (`API-*`), thường đi cùng màn hình nhưng cũng có thể phục vụ job, webhook, device và integration.

---

## 3. Content standards by layer

| Layer | Pure text (why, scope, constraints) | Diagrams / DB / sequence |
|-------|--------------------------------------|---------------------------|
| **Overview · Operational area · Common · Module+** | **arc42** spirit (short sections, not all chapters) | **C4** |
| **Function** | C4 code-level screen/API behaviour | **C4** only |

> Above Function: concise arc42 prose and C4 views. At Function detail: screen/API contracts and C4-level behaviour.

Prefer `flowchart` / `sequenceDiagram`. Avoid Mermaid `C4Context` in VitePress.

---

## 4. Map → technical SSOT

| Business/technical node | Technical home | Skill |
|-------------------------|----------------|-------|
| Overview | `architecture/03-context/` (`LND-*`, `CTX-*`) + short §01 | `/context` |
| Operational areas / personas | Context narrative + links to modules | `/context` |
| Runtime containers | `architecture/05-building-blocks/` (`CTR-*`) | `/containers` |
| Module | `product/components/CMP-*/` | `/component` |
| Function screen | `CMP-*/code/W-*/` | `/spec` · grill |
| Function API contract | `CMP-*/code/API-*/` | `/spec` · grill |
| Flow | `architecture/06-runtime/journeys/FLOW-*.md` | `/journey` |
| Common / DB | `product/common/` · `product/shared/data-model/` | as needed |
| Deployment | `architecture/07-deployment/` | `/deployment` |

Nav uses business labels; **git paths and IDs stay** for codegen, grill, and docskit. Do not create physical `operational-areas/` folders unless the product needs dedicated area pages.

---

## 5. Architecture folder policy

| Chapter | Status |
|---------|--------|
| `01` Introduction | Active — purpose and scope |
| `03` Context | Active — actors, operational areas, system boundary |
| `05` Building blocks | Active — C4 runtime containers + CMP index |
| `06` Runtime | Curated `FLOW-*` only |
| `07` Deployment | Active, stub-first unless placement matters |
| Other chapters | Stub OK; fill only when a real concern requires them |

---

## 6. Skills compliance

1. `/context` owns system scope, actors, personas, and operational areas.
2. `/containers` owns runtime Portal/Client/API/Gateway views, not business-area classification.
3. `/component` owns each module once and maps it to relevant areas and containers.
4. `/spec` owns Function detail: `W-*` and `API-*`.
5. `/journey` owns curated cross-area/module/container flows.
6. New docs use **flow**, never `dynamics`.

Router: `/architecture` maps an ask to context/operational area, containers, module, function, flow, or deployment.

---

## 7. Pilot shape — Auth

```text
overview                 → CTX-admin / LND-base
operational area         → Admin operations
persona + channel        → Admin operator + Web Portal
runtime containers       → CTR-admin-web · CTR-admin-api
module Auth              → CMP-01-auth
  function login         → W-AD-AUTH-001 · API-AD-AUTH-001
flow                     → FLOW-login
```

---

## 8. Related

- [Start now](./start-now.md) — onboarding and responsibility matrix
- Skills are toolkit-owned and generated locally under `.cursor/skills/` after
  installing the docs toolkits — see [Toolkits (MCP)](./toolkits.md).
