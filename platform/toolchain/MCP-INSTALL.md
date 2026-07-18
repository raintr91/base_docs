# MCP install catalog

Read this first, then install **only** the kits your lane needs. Every kit is an
independent MCP package: it installs, initializes, and runs on its own. No kit
hard-depends on another — cross-kit features are optional accelerators that
degrade gracefully when the other kit is absent.

- Ownership per kit: [MCP-OWNERSHIP](./MCP-OWNERSHIP.md)
- Convenience bundles per lane: [MCP-INSTALL-PROFILES](./MCP-INSTALL-PROFILES.md)
- A fresh clone has no skills/rules/maps until you init a kit.

## 1. Pick by capability

Install a kit only when you need its capability. This is a menu, not a
checklist.

| I want to… | Install kit | Lane |
|------------|-------------|------|
| Author/index arc42 + C4 architecture IDs | **hubdocs** | docs |
| Split/merge/render bundle IR + docs grill + legacy-spec | **bundlekit** | docs |
| Trace business processes / review change impact | **processkit** | docs · fe · be |
| Generate FE or BE code | **codegenkit** | fe · be |
| Author test plans / generate Playwright E2E | **testkit** | tests · fe |
| Suggest registry tags / gaps / gen allowlist | **artifactgraph** | any (accelerator) |
| Explore code structure / call graph | **codegraph** | any (accelerator) |
| Seed repo identity + lane router meta | **platform-dna** | any (bootstrap) |

## 2. Per-kit install (independent)

Each block is self-contained. Run it in the target repository root. `Node ≥ 22`.

### hubdocs — architecture/C4 ID index

```bash
curl -fsSL https://raw.githubusercontent.com/raintr91/hubdocs/main/install.sh | bash
hubdocs init --yes
```

Adds: `/architecture` `/context` `/containers` `/component` `/journey`
`/deployment` `/cross-cutting` `/decision` `/hubdocs` + docs ID/graph tools.
Optional accelerator: none required.

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
codegenkit init --type=fe --adapter=nuxt4 --docs-root=/path/to/docs-hub --yes
codegenkit init --type=be --adapter=fastapi --yes
```

Adapters: FE `nuxt4` `nextjs` `dotnet-line`; BE `fastapi` `laravel`
`dotnet-integration`. Adds FE `/prototype` `/wire` `/unit` `/model` (+ grills)
or BE `/api` (+ grill). Optional accelerator: artifactgraph (allowlist only).
Never installed in docs/tests.

### testkit — plans + Playwright gen

```bash
testkit init --type=tests --yes
testkit init --type=fe --tests-root=/path/to/tests-hub --docs-root=/path/to/docs-hub --yes
```

Adds: tests `/testcase` `/grill-testcase`; fe `/test` `/grill-test`. Optional
accelerator: artifactgraph.

### artifactgraph — registry tags / gaps (accelerator)

```bash
artifactgraph init --target=cursor --type=common,docs --yes   # or common,fe | common,be | common,test
```

Adds: `/artifactgraph` `/docs-mark` + analyze/parity/tag/gap tools. Pure
accelerator: no other kit requires it, and every consumer falls back to model
analysis without it.

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
below.

## 3. Independence contract

1. Each kit installs, inits, and runs **standalone**; installing one never
   requires another.
2. Cross-kit usage is an **optional accelerator** only. Missing accelerator →
   documented graceful fallback, never a hard failure.
3. Each kit owns its own skills, tools, rules, extracts, and
   `install-manifest.json`. Nothing is shared through a common map.
4. `platform-repos.json` carries repo identity only (Platform DNA owned); it is
   **not** a skill registry and is not read to decide what to install.
5. Uninstalling a kit removes only its owned files (`<kit> prune`).

## 4. Two install paths

**A. Per-kit (default).** Install exactly the kits from section 2 that you need.
This keeps a member checkout minimal — weight comes from synced `.cursor/` files,
so install less to stay light.

**B. Lane bootstrap (convenience).** `platform-dna init --type=<lane>` runs the
recommended kits for that lane in one shot. It is a convenience wrapper over the
same independent kits; the recommended set per lane lives in
[MCP-INSTALL-PROFILES](./MCP-INSTALL-PROFILES.md). Use `--dry-run` to preview,
`--with=<kit>` to add an optional accelerator, `--no-install` to require
preinstalled binaries.

> Bootstrap never couples kits at runtime; it only automates typing several
> independent `init` commands.
