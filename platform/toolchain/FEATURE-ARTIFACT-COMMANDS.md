# Feature artifact — lệnh script

> **R2/R3:** Product Code + architecture → [`base-docs`](../../base-docs/) · E2E plans → [`base-tests`](../../base-tests/) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> Bảng tra cứu · Diagram: [FEATURE-ARTIFACT-FLOWS](./FEATURE-ARTIFACT-FLOWS.md)  
> **Layout folder gen/registry (global):** [CODEGEN-LAYOUT](./CODEGEN-LAYOUT.md)  
> Codegen chi tiết tag/registry: [PORTAL-CODEGEN](./PORTAL-CODEGEN.md)

---

## Authoring & IR

| Lệnh | Input | Output / hiệu ứng |
|------|--------|-------------------|
| `pnpm spec:convert -- <legacy.spec.yaml>` | Spec cũ (one-off) | `yaml/.../{id}.bundle.yaml` |
| `pnpm spec:normalize-gen -- <bundle> --write` | Bundle trộn spec+gen | Tách `spec` design v1 ↔ `gen` |
| `pnpm spec:split -- <bundle.yaml>` | Bundle SSOT | `ir/spec.yaml`, `ir/legacy.yaml`, `ir/design.yaml` |
| `pnpm spec:merge -- <bundle.yaml>` | `ir/*` đã sửa tay | Cập nhật bundle (đặc biệt `gen`) |
| `pnpm spec:split:check -- <bundle.yaml>` | Bundle + ir | Exit 1 nếu lệch |
| `pnpm spec:split:all` | Mọi `yaml/**/*.bundle.yaml` | Quét thư mục, split + verify từng bundle |

---

## Common (shared) — tách khỏi features

Common component specs nằm ở `docs/common/yaml/{function}/`, dùng lại và ít thay đổi. **Không** chạy qua `portal:gen` / `docs:render` / `spec:split:all` của features — dùng lệnh riêng bên dưới.

| Lệnh | Mục đích |
|------|----------|
| `pnpm spec:split:common` | Split mọi `common/yaml/**/*.bundle.yaml` |
| `pnpm docs:render:common` | Render `common/yaml` → `common/md` (không ghi index features) |
| `pnpm portal:gen:dry:common` | Dry gen common (cần `codegen.profile` trong mỗi spec) |
| `pnpm portal:gen:common` | Gen common (cần `codegen.profile`) |



## Phase aggregates (1 lệnh/phase)

Lệnh tổng hợp chạy tuần tự các bước hạt nhân của mỗi phase. Lệnh hạt nhân ở các bảng trên **vẫn giữ nguyên** để tech review từng bước mà không phụ thuộc AI.

| Lệnh | Chạy tuần tự | Dùng sau |
|------|--------------|----------|
| `pnpm phase:spec -- <bundle.yaml>` | `spec:split` → `spec:split:check` → `docs:render` | Sửa 1 bundle xong |
| `pnpm phase:spec` (không arg) | `spec:split:all` → `docs:render` | Quét toàn bộ `yaml/**` |
| `pnpm phase:gen -- --spec <ir/spec.yaml>` | `portal:gen:dry` → `portal:gen` → `docs:render` | Dev-grill xong |
| `pnpm phase:unit -- --spec <ir/spec.yaml>` | `portal:unit-gen:dry` → `portal:unit-gen` | Gen xong |
| `pnpm phase:e2e -- <feature>` | `testcase:gen:dry` → `testcase:gen` → `test:e2e` | Testcase viết xong |
| `pnpm phase:common` | `spec:split:common` → `docs:render:common` | Common component specs |

> `docs:render` (render toàn bộ) và `test:e2e` (chạy toàn bộ spec) không nhận path arg — runner tự bỏ arg ở 2 bước đó. Runner: `scripts/run-phase.mjs`.

## Legacy dynamics

| Lệnh | Mục đích |
|------|----------|
| `pnpm legacy-dynamics:validate -- product/legacy-dynamics/…/_legacy.dynamics.yaml` | Schema + index/slice consistency (SSOT on docs hub) |

---

## Codegen — app (`portal:gen`)

**Input ưu tiên:** `pnpm portal:gen --id <W-|CMP-|CTR-…>` → Code trên [`base-docs`](../../base-docs/) (`ir/spec.yaml` sau `/dev-grill-docs`).

| Lệnh | Mục đích |
|------|----------|
| `pnpm portal:registry` | Validate design registry |
| `pnpm platform-common:registry` | Validate logic common registry |
| `pnpm portal:gen:dry --id W-AD-AUTH-001` | Gate sau dev-grill (không ghi file) |
| `pnpm portal:gen --id W-AD-AUTH-001` | Scaffold app + handoff |
| `pnpm portal:gen --id … --force` | Overwrite file đã gen |
| `pnpm portal:lifecycle sync` | Đồng bộ page registry |

V2 escape: `--spec <path-to-ir/spec.yaml>` vẫn chạy. Output app layers trên **FE repo**; handoff/manifest cạnh Code trên docs hub khi có.

## Unit tests (`portal:unit-gen`)

| Lệnh | Mục đích |
|------|----------|
| `pnpm portal:unit-registry` | Validate unit registry |
| `pnpm portal:unit-gen:dry --spec .../ir/spec.yaml` | Dry plan |
| `pnpm portal:unit-gen --spec .../ir/spec.yaml` | Smoke + `unit.manifest.json` |
| `pnpm portal:unit-gen --spec ... --phase wire` | Sau `/wire` |
| `pnpm exec vitest run tests/unit/...` | Scoped verify |

---

## E2E (`testcase:gen`)

**Plans SSOT:** [`base-tests`](../../base-tests/). **Output:** `tests/e2e/` trên FE.

| Lệnh | Mục đích |
|------|----------|
| `pnpm portal:e2e-registry` | Validate E2E registry |
| `pnpm testcase:gen:dry --id TC-LOGIN-VALID` | Dry một case |
| `pnpm testcase:gen --id W-AD-AUTH-001` | Mọi TC dưới screen |
| `pnpm testcase:gen --id smoke` | Suite pack |
| `pnpm test:e2e tests/e2e/...` | Chạy Playwright |

V2 escape: `--testcase <path>` / `--feature …`.

## Platform mark (`/platform-mark`)

Member marks common UI + logic — grill hỏi trước khi gắn tag. Hub: [PLATFORM-MARK](./PLATFORM-MARK.md)

| Lệnh / skill | Mục đích |
|--------------|----------|
| `/platform-mark` | Gắn `#needs-component`, `#common:*`, … vào `ir/spec.yaml` + registry |
| `/dev-grill-docs` | In bảng **Common candidates** — member A/B/C |
| `pnpm platform-common:registry` | Validate `registries/common.registry.json` |

---

## AI infra

| Lệnh | Mục đích |
|------|----------|
| `pnpm portal:gen --id <W-\|CMP-\|CTR-…>` | FE codegen from **base-docs** Code (`ir/spec.yaml` required) |
| `pnpm testcase:gen --id <W-\|TC-\|SC-\|suite\|CMP-…>` | E2E gen from **base-tests** plans → `tests/e2e/` |
| Root `platform-repos.json` | Cross-repo map — [PROJECT-MAPS](./PROJECT-MAPS.md) |
| `pnpm extracts:validate` | Skill `extractBundle` ⊆ registry |

---

## Ví dụ end-to-end (hotel-list)

```bash
# Sau dev-grill
pnpm spec:split -- <base-docs …/bundle.yaml>
pnpm portal:gen:dry --id W-AD-AUTH-001
pnpm portal:gen --id W-AD-AUTH-001
pnpm docs:render

pnpm portal:unit-gen --id W-AD-AUTH-001
pnpm testcase:gen --id W-AD-AUTH-001
```

Thứ tự team command: [DESIGN-PHASE-DIAGRAM](./DESIGN-PHASE-DIAGRAM.md) · [FEATURE-ARTIFACT-FLOWS](./FEATURE-ARTIFACT-FLOWS.md)
