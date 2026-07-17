# Feature artifact — flow index

> **R2/R3:** Product Code + architecture → [`base-docs`](../../base-docs/) · E2E plans → [`base-tests`](../../base-tests/) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> **R2/R3:** Product Code + architecture → [`base-docs`](../../base-docs/) · E2E plans → [`base-tests`](../../base-tests/) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> Hub diagram + lệnh script cho layout **yaml/md** mới.  
> Load policy: `.cursor/extracts/artifact-graph.md` · commands: [FEATURE-ARTIFACT-COMMANDS](./FEATURE-ARTIFACT-COMMANDS.md)

**Quy ước diagram:** mỗi file **một concern**, một Mermaid ngắn — không gộp toàn pipeline depth vào một diagram.
**Overview màu (phase gam):** [FULL-CYCLE-PIPELINE-DIAGRAM](./FULL-CYCLE-PIPELINE-DIAGRAM.md) · Design + Architecture gate: [DESIGN-PHASE-DIAGRAM](./DESIGN-PHASE-DIAGRAM.md).

---

## Layout & IR

| Doc | Nội dung |
|-----|----------|
| [FEATURE-ARTIFACT-LAYOUT](./FEATURE-ARTIFACT-LAYOUT.md) | Cây thư mục `yaml/` · `md/` · `ir/` · `generated/` |
| [CODEGEN-LAYOUT](./CODEGEN-LAYOUT.md) | Global `codegen/` · `unitgen/` · `registries/` (platform-bases) |
| [ARTIFACTGRAPH](./ARTIFACTGRAPH.md) | Local MCP gaps/tags/gen allowlist |
| [FEATURE-ARTIFACT-BUNDLE-IR](./FEATURE-ARTIFACT-BUNDLE-IR.md) | SSOT bundle → split/merge · `spec` vs `gen` |

## Team commands (AI)

| Doc | Nội dung |
|-----|----------|
| [FEATURE-ARTIFACT-LEGACY-DYNAMICS](./FEATURE-ARTIFACT-LEGACY-DYNAMICS.md) | `/legacy-spec` → trace + bundle.legacy |
| [FEATURE-ARTIFACT-GRILL](./FEATURE-ARTIFACT-GRILL.md) | `/bqa-grill-docs` → `/dev-grill-docs` → [`/grill-with-docs`] |
| [DESIGN-PHASE-DIAGRAM](./DESIGN-PHASE-DIAGRAM.md) | Design lane đến `/prototype` (+ Phase 0 Architecture gate) |
| [FULL-CYCLE-PIPELINE-DIAGRAM](./FULL-CYCLE-PIPELINE-DIAGRAM.md) | Overview màu toàn cycle (Phase 0…4) |
| [FEATURE-ARTIFACT-COMMANDS](./FEATURE-ARTIFACT-COMMANDS.md) | Lệnh `pnpm portal:*`, `spec:*`, `docs:render` |

## Pipeline tổng (các phase khác)

| Doc | Nội dung |
|-----|----------|
| [FULL-CYCLE-PIPELINE-DIAGRAM](./FULL-CYCLE-PIPELINE-DIAGRAM.md) | Overview màu Phase 0…4 |
| [TEST-PHASE-DIAGRAM](./TEST-PHASE-DIAGRAM.md) | E2E · `testcase:gen` |
| [UNIT-PHASE-DIAGRAM](./UNIT-PHASE-DIAGRAM.md) | Vitest · `portal:unit-gen` |
| [NEEDS-COMPONENT-FLOW](./NEEDS-COMPONENT-FLOW.md) | `#needs-component` gap loop |
| [NEEDS-TEST-FLOW](./NEEDS-TEST-FLOW.md) | needs-test gap loop |
| [NEEDS-UNIT-FLOW](./NEEDS-UNIT-FLOW.md) | `#needs-unit-test` gap loop |
| [BACKEND-PHASE-DIAGRAM](./BACKEND-PHASE-DIAGRAM.md) | API repo |
| [WIRE-PHASE-DIAGRAM](./WIRE-PHASE-DIAGRAM.md) | Integration |
| [UPDATE-SPEC-FLOW](./UPDATE-SPEC-FLOW.md) | Gap loop |

---

## Lệnh thường dùng (copy nhanh)

```bash
# Hubs
cd ../base-docs && pnpm docs:dev

# Codegen / E2E by id (from FE — portal / nextjs / …)
pnpm portal:gen:dry --id W-AD-AUTH-001
pnpm portal:gen --id W-AD-AUTH-001
pnpm testcase:gen:dry --id TC-LOGIN-VALID
pnpm testcase:gen --id W-AD-AUTH-001
pnpm testcase:gen --id smoke

# Common UI (vẫn trên FE docs/common)
pnpm phase:common
pnpm portal:gen:dry:common

pnpm extracts:validate
```

Pointers: [DOCS-HUB](./DOCS-HUB.md) · [TESTS-HUB](./TESTS-HUB.md) · [HUBS](./HUBS.md)

Chi tiết từng lệnh: [FEATURE-ARTIFACT-COMMANDS](./FEATURE-ARTIFACT-COMMANDS.md)
