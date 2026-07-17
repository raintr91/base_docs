# ArtifactGraph MCP (docs-hub guide)

Package / GitHub: **[raintr91/artifactgraph](https://github.com/raintr91/artifactgraph)**

**Chi tiết lệnh:** [ArtifactGraph `docs/INIT.md`](https://github.com/raintr91/artifactgraph/blob/main/docs/INIT.md).  
**Internals:** [ArtifactGraph `docs/INTERNALS.md`](https://github.com/raintr91/artifactgraph/blob/main/docs/INTERNALS.md).

## Bootstrap

| OS | Command |
|----|---------|
| **Linux / WSL** | `curl -fsSL https://raw.githubusercontent.com/raintr91/artifactgraph/main/install.sh \| bash` |
| **Windows** | `irm https://raw.githubusercontent.com/raintr91/artifactgraph/main/install.ps1 \| iex` |
| **npx** | `npx --yes github:raintr91/artifactgraph` |

```bash
artifactgraph version
# Run from this docs hub; init installs common + docs assets and local MCP wiring.
cd <base-docs-checkout>
artifactgraph init --target=cursor --type=docs --yes
artifactgraph rebuild
```

| Lệnh | Việc |
|------|------|
| `init` | Wire MCP + đồng bộ config, local lexicon và AG harness theo type |
| `init --type=docs --yes` | Cài `common` + `docs` không cần interactive selector |
| `init-project` | Alias tương thích đã deprecated; không dùng cho setup mới |
| `install` | Alias deprecated → `init` |

### Token / MCP

- **Project:** chạy `artifactgraph init` trên từng máy để sinh `.cursor/mcp.json` theo checkout hiện tại.
- MCP config là machine-local và bị gitignore; không commit executable path hoặc workspace path do installer sinh.
- **Global Win:** `%USERPROFILE%\.cursor\mcp.json` — giữ CodeGraph (nếu cần); **không** để `artifactgraph` ở đây.
- Skill/grill mới cần tools; ad-hoc dùng CLI:
  `artifactgraph parity|gaps|status|recommend-command|allowlist-check …`.
- ArtifactGraph chỉ recommend/check product-owned command. `artifactgraph gen`
  là compatibility shim deprecated trong 2.x; Bundlekit/Codegenkit/Testkit là
  executable owner.
- Rule `artifactgraph.mdc` = **opt-in** (`alwaysApply: false`), không inject mọi chat.

## Local-first (important)

| Local (MCP + member) | Cloud model |
|----------------------|-------------|
| Grill A/B/C: common vs feature-only | Implement Mo* / logic **chưa có** mẫu |
| Confirm blocks khi không clone legacy | Legacy symbol **chưa** có history |
| **Parity-drift** create≠edit / empty / FE≠BE | Cùng turn: trả `parityFindings[]` (schema) |
| gen allowlist + wire Mo* đã có registry | Chỉ `cloudPromptSlice` đã nén |

Detail: [ArtifactGraph `docs/INTERNALS.md`](https://github.com/raintr91/artifactgraph/blob/main/docs/INTERNALS.md) · extract `legacy/parity.md` · [ArtifactGraph `docs/PARITY.md`](https://github.com/raintr91/artifactgraph/blob/main/docs/PARITY.md)

## In this repo

- Harness installed from ArtifactGraph `2.0.0` with types `common` + `docs`
- MCP: member chạy `artifactgraph init --target=cursor --type=docs --yes` để wire checkout của mình
- Config: `artifactgraph.json` — product-owned allowlist SSOT (`commands`); docs hub typically keeps `commands: {}` until FE/kits wire keys
- Local index: `.artifactgraph/` (registries + lexicon only — **not** architecture MD)
- Architecture IDs / chapter graph → [HUBDOCS](./HUBDOCS.md)
- Command boundary → [ARTIFACTGRAPH-API-CONTRACT](./ARTIFACTGRAPH-API-CONTRACT.md)
- `platform-repos.json` is tooling inventory only; runtime resolves this repo directly.
- Lexicon local copy: `artifactgraph/lexicon/registry-tags.en.txt` (from package baseline)
- Detail: [ArtifactGraph `docs/INTERNALS.md`](https://github.com/raintr91/artifactgraph/blob/main/docs/INTERNALS.md)