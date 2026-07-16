# System doc structure — business tree + standards

How we **present** docs for one **system** (many surfaces: web, client, API) — not a single website sitemap.

**People entry:** [Start now](./start-now.md)  
**IDs / codegen stay:** `CMP-*` · `W-*` · `API-*` · `CTR-*` · `FLOW-*` (skills keep `/journey`, `/spec`, …)

---

## 1. Business tree (nav / mental model)

```text
overview/                         # hệ thống
surfaces/                         # kênh chạy (≠ tenant)
  flows/                          # optional — xuyên nhiều surface (*_flow / FLOW-*)
  web/
    flows/                        # optional — trong một app
    [role/…]                      # optional — chỉ khi dự án phân persona/role
      module-…/                   # năng lực = CMP
        functions/                # màn / API chi tiết
          …/
  client/
    …
  api/                            # nên có ngang web/client
    …
common/                           # UI chung · DB/DA wrapper — chỉ khi cần
architecture/
  01-introduction/                # sống
  07-deployment/                  # sống (stub-first topology)
  02…06, 08…12/                   # stub — team ít đụng
```

### Optional levels

| Tầng | Bắt buộc? | Khi nào có |
|------|-----------|------------|
| **role** | Không | Overview/dự án mô tả phân cấp persona → xen giữa surface và module; không thì surface → module |
| **flows** (`*_flow`) | Không | Chỉ chỗ cần (hệ hoặc trong một surface) |
| **common / DB** | Không | Shared UI hoặc data wrapper thật sự dùng chung |

### Vocabulary

| Từ | Nghĩa | Không nhầm với |
|----|--------|----------------|
| **Surface** | Kênh runtime: Admin web, Line client, API… | **Tenant** (đa thuê bao) — chỉ chú thích nếu team quen gọi tenant |
| **Module** | Năng lực nghiệp vụ (`CMP-*`) | Một folder Next.js |
| **Function** | Màn (`W-*`) hoặc API (`API-*`) trong module | Journey xuyên hệ |
| **Flow** | Câu chuyện curated (`FLOW-*` / `*_flow`) | Legacy `dynamics` (không dùng trên cây mới) |

---

## 2. Content standards by layer

| Layer | Pure text (why, scope, constraints) | Diagrams / DB / sequence |
|-------|--------------------------------------|---------------------------|
| **Overview · Common · Module trở lên** | **arc42** spirit (short sections — not all chapters 01–12) | **C4** (context, container, relations, ER, journey sequence) |
| **Function** (inside module) | **C4** code-level (screen/API behaviour) | **C4** only |

One line for the team:

> *Above module: words = arc42, pictures/DB/seq = C4. Inside a function: everything = C4.*

Prefer `flowchart` / `sequenceDiagram`. Avoid Mermaid `C4Context` in VitePress.

---

## 3. Map → technical SSOT (do not rename IDs)

| Business node | Technical home (today) | Skill |
|---------------|------------------------|-------|
| Overview | `architecture/03-context/` (`LND-*` `CTX-*`) + short §01 | `/architecture` → `/context` |
| Surfaces (web/client/api) | `architecture/05-building-blocks/` (`CTR-*`) | `/containers` |
| Module | `product/components/CMP-*/` | `/component` |
| Function (screen) | `CMP-*/code/W-*/` | `/spec` · grill |
| Function (API) | `CMP-*/code/API-*/` | `/spec` · grill |
| Flow | `architecture/06-runtime/journeys/FLOW-*.md` | **`/journey`** (not `/dynamics`) |
| Common / DB | `product/common/` · `product/shared/data-model/` | as needed |
| Intro | `architecture/01-introduction/` | `/architecture` |
| Deploy | `architecture/07-deployment/` | `/deployment` (stub-first) |

Nav uses business labels (VitePress **System** sidebar); **git paths and IDs stay** for codegen / grill / hubdocs. No physical `overview/` / `surfaces/` folders unless lead says nav is still confusing.

---

## 4. Architecture folder policy (thin for the team)

| Chapter | Status |
|---------|--------|
| `01` Introduction | **Active** — purpose / scope of this system docs |
| `07` Deployment | **Active** — stub unless placement matters |
| `02`–`06`, `08`–`12` | **Stub OK** — fill when lead needs; do not force every member |

C4 views that matter day-to-day still live under §03 / §05 / journeys — linked from **Start now** and module indexes, not by forcing the arc42 TOC on everyone.

---

## 5. Skills compliance (Layer rules)

Every architecture/product skill above **function** must:

1. Write **prose** in arc42 tone (intent, constraints, decisions) — no fake full 01–12 dump.  
2. Write **diagrams / DB / sequences** as C4 views.  
3. Never label new trees **dynamics**; use **flow** / `FLOW-*` / `/journey`.

**Function** skills (`/spec`, grill): C4 detail only — no new arc42 chapters for one screen.

Router: **`/architecture`** maps business ask → overview / surfaces / module / flow / deploy (see skill).

---

## 6. Pilot shape (Auth)

Business view:

```text
overview          → CTX-admin / LND-base
surfaces/web      → CTR-admin-web
surfaces/api      → CTR-admin-api
module Auth       → CMP-01-auth
  function login  → W-AD-AUTH-001 · API-AD-AUTH-001
flow (system)     → FLOW-login
```

---

## 7. Related

- [Start now](./start-now.md) — people entry by seat  
- Skills: `.cursor/skills/{architecture,context,containers,component,journey,spec,deployment}/`
