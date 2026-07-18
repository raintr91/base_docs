# MCP ownership freeze (Phase 0)

> Status: working freeze for implementation. Changes need an explicit note in
> [MCP-SPLIT-TODO](./MCP-SPLIT-TODO.md).

## Packages

| Package | Owns (skills) | Owns (tools) | Profiles |
|---------|---------------|--------------|----------|
| **hubdocs** | architecture family + `/hubdocs` + `/dynamics`→`/journey` redirect | docs ID/graph tools | `docs` |
| **bundlekit** | `/spec` `/update-spec` `/update-spec-legacy` `/legacy-spec` **all docs grill:** `/bqa-grill-docs` `/dev-grill-docs` `/grill-with-docs` | split/merge/check/render/legacy-validate + grill orchestration | `docs` |
| **processkit** | `/business-process-trace` `/business-impact-review` (`/flow-trace` deprecated alias) | process validate / impact report schema | `docs`, `fe`, `be` (subset) |
| **artifactgraph** | `/docs-mark` `/artifactgraph` (`/platform-mark` deprecated alias one cycle) | analyze/grill/parity/gaps/tags + command recommendation/allowlist check | `docs`, `fe`, `be`, `test` |
| **codegenkit** | FE: `/prototype` `/wire` `/unit` `/grill-prototype` `/grill-unit` `/model` (web FE only) · BE: `/api` (+ grill-api) | FE portal/unit gen · BE api gen · registry validate | `fe`, `be` (adapter-selected) |
| **testkit** | `/testcase` `/grill-testcase` `/test` `/grill-test` | cases:render · testcase:gen* | `tests`, `fe` |
| **codegraph** | *(no skill sync)* | explore/call graph | any (accelerator) |
| **platform-dna** | `/platform-ai` (docs only) · FE `/platform-base` (`nuxt4`/`nextjs` adapters) · lane router rules | executable profile resolver + portable map bootstrap | `docs`, `fe`, `be`, `tests` (never MCP tooling repos) |

Product-owned (not MCP-synced): code-lane `/platform-ai` (per-repo harness meta).

## Hard rules

1. One destination `SKILL.md` / rule / extract path → one package owner.
2. Shared extracts: one owner; consumers reference or receive versioned copies.
3. Cross-package deterministic steps → `requires`. Lookup/token helpers → `optional`.
4. Canonical process skill is `/business-process-trace`; `/flow-trace` is a temporary deprecated redirect. `/dynamics` is Hubdocs→`/journey` only.
5. Docs hub never inits codegenkit/testkit by default.

## Rule ownership

| Rule | Owner | Notes |
|------|-------|-------|
| `platform-ai.mdc` | **Platform DNA** | Profile-specific lane boundary + portability |
| `team-flow-router.mdc` | **Platform DNA** | Routes to installed skills only |
| `team-flow-harness-state.mdc` | **Platform DNA** | Shared harness protocol |
| `platform-contract-naming.mdc` | **Platform DNA** | Cross-package naming contract |
| `team-flow-spec.mdc` | **Bundlekit** | Spec + all docs grill orchestration |
| `team-flow-grill.mdc` | **Bundlekit** | Grill metadata shared by all three grill skills |
| `platform-code-size.mdc` | **Codegenkit** | Adapter-neutral FE code-generation concern; never installed in docs |
| `platform-design-vocabulary.mdc` | **Codegenkit** | Registry-backed vocabulary; adapter/product names remain registry data |
| `team-flow-prototype.mdc`, `team-flow-unit.mdc` | **Codegenkit** | FE generation lifecycle; adapter-neutral package rules |
| `codegenkit-optional-integrations.mdc` | **Codegenkit** | Optional accelerator fallback contract |
| `platform-invariants.mdc` | **Product repo** | Stack-specific; Nuxt and Next author separate variants |
| `platform-component-split.mdc` | **Product repo** | Route/component layout differs by stack |
| `platform-import-alias.mdc` | **Product repo** | Must match the product `tsconfig`/framework |
| `artifactgraph.mdc` | ArtifactGraph | Opt-in accelerator rule |
| `codegraph.mdc` | CodeGraph integration/bootstrap | Opt-in accelerator rule |

Platform DNA and Codegenkit destinations are install-manifest managed. Product
repos may commit the installed copies, but must not hand-fork package-owned
content. Product-owned rules are deliberately excluded from package harnesses.

## Extract ownership

| Extract family | Owner |
|----------------|-------|
| `architecture-core.md`, `tpl-arc42-*`, `tpl-{component,journey,deployment,adr,cross-cutting}.md` | Hubdocs |
| `spec/*`, `spec-update-*`, `spec-incremental-*`, `grill/*`, `grill-tech-debt.md`, `common-ui-spec.md`, `legacy-dynamics.md` | **Bundlekit** |
| `business-process-trace.md`, Processkit risk/process templates | Processkit |
| `artifactgraph-*`, `docs-mark*`, codegen readiness/tag analysis used by `/docs-mark` | ArtifactGraph |
| `core/agent-discipline.md`, portable repo-map policy/schemas | **Platform DNA** |

Existing package namespaced snapshots remain compatibility assets; Platform DNA
now owns the shared destination and must not overwrite a locally customized
file without explicit `--force`.

## Grill boundary (frozen)

Bundlekit owns all docs grill skills because they mutate/reconcile bundle IR and
must run independently of ArtifactGraph:

```text
/bqa-grill-docs → /dev-grill-docs → /grill-with-docs
       owner: Bundlekit (model + bundle tools)
       optional: ArtifactGraph analyze/parity/tag hints
       handoff: Codegenkit dry-run on FE, never a docs-hub fallback shell
```

ArtifactGraph remains a read/analyze/recommend accelerator. Codegenkit owns
executable dry-gen and registry validation. Therefore no grill skill
hard-requires ArtifactGraph or Codegenkit.

## Cross-package dependency classification

| Caller | Target | Class |
|--------|--------|-------|
| Bundlekit grill | ArtifactGraph gaps/parity/tags | `optional` |
| Bundlekit legacy | CodeGraph evidence | `optional` |
| Bundlekit spec | Hubdocs ID→path | `optional` |
| Docs grill | Codegenkit dry-gen | handoff, not runtime dependency |
| ArtifactGraph command recommendation | Bundle/Codegen/Test executors | handoff, not runtime dependency |
| Hubdocs architecture → `/spec` | Bundlekit | user-level handoff; Hubdocs authoring still works alone |

## Install profiles

See [MCP-INSTALL-PROFILES](./MCP-INSTALL-PROFILES.md).
