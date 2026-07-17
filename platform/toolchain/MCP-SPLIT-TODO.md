# MCP split TODO — independent packages

> **Status:** Phases 0–6 shipped/verified; residual package hardening remains.  
> **Goal:** mỗi MCP cài độc lập; skill + script thuộc package owner; MCP phụ chỉ là accelerator (có thì gọi, không thì fallback model/local).  
> Related: [ARTIFACTGRAPH](./ARTIFACTGRAPH.md) · [HUBDOCS](./HUBDOCS.md) · [BUNDLEKIT](./BUNDLEKIT.md) · [PROCESSKIT](./PROCESSKIT.md) · [CODEGENKIT](./CODEGENKIT.md) · [TESTKIT](./TESTKIT.md) · [MCP-OWNERSHIP](./MCP-OWNERSHIP.md) · [MCP-INSTALL-PROFILES](./MCP-INSTALL-PROFILES.md) · [FEATURE-ARTIFACT-FLOWS](./FEATURE-ARTIFACT-FLOWS.md) · `/platform-ai`

## Current implementation status (2026-07-17)

| Phase | Status | Evidence / next gate |
|-------|--------|----------------------|
| Phase 0 — contracts/bootstrap | **Complete; Platform DNA 0.1.4 released** | `TI.1–TI.7`, `TC.1–TC.6`, `TG.1` closed. Resolver, portable maps, profile isolation, lifecycle and final meta checklist published. |
| Phase 1 — Bundlekit | **Released (0.1.3)** | Independent docs engines, lifecycle, compatibility and measured optional fallback contract |
| Phase 1B — Processkit | **Released (0.3.1)** | Process/impact tools, lifecycle, CodeGraph metric fixture and namespaced fallback schema |
| Phase 2 — ArtifactGraph cleanup | **Complete (2.0.1 release branch)** | Recommend/check boundary, safe lifecycle and contract-aligned legacy manifest migration |
| Phase 3 — Hubdocs audit | **Complete (1.0.2)** | Architecture ownership, safe lifecycle and namespaced ArtifactGraph fallback contract |
| Phase 4 — Codegenkit | **Released (0.3.2)** | FE+BE+fullstack engines, lifecycle and profile-safe optional fallback contract; residual `TKC.1`, `TKC.3–8`, `TKC.12` |
| Phase 5 — Testkit | **Released (0.2.1)** | Tests/FE profiles, lifecycle and shared namespaced optional fallback contract; residual `TKT.1`, `TKT.3–8` |
| Phase 6 — independence matrix | **Complete** | `T6.1–T6.8` closed with install, portability, lifecycle, compatibility and measured fallback fixtures |

**Bundlekit verification:** TypeScript build pass · CLI/engine/init smoke pass ·
initial `main` published to <https://github.com/raintr91/Bundlekit>.

**Processkit local verification:** TypeScript build pass · 9 tests pass,
including no-accelerator, CodeGraph-only and full-accelerator MCP config
preservation; idempotent fresh docs init passes. Initial `main` published to
<https://github.com/raintr91/Processkit>.

---

## Principles (locked)

1. **One skill → one package owner** (SSOT skill/extract/script trong MCP package; `init` sync ra repo đích).
2. **MCP độc lập:** thiếu MCP phụ **không** làm fail skill.
3. **Accelerator pattern:**

   ```text
   if tool_available(optional_mcp): call tool  # tiết kiệm token / tìm nhanh
   else: local Grep/Read / cloudPromptSlice
   ```

4. **MCP phụ hỗ trợ MCP/skill chính** — ví dụ Hubdocs index ID → path; ArtifactGraph index tag/registry → slice nhỏ.
5. **Không** hai package cùng sync một `SKILL.md`.
6. Docs hub **không** init codegenkit / testkit (FE/tests lane).
7. **Config maps cũng theo MCP:** schema + portable template sống trong package; `init` seed/sync ra repo đích. Path máy **không** commit — chỉ `*.local.json` (gitignore).
8. **Canonical process skill = `/business-process-trace`.** `/flow-trace` is a temporary deprecated redirect for one compatibility cycle. `/dynamics` remains Hubdocs→`/journey` only and must not be merged with process tracing.

### Accelerator examples

| Primary | Optional later MCP | Lợi ích nếu có |
|---------|-------------------|----------------|
| Architecture skills | Hubdocs | Resolve `CTX-*` / `CMP-*` → file nhanh |
| Bundle / grill skills | ArtifactGraph | Gaps/tags/parity slice thay vì đọc full registry |
| Legacy skills | CodeGraph | AST/call graph thay vì Grep mù |
| Grill / mark | Codegenkit (FE) | Dry-gen / registry validate executable |
| Spec / grill | Bundlekit tools | split/check/render deterministic |

---

## Install profiles by base type (proposed — freeze in Phase 0)

`--type` là **profile resolver**, không phải ánh xạ một-một package ↔ lane. Một package có thể hợp lệ ở nhiều base type; resolver chỉ cài/sync tập package và asset đúng repo đang mở.

| `init --type` | Required package set | Optional accelerators | Skills/lane |
|---------------|----------------------|-----------------------|-------------|
| `docs` | Hubdocs · Bundlekit · Processkit | ArtifactGraph · CodeGraph | Docs hub |
| `fe` | Codegenkit · Testkit · Processkit | ArtifactGraph · CodeGraph · Hubdocs | FE code |
| `be` | Codegenkit · Processkit | ArtifactGraph · CodeGraph · Hubdocs | BE code |
| `tests` | Testkit | ArtifactGraph | Plans hub |

> Không có profile `tooling`. Platform DNA **không** cài vào MCP package repos.

Rules:

1. Resolver phát hiện/nhận explicit `--type`; không suy diễn từ sibling checkout.
2. Mỗi package vẫn hỗ trợ init độc lập. Profile resolver chỉ điều phối required set, không tạo runtime dependency giữa các MCP.
3. `init --type=docs` không sync FE/BE/tests skills; `fe`/`be` không sync docs authoring family trừ skill shared được profile khai báo rõ.
4. Processkit là multi-lane: docs nhận `/business-process-trace` (+ deprecated `/flow-trace` redirect); FE/BE có thể nhận `/business-impact-review`; không bắt buộc sync cả hai skill vào mọi profile.
5. Testkit phải tách asset theo `tests` (`cases:render`, testcase authoring) và `fe` (E2E consumption/gen); không sync nguyên gói skill cho cả hai.
6. **Codegenkit is one package for FE + BE.** `init` chọn `--type=fe|be` (hoặc cả hai khi repo fullstack), rồi `--adapter` theo stack (`nuxt4`/`nextjs` · `fastapi`/`laravel`/…). Không tách Apikit riêng trừ khi lifecycle/schema thực sự không tái dùng được.

### Install-profile TODO

- [x] **TI.1** Owner = **Platform DNA** (`raintr91/platform-dna`): profile resolver + meta-harness/maps bootstrap.
- [x] **TI.2** `profiles.json` + `mcp-package.json`: supported types, required/optional packages, invocations, owned skills/rules/extracts and compatibility APIs.
- [x] **TI.3** Owner `/api` = **Codegenkit** multi-adapter (`--type=be --adapter=…`); không tạo MCP BE riêng mặc định.
- [x] **TI.4** Resolver invokes each package's profile subset; end-to-end fixtures prove Docs/FE/BE/Tests do not pull another lane's skills.
- [x] **TI.5** Fail fast on declared/detected lane and adapter mismatch; new empty bases require explicit `--force`.
- [x] **TI.6** Platform DNA: automated profile/map/isolation tests + end-to-end local package installs for `docs`, `fe`, `be`, `tests`; MCP tooling targets rejected (`mcp-package.json` / `role=tooling`).
- [x] **TI.7** MCP repositories own no `platform-repos*.json`; their local `/platform-ai` skill is dedicated to building/testing/releasing the independent MCP package.

---

## Ownership map

| Package | Skills sync (owner) | Primary tools / scripts | Optional accelerators |
|---------|---------------------|-------------------------|------------------------|
| **hubdocs** | `/architecture` `/context` `/containers` `/component` `/journey` `/deployment` `/decision` `/cross-cutting` `/hubdocs` | list/get/deps/orphans/links/route/journeys/layout | AG: tag hint nếu có |
| **bundlekit** ★ NEW | `/spec` `/update-spec` `/update-spec-legacy` `/legacy-spec` `/bqa-grill-docs` `/dev-grill-docs` `/grill-with-docs` | split/merge/check/normalize/render/legacy-validate + docs grill orchestration | Hubdocs · AG · CodeGraph |
| **processkit** ★ NEW | **`/business-process-trace`** · **`/business-impact-review`** (+ deprecated `/flow-trace`) | process-step validate · diff/symbol scope · review report schema | CodeGraph · Hubdocs · AG |
| **artifactgraph** | `/platform-mark` `/artifactgraph` | analyze/grill/parity/remember/gaps/tags + command recommend/allowlist check | Bundlekit · Codegenkit |
| **codegenkit** ★ NEW | FE: `/prototype` `/wire` `/unit` `/grill-*` · BE: `/api` (+ grill-api khi có) | FE portal/unit gen · BE api gen · registry validate | AG allowlist/tags |
| **testkit** ★ NEW | `/testcase` `/grill-testcase` `/test` `/grill-test` | cases:render · testcase:gen* | AG coverage gaps |
| **codegraph** | *(no docs skill sync)* | `codegraph_explore` | — |

`/platform-ai` = meta docs-hub harness — **không** thuộc tool package chuyên môn.

### Ownership gaps to close before moving files

Skills-only ownership is insufficient: an install also syncs rules, extracts, templates and thin command shims. Freeze these before implementation:

- [x] **TG.1 Bootstrap/DNA owner:** **Platform DNA** owns `/platform-ai` (docs), profile lane routers, portability invariant, profile resolver and common agent discipline.
- [x] **TG.2 Rules inventory:** one-owner map frozen in [MCP-OWNERSHIP](./MCP-OWNERSHIP.md).
- [x] **TG.3 Shared extracts inventory:** owner families + namespaced-snapshot rule frozen in [MCP-OWNERSHIP](./MCP-OWNERSHIP.md).
- [x] **TG.4 Grill-family boundary:** all three docs grill skills belong to Bundlekit; AG is optional accelerator.
- [x] **TG.5 Hard cross-calls:** dependency classes frozen in [MCP-OWNERSHIP](./MCP-OWNERSHIP.md).
- [x] **TG.6 Generator allowlist SSOT:** current product `artifactgraph.json`; AG recommends/checks, owning kit executes.
- [x] **TG.7 Lifecycle:** init/upgrade/prune/uninstall contract defined in [MCP-PACKAGE-CONTRACT](./MCP-PACKAGE-CONTRACT.md).
- [x] **TG.8 Compatibility:** package + install manifest API/version contract defined in [MCP-PACKAGE-CONTRACT](./MCP-PACKAGE-CONTRACT.md).
- [x] **TG.9 Alias lifecycle:** `/dynamics` stays Hubdocs-owned redirect to `/journey`; `/flow-trace` is Processkit-owned deprecated redirect to `/business-process-trace` for one compatibility cycle.

---

## Config maps (`platform-repos` / `legacy-repos`) — decision

Cùng pattern skill/script: **SSOT template trong MCP**, `init` sync ra repo. Không để member tự “đoán” shape JSON.

| File | Role | Owner (package) | Sync on `init` | Commit? |
|------|------|-----------------|----------------|---------|
| `platform-repos.example.json` | Portable template (docs / FE / BE profile) | Docs DNA: **Hubdocs** `init --type=docs` (seed); FE/BE: **codegenkit** / **testkit** theo lane | Seed if missing; `--force` overwrite template only | Yes (example) |
| `platform-repos.json` | Live map = **current repo only** (`root: "."` + `url`) | Seeded by lane `init`; harness `profiles.*.skills` **merged** by each MCP that syncs skills | Create if missing; merge skills list by package owner ids; never invent sibling `../` roots | Yes (portable) |
| `legacy-repos.example.json` | Empty shape for optional legacy evidence | **processkit** (+ Bundlekit consumers of `/legacy-spec`) | Seed if missing | Yes (example, empty projects) |
| `legacy-repos.json` | Committed empty / greenfield default | Same | Seed empty if missing | Yes (empty OK) |
| `legacy-repos.local.json` | Machine checkout roots | Member only | **Never** sync absolute paths from package | **No** (gitignore) |
| `platform-repos.local.json` | Machine override if ever needed | Member only | Never from package | **No** (gitignore) |

### Rules

1. Committed `platform-repos.json` **chỉ** mô tả repo đang mở (`root: "."`) + optional public `url`. Không `../portal`, `~/workspace`, `/home/...`, ổ đĩa.
2. `harness.profiles.<lane>.skills` là **union** các skill do MCP đã init trên repo đó (mỗi package append owned skills; không một file hardcode cả FE gen trong docs hub).
3. Legacy evidence path: user điền `legacy-repos.local.json`; skill `/legacy-spec` / `/business-process-trace` / `/business-impact-review` đọc local trước, example sau; **không đoán** sibling.
4. ArtifactGraph / Hubdocs / Processkit `init` **không** ghi đè `*.local.json`.
5. Khi nâng cấp package: cập nhật example/schema; merge skill ids; giữ `projects.base-docs` / product roots trừ `--force`.

### Init checklist (add to Phase 0 / 1 / 1B)

- [x] **TC.1** Platform DNA publishes JSON Schemas + package docs for `platform-repos` and `legacy-repos`.
- [x] **TC.2** Platform DNA docs bootstrap seeds portable `platform-repos.json` + example before specialist package merges.
- [x] **TC.3** Platform DNA/Processkit seed legacy example + empty map; `.local.json` paths are documented and gitignored.
- [x] **TC.4** End-to-end profile fixtures prove each MCP merges only owned skill IDs.
- [x] **TC.5** Platform DNA rejects sibling/home/drive/UNC paths in committed maps; local override files are excluded.
- [x] **TC.6** [PROJECT-MAPS](./PROJECT-MAPS.md) points to Platform DNA schemas/templates and executable validation/init.

---

## Cross-calls to clean (before / during split)

| Current overlap | Problem | Target |
|-----------------|---------|--------|
| `artifactgraph_gen genDry` ↔ `portal:gen:dry` | Hai owner cùng dry-gen | AG: recommend/allowlist only; Codegenkit: executable dry |
| `artifactgraph_gen registryValidate` ↔ `portal:registry` | Hai owner cùng validate | AG: semantic gaps/suggest; Codegenkit: schema validate |
| AG indexing architecture MD ↔ Hubdocs | Đụng docs graph | Architecture/MD → Hubdocs only; IR/registry → AG |
| CodeGraph vs AG on legacy | Dễ lẫn | CodeGraph = evidence; AG = parity/gap; Bundlekit = write/validate IR |
| AG-owned grill skill calls Bundlekit split/render | Nếu bắt buộc thì AG-only install không thể chạy đúng | Declare Bundlekit in `requires`, hoặc chuyển grill orchestrator về Bundlekit; không gọi đây là accelerator |
| `/architecture` routes to `/spec` | Cross-skill handoff khác runtime dependency | If Bundlekit absent, emit explicit handoff/install guidance; architecture authoring itself remains Hubdocs-only |
| `/flow-trace` tên mơ hồ | Không thể hiện brownfield business-process purpose | **Rename → `/business-process-trace`**; keep `/flow-trace` as temporary deprecated redirect; owner processkit |
| `/dynamics` là deprecated alias của `/journey` | Dễ bị hiểu nhầm là cùng `/flow-trace` | Hubdocs giữ redirect trong compatibility cycle rồi remove; **không gộp `/dynamics` với `/flow-trace`** |
| Legacy code change review chưa có package owner | Dễ chỉ xem diff cục bộ, bỏ sót process/caller/risk | **processkit** owns `/business-impact-review`: vertical process + horizontal callers + risk checklist |

---

## Flow trace + business impact review (decision)

**Owner package:** `processkit` — độc lập với Bundlekit, Hubdocs, ArtifactGraph và CodeGraph.

### Naming / migration

- Canonical skill: **`/business-process-trace`**.
- Existing `/flow-trace` is a thin deprecated redirect for one compatibility cycle, then remove.
- Extract SSOT: `business-process-trace.md`; `flow-trace.md` points at the canonical extract.
- `/dynamics` remains a deprecated redirect to `/journey` for product `FLOW-*`; it is unrelated to process tracing and must not be merged into Processkit.

| | `/business-process-trace` | `/journey` | `/legacy-spec` |
|--|---------------------------|------------|----------------|
| Purpose | Trace an observed cross-system business process in legacy/code | Curated product journey `FLOW-*` | Module IR archaeology |
| Output | Verified steps/evidence + process map; may seed a journey | `architecture/06-runtime/journeys/FLOW-*` | `product/legacy-dynamics/` + bundle |
| Primary owner | **processkit** | Hubdocs | Bundlekit |
| Accelerators | CodeGraph symbols/calls · Hubdocs ID→docs · AG tags/parity | Hubdocs | CodeGraph · AG |

### Skill 1 — `/business-process-trace`

Required workflow (model/skill works even with no optional MCP):

- Discover entrypoint(s): page/API/webhook/command/schedule/job.
- Trace steps: `page | api | call | persist | job | event | listener | command | mail`.
- Record system/repo, route/symbol, input/output, sync/async and evidence location per step.
- Mark unverified hops and process gaps; never invent missing calls.
- Handoff to `/journey` only for curated target documentation; handoff to `/legacy-spec` for module IR.

Optional accelerators:

```text
if CodeGraph available: symbol/caller/call-chain lookup
else: targeted Grep/Read; unresolved hop → compact cloudPromptSlice

if Hubdocs available: resolve CMP/CTR/FLOW IDs and doc paths
else: repository path conventions/search

if ArtifactGraph available: parity/tag slice when contract/registry is touched
else: model review from scoped evidence
```

Potential deterministic processkit tool (later): `business_process_validate` validates step vocabulary, required evidence and broken step references.

### Skill 2 — `/business-impact-review`

Trigger after a legacy code change/fix/refactor, especially public/protected method, route, Job/Event/Listener/Command/Schedule, auth/tenant, normalize/merge, delete/update, proxy/status or contract changes. **Read-only by default**; report findings + test plan, do not auto-fix.

#### Vertical — full business process

For every reachable entrypoint, trace as far as applicable:

```text
Client/FE or Scheduler/Webhook
  → route/command/job
  → auth + middleware + context injection/rewrite
  → controller/handler
  → service/domain
  → repository/model/database
  → event/listener/job/external API
  → response/error/status mapping
  → FE/consumer/next async hop
```

#### Horizontal — full changed-symbol blast radius

- All direct and indirect callers of changed class/function/method.
- Controllers, services, facades, helpers, traits, Jobs, Events, Listeners, Commands, Schedules.
- FE/API clients and external callers when route/response/status changes.
- Overrides/interfaces/implementations, factories/tests/fixtures and reflection/string dispatch where detectable.
- Follow one more hop beyond facade/dispatch/proxy; do not stop at the first caller.

#### Mandatory risk classes

Every review must evaluate:

- Null / missing relation / optional property access.
- Empty string/list/map; `whereIn([])`; accidental match-all; 404 vs empty semantics.
- Exception swallowing/collapsing; wrong HTTP/message mapping; proxy status mismatch.
- Hard-coded IDs/tenant/status/path/date; magic values/constants drift.
- AuthZ/IDOR and tenant context trust boundary.
- Request bag pollution / middleware `merge` / over-broad parse of `$request->all()`.
- Async context loss, retry/idempotency and partial side effects.
- Business-rule false positive/negative; delete/update/relation gates; soft delete.
- Transaction/data consistency and response/contract compatibility.

#### Required report

```text
Summary / ship recommendation
Changed symbols
Horizontal caller table
Vertical process paths
Findings: severity · class · evidence · impact · verify
Unsearched repos / residual risks
Targeted test plan
```

Optional accelerators:

- **CodeGraph:** changed symbols + callers + call graph (primary accelerator).
- **Hubdocs:** map process steps to CMP/CTR/FLOW docs.
- **ArtifactGraph:** affected tags/registries/parity.
- Missing accelerator never blocks review: targeted search then model analysis; explicitly report unsearched repo/symbol gaps.

### Processkit implementation TODO

- [x] **TP.1** Create processkit package with independent install/init.
- [x] **TP.2** Package owns/syncs `/business-process-trace`, `/business-impact-review`, templates and risk classes (+ deprecated `/flow-trace` redirect).
- [x] **TP.3** Inventory + rename in docs hub: canonical `/business-process-trace` + extract; `/flow-trace` kept as redirect for one cycle.
- [x] **TP.4** Add optional-tool detection; no hard dependency on CodeGraph/Hubdocs/AG.
- [x] **TP.5** Optional `business_process_validate` tool; avoid rebuilding a CodeGraph clone.
- [x] **TP.6** Smoke tests with no optional MCP, CodeGraph-only and full accelerators.

---

## Phase 0 — Contract (docs only)

- [x] **T0.1** Publish this file as SSOT plan; link từ toolchain index + handbook pointers ([BUNDLEKIT](./BUNDLEKIT.md) · [MCP-OWNERSHIP](./MCP-OWNERSHIP.md) · [MCP-INSTALL-PROFILES](./MCP-INSTALL-PROFILES.md)).
- [x] **T0.2** Freeze ownership table — see [MCP-OWNERSHIP](./MCP-OWNERSHIP.md); change needs explicit note.
- [x] **T0.3** Define skill section template `## Accelerators (optional)` — applied on Bundlekit-owned skills first; remaining skills follow on their package move.
- [x] **T0.4** AG API implemented: `artifactgraph_recommend_command` + `artifactgraph_allowlist_check`; executable `artifactgraph_gen` is a deprecated 2.x shim.
- [x] **T0.5** Package `requires` vs `optional` metadata for `init` (required = same package tools; optional = accelerators) — documented in ownership + Bundlekit skills.
- [x] **T0.6** Freeze config-map decision (section above) + TC.1 schema outline (portable root + harness skill merge).
- [x] **T0.7** Freeze install profiles matrix ([MCP-INSTALL-PROFILES](./MCP-INSTALL-PROFILES.md)); `/api` → Codegenkit and resolver/bootstrap → Platform DNA.
- [x] **T0.8** Freeze ownership for rules and shared extracts — [MCP-OWNERSHIP](./MCP-OWNERSHIP.md).
- [x] **T0.9** Grill family → Bundlekit; cross-calls classified in ownership contract.
- [x] **T0.10** Package uninstall/prune and skill↔tool compatibility policy — [MCP-PACKAGE-CONTRACT](./MCP-PACKAGE-CONTRACT.md).

**Exit:** ownership, profiles, AG API and lifecycle contracts published; Phase 0 complete.


---

## Phase 1 — `bundlekit` (docs hub, first implementation)

- [x] **T1.1** Create package repo/scaffold (`bundlekit`) mirroring hubdocs/AG install+init UX — local package sibling `bundlekit` (publish GitHub later).
- [x] **T1.2** Move engines from base-docs: copied into package `engines/` (`scripts/spec/*`, `scripts/docs/render*`, `legacy-dynamics-validate`). Hub keeps local fallback scripts until cutover.
- [x] **T1.3** MCP tools: `bundle_split` · `bundle_merge` · `bundle_check` · `bundle_normalize` · `bundle_split_all` · `docs_render` · `docs_render_common` · `legacy_dynamics_validate`.
- [x] **T1.4** Package owns + syncs skills: `/spec` `/update-spec*` `/legacy-spec` + all docs grill (`/bqa-grill-docs` `/dev-grill-docs` `/grill-with-docs`) + related extracts/rules.
- [x] **T1.4a** Bundlekit does **not** own business-process tracing or code-impact review; those belong to processkit.
- [x] **T1.5** Rewrite those skills: Bundlekit tools **required after bundlekit init**; Hubdocs/AG/CodeGraph **optional**.
- [x] **T1.6** `bundlekit init --type=docs`: wire Cursor MCP + sync harness.
- [x] **T1.6b** Merge Bundlekit-owned skill ids into `platform-repos.json` harness profile; do not rewrite project roots.
- [x] **T1.7** Machine-local MCP config via init; handbook states gitignore (no `/home/...` committed in package sources).
- [x] **T1.8** Handbook: [BUNDLEKIT](./BUNDLEKIT.md) + toolchain index / commands pointers.

**Exit:** docs hub member: install+init bundlekit (+ optional hubdocs/AG) → `/spec` chạy không cần sibling layout.


---

## Phase 1B — `processkit` (business process + legacy impact)

- [x] Complete **TP.1–TP.6** in the decision section above.
- [x] Rename to `/business-process-trace`; keep `/flow-trace` redirect; document that `/dynamics` → `/journey` only and is not a Processkit alias.
- [x] Port the existing shared impact-review vertical/horizontal/risk checklist into package SSOT.
- [x] **TC.3–TC.4** for processkit: seed legacy-repos example/empty + merge processkit skill ids; never touch `*.local.json`.

**Exit:** processkit alone can sync both skills and run model/search fallback; optional MCPs only accelerate.

---

## Phase 2 — Clean ArtifactGraph

- [x] **T2.1** Executable `artifactgraph_gen` deprecated as 2.x shim; recommend/check APIs implemented and tested.
- [x] **T2.2** Bundlekit-owned `/dev-grill-docs` `/grill-with-docs`: AG optional analyze/recommend; executable dry-gen is FE Codegenkit handoff only.
- [x] **T2.3** `/platform-mark`: AG suggest/remember + allowlist recommend; registry validate is FE Codegenkit handoff only.
- [x] **T2.4** Architecture Markdown graph stays Hubdocs; AG indexes registries/lexicon only (documented in [ARTIFACTGRAPH](./ARTIFACTGRAPH.md)).
- [x] **T2.5** Docs-hub handbook + `/artifactgraph` skill updated for thinner AG role (recommend/check; deprecated `artifactgraph_gen` shim).
- [x] **T2.6** Generator allowlist SSOT = current product `artifactgraph.json` `commands` (docs hub keeps `{}`); AG recommends, owning kit executes.

**Exit:** AG installable alone; grill skills degrade gracefully without codegenkit.

---

## Phase 3 — Hubdocs (independence check)

- [x] **T3.1** Audit architecture skills: Hubdocs already optional — tighten fallback wording.
- [x] **T3.2** Confirm no skill hard-requires AG inside Hubdocs-owned skills.
- [x] **T3.3** Document accelerator-only relationship AG ← Hubdocs (never reverse require).

**Exit:** Hubdocs-only checkout can author CTX/CTR/CMP/FLOW.

---

## Phase 4 — `codegenkit` (FE + BE, adapter-selected)

Decision (locked): one Codegenkit package owns code generation for both lanes.
`init` picks lane then stack:

```bash
codegenkit init --type=fe --adapter=nuxt4|nextjs …
codegenkit init --type=be --adapter=fastapi|laravel|… …
codegenkit init --type=fullstack --fe-adapter=nuxt4|nextjs --be-adapter=fastapi|laravel …
```

Docs hub still never gets Codegenkit by default.

- [x] **T4.1** Package: portal:gen* · unit-gen* · registry validates · related scripts.
- [x] **T4.2** Sync FE skills for `--type=fe`; **forbid** docs-hub init profile including codegenkit.
- [x] **T4.3** AG optional before gen (tags/allowlist) for token savings.
- [x] **T4.4** Docs skills that mentioned `portal:gen:dry` become handoff text or optional codegenkit call.
- [x] **T4.5a** FE adapters shipped: `nuxt4` / `nextjs` (reject `--type=docs`; BE belongs in the same package, not a separate MCP).
- [x] **T4.5b** Add BE profile + adapters (`fastapi` / `laravel`): sync `/api` + `/grill-api`, engines, and `--type=be` init (Codegenkit 0.2.0).
- [x] **T4.5c** Allow fullstack init (explicit FE+BE adapters) without pulling docs skills (Codegenkit 0.2.0).

**Exit:** FE + BE + explicit fullstack profiles ship; production BE engines,
unitgen and registry validation ship in Codegenkit 0.3.0.
Adapters: `nuxt4` / `nextjs` · `fastapi` / `laravel`. Hardening remains under
`TKC.*`.

---

## Phase 5 — `testkit` (tests / FE lane)

- [x] **T5.1** Package: `cases:render` · `testcase:gen*`.
- [x] **T5.2** Sync `/testcase` `/grill-testcase` `/test` on tests/FE bases only.
- [x] **T5.3** AG optional for coverage gaps.
- [x] **T5.4** Docs `/spec` handoff → tests hub URL / open tests workspace — no local sibling path (completed during Bundlekit harness cleanup).
- [x] **T5.5** Split Testkit sync manifest by `--type=tests` vs `--type=fe`; shared package does not imply identical skills/assets.

**Exit:** plans+E2E gen không giả định `../base-tests`. Initial `main` published
to <https://github.com/raintr91/Testkit>; hardening debt tracked as `TKT.*`.

---

## Phase 6 — Verify independence

- [x] **T6.1** Matrix installs: Hubdocs-only · Bundlekit-only · **Processkit-only** · AG-only · Hubdocs+Bundlekit · Processkit+CodeGraph · Hubdocs+Bundlekit+AG · full FE set. Seven clean temp-root installs pass; Processkit's offline CodeGraph configuration-preservation fixture proves the eighth without requiring a live server.
- [x] **T6.2** Each matrix: skill smoke does not require optional MCPs. Hubdocs 1.0.2, Bundlekit 0.1.3, Processkit 0.3.1, Codegenkit 0.3.3 and Testkit 0.2.4 ship package-owned namespaced event schemas/rules; fallback completes first, then emits once per run+optional with retry dedup and measured reads/bytes.
- [x] **T6.3** Measured context smoke: fixed Processkit CodeGraph fixture reads `2 files / 162 bytes` with accelerator vs `6 / 638` full fallback (74.61% fewer bytes); targeted fallback is `2 / 377` (57.03% fewer bytes). No estimated token claims.
- [x] **T6.4** Portability: committed maps contain current repo/lane only; sibling topology is member-local and ignored. `api@db925e6` and `base-tests@3f733d8` pass Platform DNA validation; Platform DNA 0.1.2 removes `tooling` from the map schema.
- [x] **T6.5** Platform DNA 0.1.4 and docs-hub `/platform-ai` Done checklists record ownership, lane isolation, portable maps, safe lifecycle and namespaced measured fallback contracts.
- [x] **T6.6** Lifecycle matrix: all owning packages now track managed hashes/stale assets and expose status + dry-run-by-default prune; `--yes` removes only unmodified stale assets. Shared maps/registries, product state, unmanaged files and local modifications are preserved. Covered by package lifecycle tests across Bundlekit, Hubdocs 1.0.1, Processkit 0.2.0, ArtifactGraph 2.0.0, Codegenkit 0.3.1, Testkit 0.2.0 and Platform DNA 0.1.3.
- [x] **T6.7** Compatibility tests cover every managed package manifest: supported `toolApi`/`harnessApi` pass; version drift warns; incompatible APIs fail before writes/deletes with actionable upgrade/re-init guidance. ArtifactGraph 2.0.1 also migrates its 2.0.0 legacy manifest; Bundlekit 0.1.2 adds fail-safe status/init/prune regression coverage.
- [x] **T6.8** Processkit 0.3.0 ships `missing-optional-event.schema.json`, run/optional dedup, exact `fileReads`/`contextBytes` measurement and a deterministic CodeGraph accelerator/fallback fixture.

**Exit:** “cài MCP lane là chạy” proven.

---

## Residual debt from Bundlekit migration audit

Captured from independence audit after Phase 1 scaffold. Track here; do not treat Phase 1 as fully closed until these are cleared or explicitly deferred.

- [x] **TB.1** Remove corrupted `base-docs Code / --id` placeholders from Bundlekit-owned `/update-spec` + `spec/split` + `common-ui-spec`.
- [x] **TB.2** `split-all` default root: `docs/features/yaml` → `product` (package + docs-hub fallback scripts).
- [x] **TB.3** Design-render testcase footer: no sibling `base-tests/` path; point to GitHub tests hub URL.
- [x] **TB.4** Drop `convert-spec-to-bundle` from Bundlekit package (legacy `docs/features` coupled; not in initial portable surface).
- [x] **TB.5** Remove hard reference to non-existent `artifactgraph_projects` from Bundlekit `legacy/project-config`.
- [x] **TB.6** Bundlekit copies classify `portal:gen` / testcase generation as FE/tests lifecycle handoffs; docs skills never execute them.
- [x] **TB.7** Bundlekit does not sync `team-flow-spec.mdc` / `team-flow-grill.mdc` wholesale; both remain out of package until TG.2/TG.4 resolves final ownership.
- [x] **TB.8** Obsolete converter quarantined at `scripts/legacy/convert-spec-to-bundle.mjs` and documented unsupported.
- [x] **TB.9** `yaml` promoted to docs-hub runtime dependency while fallback scripts remain.
- [x] **TB.10** Engine/install tests added: split/check/merge, legacy validate, managed-file conflict and extract-registry merge (7 tests total).
- [x] **TB.11** Publish `raintr91/Bundlekit` + install.sh from GitHub (`main` initial release).
- [x] **TB.12** Bundlekit init merges only owned bundle IDs into shared `extract-registry.json`; non-Bundlekit bundles are preserved and tested.
- [x] **TB.13** Bundlekit 0.1.1 uses namespaced snapshots for Platform DNA-owned `core/agent-discipline.md` and `legacy/project-config.md`; no shared-destination dual write. ([Inventory bootstrap ownership](da8b04cb-e41a-43ba-9b2e-3ff92ba9823e))

---

## Residual debt from Codegenkit source audit

Captured from [Discover Codegenkit sources](0cee841e-f7ae-4c62-aa02-a0467269bc42). Local package exists; these are hardening/cutover items.

- [x] **TKC.1** Installers pin immutable tag `v0.3.3` and enforce lockfiles (`pnpm --frozen-lockfile` / `npm ci`); override only via `CODEGENKIT_REF` / `-Ref`.
- [x] **TKC.2** Codegenkit 0.3.1 adds manifest-aware `status` and dry-run-by-default `prune --yes`; adapter/profile stale assets are tracked and locally modified files are preserved.
- [x] **TKC.3** Nuxt `nuxt_v_3@185377e` and Next `nextjs_v3@a346b7d` route `portal:gen*`, registry, unitgen and `gen:id` shims through Codegenkit; legacy hardcoded `portal:*:common` sibling paths were removed.
- [ ] **TKC.4** Seed FE `artifactgraph.json` allowlists so AG recommend/check can work.
- [x] **TKC.5** Codegenkit 0.3.3: Nuxt/Next `preferGenSpec()` / `--id` resolution require `ir/spec.yaml`; bundle YAML is refused with an actionable docs-hub IR error.
- [x] **TKC.6** Codegenkit 0.3.3 ships `schemas/common-registry.schema.json` plus CLI/MCP `common-registry` validation (Zod + alias integrity).
- [x] **TKC.7** Codegenkit 0.3.3 covers Nuxt+Next dry-run non-writing, adapter detect, `ir/spec.yaml` requirement, and common-registry validate happy/fail fixtures.
- [ ] **TKC.8** Resolve contested FE rules (`platform-invariants`, component-split, import-alias, …).
- [x] **TKC.9** Replace Laravel stub `apigen` with recovered module-first engine from `api@4bb1366` (`codegen/` + registries + unitgen); profile `modules-v1` only. Defer `api_v2` app-layer as later profile. Shipped in Codegenkit 0.3.0. ([Inventory Laravel adapter](521d527b-4929-4bb6-b970-82137beaa020))
- [x] **TKC.10** Laravel preflight: locate `artisan`/`composer.json` (root or `src/`), verify Laravel 12 + `nwidart/laravel-modules`, required Artisan commands, refuse unsupported layouts. Shipped in Codegenkit 0.3.0. ([Inventory Laravel adapter](521d527b-4929-4bb6-b970-82137beaa020))
- [x] **TKC.11** FastAPI: package `unitgen` + real registry validate entrypoints; seed target `registries/`; document Python runtime (`CODEGENKIT_PYTHON` → `.venv` → `python3` → `python`). Shipped in Codegenkit 0.3.0. ([Inventory FastAPI adapter](aa5385bf-4fe2-4263-b0f4-c63f6f80a972))
- [ ] **TKC.12** FastAPI remaining hardening: multi-entity generation and managed-hash ownership before `--force`. Identifier validation, field-typed schemas, CRUD store decoupling, route normalization and target containment shipped in 0.3.0. ([Inventory FastAPI adapter](aa5385bf-4fe2-4263-b0f4-c63f6f80a972))

---

## Residual debt from Testkit source audit

Captured from [Discover Testkit sources](baa41a12-f3c5-49ce-9801-2de8a79e66f6). Local package exists; `/grill-test` ownership is frozen.

- [x] **TKT.1** Installers pin immutable tag `v0.2.4` and enforce lockfiles (`pnpm --frozen-lockfile` / `npm ci`); override only via `TESTKIT_REF` / `-Ref`.
- [x] **TKT.2** Testkit 0.2.0 adds profile-aware `status` and dry-run-by-default `prune --yes`; tests↔FE stale assets are tracked and locally modified files are preserved.
- [x] **TKT.3** Testkit 0.2.2 preflights every generated E2E output (including dry-run): only lexical paths under `tests/e2e` are allowed; absolute/`..`/sibling-prefix and symlink ancestors/targets are rejected all-or-nothing.
- [x] **TKT.4** Testkit 0.2.3 drives `cases:check` through Ajv + package-owned `schemas/testcase.schema.json` (feature/capability/component-or-feature/a11y conditionals live in the schema; schema resolves from package root, not destination cwd).
- [x] **TKT.5** Testkit 0.2.4 resolves tests-only IDs without docs topology; missing optional docs `ir/spec.yaml` enrichment warns once per run and generation continues. Malformed testcase YAML/output failures remain fatal.
- [x] **TKT.6** Nuxt `nuxt_v_3@185377e` and Next `nextjs_v3@a346b7d` route testcase/e2e-registry shims through Testkit; tests hub `main@4d6a688` routes render/check/coverage through Testkit.
- [x] **TKT.7** Testkit 0.2.4 has deterministic goldens for cases render, local coverage happy/gap, generator output and cross-root portability (36 tests total).
- [x] **TKT.8** Testkit 0.2.4 removes package/runtime `../base-tests` / `../base-docs` assumptions and uses explicit docs/tests hub terminology and environment roots.

---

## Out of scope (this plan)

- Mermaid / Kroki MCP
- Structurizr MCP (later only if Hubdocs pain)
- Vendoring FE/BE product code into docs hub
- Splitting one skill into its own MCP package

---

## Suggested start order (historical) → remaining work

Original sequence (all package phases complete except Phase 6 verify):

1. ~~Phase 0 (contracts + Platform DNA bootstrap)~~  
2. ~~Phase 1 (`bundlekit`)~~  
3. ~~Phase 1B (`processkit`)~~  
4. ~~Phase 2 (AG cleanup)~~  
5. ~~Phase 3 (`hubdocs`)~~ — architecture ownership merged to `main`  
6. ~~Phase 4–5 (`codegenkit` / `testkit`)~~ — packages released; residual `TKC.*` / `TKT.*`  
7. Phase 6 (independence matrix `T6.1–T6.8`)

**Residual tracks outside the 1–7 package sequence:**

| Track | Why it matters | Open items |
|-------|----------------|------------|
| Platform DNA | Resolver/maps/meta harness released; lifecycle compatibility is verified in Phase 6 | — |
| Codegenkit harden | AG allowlists, contested FE rules, FastAPI multi-entity/`--force` hash | `TKC.4`, `TKC.8`, `TKC.12` |
| Testkit harden | All residual source-audit items released/cut over | — |

**Next recommended order:**

1. Seed FE ArtifactGraph allowlists (`TKC.4`).  
2. Contested FE rules (`TKC.8`) and FastAPI multi-entity/`--force` hash (`TKC.12`).

When an item is implemented, check it here and note package version / PR when
published. Local-only completion must be labelled explicitly; it is not a
release.
