# Fast codegen

> **R2/R3:** Product Code + architecture → [`base-docs`](../..) · E2E plans → [`base-tests`](https://github.com/raintr91/base_test) · gen: `pnpm portal:gen --id …` / `pnpm testcase:gen --id …` · [HUBS](./HUBS.md) / [DOCS-HUB](./DOCS-HUB.md) / [TESTS-HUB](./TESTS-HUB.md)


> **Python-native repo** — `uv`/`venv` + `./codegen/runners/generate` (Jinja2 + Typer).  
> **Không dùng pnpm** — spec split + codegen đều Python (`./scripts/spec-split`, `./codegen/runners/generate`).

## Commands

```bash
cd <fast-api-base-checkout>
python -m venv .venv && .venv/bin/pip install -e ".[dev]"

# Bundle → ir/{spec,legacy,design} + backend/01-backend-spec.yaml
./scripts/spec-split `base-docs` Product Code (prefer `--id`)
./scripts/spec-split-all
./scripts/docs-render

# Codegen (Python)
./codegen/runners/generate dry --spec `base-docs` Product Code (prefer `--id`)
./codegen/runners/generate write --spec `base-docs` Product Code (prefer `--id`)
./codegen/runners/generate openapi --spec `base-docs` Product Code (prefer `--id`)

# Hoặc Makefile
make spec-split-all SPEC=...   # xem Makefile
make docs-dev                  # MkDocs :8001
make test
```

## Feature layout

```text
`docs/features/` (stub only — SSOT on hubs) / 
  yaml/{domain}/{function}/
    {function}.bundle.yaml      # portal-feature-bundle/v1
    ir/spec.yaml · legacy.yaml · design.yaml
    backend/01-backend-spec.yaml
    backend/02-openapi.yaml
    {function}.api-test.yaml    # pytest contract (thay vitest)
    testcases/
    generated/
  md/{domain}/{function}/       # ./scripts/docs-render
```

Contract keys: portal `ir/spec.yaml` · `contractRef.portalIrSpec` in bundle.

Hub: [FEATURE-ARTIFACT-FLOWS](./FEATURE-ARTIFACT-FLOWS.md) · [FAST-ARTIFACT-COMMANDS](./FAST-ARTIFACT-COMMANDS.md) · portal [REPO-SPLIT-MAP](./REPO-SPLIT-MAP.md)
