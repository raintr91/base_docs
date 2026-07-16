# Feature artifact — hub

SSOT: `base-docs Code / `--id``

```text
legacy source (external)
       ↓ legacy-spec
base-docs/product/legacy-dynamics/…/_legacy.dynamics.yaml + Code bundle.legacy
       ↓ pnpm spec:split
ir/{spec,legacy,design}.yaml
       ↓ dev-grill writes ir/spec (codegen)
portal:gen --id W-…
```

## One truth per concern

| Concern | File |
|---------|------|
| Legacy facts | `base-docs/product/legacy-dynamics/` + `ir/legacy.yaml` |
| Portal UI intent | `ir/design.yaml` |
| Codegen contract | `ir/spec.yaml` |
| BA prose | `bundle.review` → md |

Policy: `.cursor/rules/platform-ai.mdc` — feature docs = chuột bạch.

## Quy tắc chung (một concern = một nguồn)

| Concern | Nguồn | Không duplicate |
|---------|--------|-----------------|
| Legacy fact | `base-docs/product/legacy-dynamics/…/_legacy.dynamics.yaml` + `bundle.legacy` / `ir/legacy.yaml` | Không copy controller vào prose |
| Portal UI | `bundle.design` / `ir/design.yaml` | Không manifest riêng — chỉ design+zones |
| Codegen | `ir/spec.yaml` | Không đọc bundle/legacy trong portal:gen |
| BA prose | `bundle.review` → `md/` | Không prose trong `ir/*` |
| Agent policy | extract bundle theo command | Không load all extracts mọi phase |

**Cấm thêm:** `analysis.yaml`, `manifest.yaml`, `generation.yaml`, tag `#evidence:`.

**knowledge.level:** `observed` | `normalized` | `canonical` — không reuse `status: draft`.

**Pipeline:** `legacy-spec` | `/spec` → `bqa-grill` → `dev-grill` → [`grill-with-docs`] → `prototype`.

Flow hub: `base-docs/platform/toolchain/FEATURE-ARTIFACT-FLOWS.md` · `base-docs/platform/toolchain/FEATURE-ARTIFACT-COMMANDS.md`
