# Split specs by child function

One bundle / `ir/spec.yaml` = **one child function** (list, create, update, …).

## Path layout (feature artifact)

```text
base-docs Code / `--id`
  {id}.bundle.yaml
  ir/spec.yaml
  ir/legacy.yaml
  ir/design.yaml
  {id}.test.yaml

base-docs Code / `--id`
```

## Rules

- Split: `list`, `detail`, `create`, `update`, `delete`, `login-as`, `import`, `export`, `setting`.
- Slug: role → domain → function (`hotel-list`, not `hotels-list`).
- Do not merge list + create + update in one bundle.
- Cross-module links: `openQuestions` or `review` notes only.
