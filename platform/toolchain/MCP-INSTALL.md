# MCP install catalog

Read this first, then install **only** the toolkits your lane needs. Every
toolkit is an independent MCP package: it installs, initializes, and runs on
its own. No toolkit hard-depends on another — cross-toolkit features are
optional accelerators that degrade gracefully when the other toolkit is absent.

**Speak:** destination hubs (`base-docs`, `portal`, …) are **repos**; MCP
packages (Hubdocs, Bundlekit, …) are **toolkits**. See [AGENTS.md](../../AGENTS.md).

- Ownership per toolkit: [MCP-OWNERSHIP](./MCP-OWNERSHIP.md)
- Convenience bundles per lane: [MCP-INSTALL-PROFILES](./MCP-INSTALL-PROFILES.md)
- A fresh clone has no skills/rules/maps until you init a toolkit.

## 1. Docs = registry hub (pointers elsewhere)

The **docs repo** is the only place that owns the full product registries,
architecture IDs, and bundle IR. Other repos (FE / BE / tests) do **not** copy
that data; they keep **machine-local pointers** to a docs checkout the member
chooses.

| From repo | Pointer (gitignored / MCP env) | Who consumes it |
|-----------|--------------------------------|-----------------|
| FE | `CODEGENKIT_DOCS_ROOT` (and `--docs-root` at init) | Codegenkit FE gen / IR read |
| FE (optional Hubdocs) | `HUBDOCS_ROOT` / `--docs-root` | Hubdocs ID→path tools |
| FE (Testkit E2E) | `TESTKIT_DOCS_ROOT` + `TESTKIT_TESTS_ROOT` | Testkit enrichment |
| BE / tests | same pattern when a toolkit needs docs | Never invent `../base-docs` |

Rules:

1. Pointers are **member-chosen absolute paths** on that machine. Never commit
   them; never infer sibling layout.
2. Registry / architecture **SSOT stays in the docs repo**. FE/BE toolkits read
   through the pointer; they do not vendor a second copy.
3. **ArtifactGraph belongs on docs by default** (full registries + parity). On
   FE/BE install it only when you truly need local tag/allowlist hints; it does
   not open the docs hub at runtime (standalone per repo). Prefer Codegenkit’s
   docs pointer for FE work that needs the full registry.

## 2. Pick by capability

Install a toolkit only when you need its capability. This is a menu, not a
checklist.

| I want to… | Install toolkit | Lane |
|------------|-----------------|------|
| Author/index arc42 + C4 architecture IDs | **hubdocs** | docs (home); optional on fe/be with `HUBDOCS_ROOT` → docs |
| Split/merge/render bundle IR + docs grill + legacy-spec | **bundlekit** | docs |
| Trace business processes / review change impact | **processkit** | docs · fe · be |
| Generate FE or BE code | **codegenkit** | fe · be (FE needs `CODEGENKIT_DOCS_ROOT`) |
| Author test plans / generate Playwright E2E | **testkit** | tests · fe |
| Suggest registry tags / gaps / gen allowlist | **artifactgraph** | **docs first**; fe/be/tests only if local hints needed |
| Explore code structure / call graph | **codegraph** | any (accelerator) |
| Seed repo identity + lane router meta | **platform-dna** | any (bootstrap) |

## 3. Per-toolkit install (independent)

Each block is self-contained. Run it in the target repository root. `Node ≥ 22`.

### hubdocs — architecture/C4 ID index

```bash
# On the docs repo (recommended home):
curl -fsSL https://raw.githubusercontent.com/raintr91/hubdocs/main/install.sh | bash
hubdocs init --yes
hubdocs harness install --type=docs

# From FE/BE (optional): wire tools to a docs checkout the member chooses
hubdocs init --docs-root=/absolute/path/to/docs-hub --yes
hubdocs harness install --type=consumer
```

Adds: `/architecture` `/context` `/containers` `/component` `/journey`
`/deployment` `/cross-cutting` `/decision` `/hubdocs` + docs ID/graph tools.
MCP env `HUBDOCS_ROOT` (or per-tool `docsRoot`) points at the docs hub; no
sibling path is assumed. Consumer mode syncs only `/hubdocs` + lightweight
rule/schema/hook — not the architecture authoring family.

### bundlekit — bundle IR + docs grill + legacy

```bash
curl -fsSL https://raw.githubusercontent.com/raintr91/bundlekit/main/install.sh | bash
bundlekit init --type=docs --target=cursor --yes
```

Adds: `/spec` `/update-spec` `/update-spec-legacy` `/legacy-spec`
`/bqa-grill-docs` `/dev-grill-docs` `/grill-with-docs` + split/merge/check/
render/legacy-validate tools. Owns the `pnpm spec:*` / `pnpm docs:render*`
aliases. Optional accelerators: artifactgraph (tags), hubdocs (ID→path),
codegraph (evidence) — all degrade gracefully.

### processkit — process trace + impact review

```bash
processkit init --type=docs --target=cursor --yes   # or --type=fe | --type=be
```

Adds: `/business-process-trace` `/business-impact-review` (+ deprecated
`/flow-trace` redirect) + process/impact validators. Optional accelerators:
codegraph, hubdocs, artifactgraph.

### codegenkit — FE/BE code generation

```bash
# FE always needs an explicit docs pointer (machine-local):
codegenkit init --type=fe --adapter=nuxt4 --docs-root=/absolute/path/to/docs-hub --yes
codegenkit init --type=be --adapter=fastapi --yes
```

Adapters: FE `nuxt4` `nextjs` `dotnet-line`; BE `fastapi` `laravel`
`dotnet-integration`. Adds FE `/prototype` `/wire` `/unit` `/model` (+ grills)
or BE `/api` (+ grill). Runtime reads IR/registries via `CODEGENKIT_DOCS_ROOT`
(set at init). Do **not** install ArtifactGraph on FE just to reach docs
registries — that pointer is Codegenkit’s job. Never installed in docs/tests.

### testkit — plans + Playwright gen

```bash
testkit init --type=tests --yes
testkit init --type=fe --tests-root=/path/to/tests-hub --docs-root=/path/to/docs-hub --yes
```

Adds: tests `/testcase` `/grill-testcase`; fe `/test` `/grill-test`. Optional
accelerator: artifactgraph — on the **tests hub** use `--type=common,test`
(testcase taxonomy + coverage hints on that repo's own plans); it never follows
`TESTKIT_DOCS_ROOT` / `TESTKIT_TESTS_ROOT` — cross-repo evidence flows through
the Testkit pointers.

### artifactgraph — registry tags / gaps (accelerator)

**Prefer the docs repo** — that is where full registries and parity live.

```bash
# Recommended: docs hub
cd /path/to/docs-hub
artifactgraph init --target=cursor --type=common,docs --yes
artifactgraph rebuild

# FE/BE/tests: only if you need local tag/allowlist hints on that repo’s own
# registries. ArtifactGraph does not follow HUBDOCS_ROOT / CODEGENKIT_DOCS_ROOT
# / TESTKIT_DOCS_ROOT.
artifactgraph init --target=cursor --type=common,fe --yes    # rare
artifactgraph init --target=cursor --type=common,test --yes  # tests hub (Testkit accelerator)
```

Adds: `/artifactgraph` `/docs-mark` + analyze/parity/tag/gap tools. Pure
accelerator: no other toolkit requires it. On non-docs repos it indexes **that
repo only** (packaged lexicon baseline + local `registries/`); it will not
silently open the docs hub.

### codegraph — code intelligence (accelerator)

```bash
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh
codegraph init
```

Adds: `codegraph_explore`. Local `.codegraph/` index, gitignored. Pure
accelerator.

### platform-dna — repo identity + lane router (bootstrap)

```bash
platform-dna init --type=docs --project-root=. --yes   # or fe | be | tests
```

Seeds portable `platform-repos.json` (repo identity), lane router meta, and
`/platform-ai`. Also the optional one-shot bootstrap for a whole lane — see
below. Use `--with=artifactgraph` on docs when you want the accelerator in the
bundle; do not treat that as a reason to install AG on every FE/BE checkout.

## 4. Independence contract

1. Each toolkit installs, inits, and runs **standalone**; installing one never
   requires another.
2. Cross-toolkit usage is an **optional accelerator** only. Missing accelerator →
   documented graceful fallback, never a hard failure.
3. Each toolkit owns its own skills, tools, rules, extracts, and
   `install-manifest.json`. Nothing is shared through a common map.
4. `platform-repos.json` carries repo identity only (Platform DNA owned); it is
   **not** a skill registry and is not read to decide what to install.
5. Cross-repo data access uses **explicit machine-local pointers**
   (`HUBDOCS_ROOT`, `CODEGENKIT_DOCS_ROOT`, …), never sibling inference.
6. Uninstalling a toolkit removes only its owned files (`<toolkit> prune`).

## 5. Two install paths

**A. Per-toolkit (default).** Install exactly the toolkits from section 3 that
you need. This keeps a member checkout minimal — weight comes from synced
`.cursor/` files, so install less to stay light.

**B. Lane bootstrap (convenience).** `platform-dna init --type=<lane>` runs the
recommended toolkits for that lane in one shot. It is a convenience wrapper over
the same independent toolkits; the recommended set per lane lives in
[MCP-INSTALL-PROFILES](./MCP-INSTALL-PROFILES.md). Use `--dry-run` to preview,
`--with=<toolkit>` to add an optional accelerator, `--no-install` to require
preinstalled binaries.

> Bootstrap never couples toolkits at runtime; it only automates typing several
> independent `init` commands.
