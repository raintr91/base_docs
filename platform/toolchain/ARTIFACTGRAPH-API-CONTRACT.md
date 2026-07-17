# ArtifactGraph API boundary

> Contract for the MCP split. ArtifactGraph analyzes/indexes/recommends;
> executable generators belong to lane kits.

## Command API

| API | Behavior | Owner |
|-----|----------|-------|
| `artifactgraph_recommend_command` | Check allowlist and materialize argv without execution | ArtifactGraph |
| `artifactgraph_allowlist_check` | Token-light membership + executable-owner result | ArtifactGraph |
| `artifactgraph_gen` | Deprecated executable compatibility shim | ArtifactGraph 2.x only |
| `bundle_*` / `docs_render*` | Execute bundle/docs transforms | Bundlekit |
| FE/BE generators and registry validators | Execute code generation/validation | Codegenkit or BE kit |
| testcase generation/render | Execute tests-lane generation | Testkit |

`artifactgraph_gen` remains for one compatibility major. Skills must stop
calling it before removal.

## Recommendation result

```json
{
  "ok": true,
  "commandKey": "genDry",
  "allowlisted": true,
  "knownKeys": ["genDry"],
  "argv": ["pnpm", "portal:gen:dry", "--spec", "…"],
  "cwd": "<current-repo>",
  "executableOwner": "codegenkit",
  "recommendation": "Execute with codegenkit; ArtifactGraph does not own this generator."
}
```

ArtifactGraph never creates a product allowlist from stack presets during
`init`. `artifactgraph.json` in the current product repository is SSOT.

## Compatibility

- 2.x: new recommend/check APIs + deprecated `artifactgraph_gen`.
- Next major: remove executable gen/registry validation after all skills use
  owning kits or explicit handoff.
- Missing owning kit is not an error for analysis: report the recommendation
  and handoff; do not execute a fallback shell command invented by the model.
