---
name: platform-ai
extractBundle: platform-ai
description: /platform-ai — maintain docs-hub AI harness; lanes vs plans/FE/BE.
disable-model-invocation: true
---

# /platform-ai — Docs hub harness (meta)

Chỉ sửa `.cursor/` / handbook pointers trên **base-docs**. Không nhồi FE/Plans/BE vào chat docs.

## Lanes (một chat = một lane)

| Lane | Repo | Skills |
|------|------|--------|
| **Docs** | **this** (`base-docs`) | `/architecture` (overview/surfaces/module/flow) `/context` `/containers` `/component` **`/journey`** `/deployment` `/cross-cutting` `/decision` **`/hubdocs`** · `/spec` `/legacy-spec` grill `/update-spec*` |

People entry: `platform/guide/start-now.md` · Doc tree: `platform/guide/SYSTEM-DOC-STRUCTURE.md`
| **Plans** | `base-tests` | `/testcase` `/grill-testcase` |
| **FE** | portal / FE bases | `/prototype` `/wire` `/test` `/unit` |
| **BE** | api / BE bases | `/api` |

Đừng luônApply Nuxt/E2E. Gen design scripts trên hub; Playwright gen trên FE đọc plans hub.

Flow: `platform/toolchain/FEATURE-ARTIFACT-FLOWS.md` · `TESTS-HUB.md` · router docs.

## Done

- [ ] Docs skills/extracts đúng hub paths
- [ ] Sync DNA từ portal không xóa docs-tier skills
