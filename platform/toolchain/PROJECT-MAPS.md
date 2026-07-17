# Shared project maps

**SSOT at repo root** — không nhét riêng trong `.cursor/`.

| File | Mục đích |
|------|----------|
| [`platform-repos.example.json`](../../platform-repos.example.json) | Template — copy → `platform-repos.json` hoặc `platform-repos.local.json` |
| [`legacy-repos.example.json`](../../legacy-repos.example.json) | Template legacy checkouts |
| [`platform-repos.json`](../../platform-repos.json) | Live map (committed) — groups + contract FE↔BE |
| [`legacy-repos.json`](../../legacy-repos.json) | Legacy roots for `/legacy-spec` — **rỗng** trên cụm base |
| `platform-repos.local.json` | Machine override (gitignored) |
| `legacy-repos.local.json` | Machine override (gitignored) |

## Base cluster

Mỗi product base + MCP giữ **cùng catalog** `platform-bases`. Root relative tới repo đang mở (từ portal: siblings `../…`). Field `stack` dùng cho artifactgraph MCP (`nuxt4`, `nextjs`, `fastapi`, …).

| Key | Path (từ portal) | Role | stack |
|-----|------------------|------|-------|
| `portal` | `.` | Nuxt 4 FE | `nuxt4` |
| `nextjs` | `../nextjs` | Next.js FE | `nextjs` |
| `nuxt-nest` | `../nuxt_nest` | Nuxt 4 + NestJS | `nuxt4-nest` |
| `next-nest` | `../next_nest` | Next.js + NestJS | `nextjs-nest` |
| `fast-api-base` | `../fast-api-base` | FastAPI BE | `fastapi` |
| `api` | `../api` | Laravel 12 BE | `laravel` |
| `integration` | `../integration` | .NET BE | `dotnet-integration` |
| `line` | `../line` | WinForms (override `D:` trong `.local.json`) | `dotnet-line` |
| `base-docs` | `../base-docs` | Docs hub (R2 C4 + Code) | `docs-c4` |
| `base-tests` | `../base-tests` | Tests hub (R3 E2E plans) | `e2e-plans` |
| `artifactgraph` | `../artifactgraph` | MCP tooling (gaps/tags/gen) | `mcp` |
| `hubdocs` | `../hubdocs` | Optional MCP tooling (docs index) | `mcp-docs` |

**Đồng bộ map:** mỗi repo giữ `platform-repos.json` riêng; chỉnh tại chỗ hoặc theo quy trình team, không dùng script sync cross-base trong hub này.

Mỗi base giữ `.cursor/{skills,rules,extracts}` (SSOT).

## Resolve order (agents)

1. `{workspace}/platform-repos.local.json` / `legacy-repos.local.json`
2. `{workspace}/platform-repos.json` / `legacy-repos.json`
3. `{workspace}/platform-repos.example.json` / `legacy-repos.example.json` (template only)
4. Optional user home: `~/.cursor/platform-repos.json`

Never guess absolute paths. Extract: `.cursor/extracts/legacy/project-config.md` (**progressive read** — defaultGroup / one project / contract pair only; never paste full JSON into chat).

## Rename note (from older layout)

| Cũ | Mới |
|----|-----|
| `.cursor/team-projects.example.json` | `platform-repos.example.json` |
| `.cursor/legacy-projects.example.json` | `legacy-repos.example.json` |
| `team-projects.json` | `platform-repos.json` |
| `.kilo/config/team-projects.json` | `platform-repos.json` |

## Local override

```bash
cp platform-repos.example.json platform-repos.local.json
# edit roots for this machine
```
