# Platform & Legacy repo config (token-tight)

Hub: `platform/toolchain/PROJECT-MAPS.md` — portable path policy for agents.

## When to touch maps

| Need | Action |
|------|--------|
| Work only in **current** repo (same folder) | **Do not** Read `platform-repos.json` / `legacy-repos.json` |
| FE/BE/tooling repo | Handoff to that repo; do not resolve a sibling from this docs lane |
| Legacy archaeology (`/legacy-spec`, `/business-process-trace`) | Use explicit user path or resolve one entry from `legacy-repos.local.json` |
| List every base “for fun” | **Forbidden** — wastes tokens |

## Resolve order

```text
current docs repo → "."
legacy evidence → explicit user path → legacy-repos.local.json
```

Deprecated: `team-projects.json`, `legacy-projects.json`, `.cursor/*-projects*`.

## Progressive read (agents) — bắt buộc

1. Prefer **Grep/jq-style** extract over pasting whole file into chat:
   - Read only the requested `projects.<id>.root`.
2. **Never** dump full JSON into the reply or into cloud prompts.
3. If multiple ids match and no default: **ask** which id (one line).
4. Missing map / missing checkout: say cross-repo unavailable — **do not guess** absolute paths.
5. Optional accelerator: if ArtifactGraph is installed, use its compact project/status tools when available; otherwise stay on explicit path / `legacy-repos.local.json` (never invent a missing tool name).

## Output language

Vietnamese for member-facing docs; keep ids, roots, route/API keys, `data-testid` in English as in sources.
