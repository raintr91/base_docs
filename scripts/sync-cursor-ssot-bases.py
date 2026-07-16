#!/usr/bin/env python3
"""Sync .cursor SSOT across platform-bases.

Sources:
  portal/.cursor  — CODE lane (prototype / api / gen / e2e / wire + DNA)
  base-docs/.cursor — DOCS lane (spec / legacy / grill / dynamics); not overwritten from portal wipe

Profiles:
  full   — FE: CODE_SKILLS only (prune docs-tier leftovers)
  shared — BE/tooling: DNA + api/wire/unit (no prototype/e2e unless present)
  docs   — skip skill overwrite from portal; prune code-only skills; keep docs SSOT
  tests  — e2e skills from portal CODE lane
"""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

PORTAL = Path("/home/vutv/workspace/portal")
WS = PORTAL.parent
SRC_CURSOR = PORTAL / ".cursor"
DOCS_CURSOR = WS / "base-docs" / ".cursor"

# Platform DNA on every base
DNA_SKILLS = (
    "platform-ai",
    "platform-base",
    "platform-mark",
    "artifactgraph",
)
# Docs hub keeps its own platform-ai (+ no Nuxt platform-base)
DNA_SKILLS_DOCS = (
    "platform-mark",
    "artifactgraph",
)
# FE/code lane — design leftover + implement
CODE_SKILLS = DNA_SKILLS + (
    "prototype",
    "grill-prototype",
    "api",
    "grill-api",
    "wire",
    "test",
    "grill-test",
    "unit",
    "grill-unit",
    "model",
)
# BE bases — no FE prototype/e2e required
SHARED_SKILLS = DNA_SKILLS + (
    "api",
    "grill-api",
    "wire",
    "unit",
    "grill-unit",
)
# Docs hub — authored on base-docs (not portal)
DOCS_SKILLS = DNA_SKILLS_DOCS + (
    "platform-ai",  # docs-local variant — not synced from portal
    "spec",
    "legacy-spec",
    "update-spec",
    "update-spec-legacy",
    "bqa-grill-docs",
    "dev-grill-docs",
    "grill-with-docs",
    "dynamics",
    "flow-trace",
)
TESTS_SKILLS = DNA_SKILLS + (
    "testcase",
    "grill-testcase",
)
# Skills that must NOT remain on code repos after sync
DOCS_ONLY_SKILLS = (
    "spec",
    "legacy-spec",
    "update-spec",
    "update-spec-legacy",
    "bqa-grill-docs",
    "dev-grill-docs",
    "grill-with-docs",
    "dynamics",
    "flow-trace",
    "testcase",
    "grill-testcase",
)

SHARED_RULES = (
    "platform-ai.mdc",
    "platform-contract-naming.mdc",
    "platform-code-size.mdc",
    "codegraph.mdc",
    "artifactgraph.mdc",
    "team-flow-router.mdc",
    "team-flow-harness-state.mdc",
)
CODE_RULES = SHARED_RULES + (
    "platform-invariants.mdc",
    "platform-base-data-layers.mdc",
    "platform-design-vocabulary.mdc",
    "platform-import-alias.mdc",
    "platform-component-split.mdc",
    "team-flow-prototype.mdc",
    "team-flow-unit.mdc",
    "team-flow-model.mdc",
    "team-flow-phase3-e2e.mdc",
    "team-flow-phase4-integration.mdc",
    "platform-base-e2e.mdc",
    "platform-base-ui-testid.mdc",
)
DOCS_ONLY_RULES = (
    "team-flow-spec.mdc",
    "team-flow-grill.mdc",
)
DOCS_RULES = tuple(
    r for r in SHARED_RULES if r != "platform-ai.mdc"
) + (
    "platform-ai.mdc",  # docs-local overlay preferred in sync_one
    "team-flow-spec.mdc",
    "team-flow-grill.mdc",
)
TESTS_RULES = (
    "platform-ai.mdc",
    "platform-contract-naming.mdc",
    "platform-code-size.mdc",
    "codegraph.mdc",
    "artifactgraph.mdc",
    "team-flow-harness-state.mdc",
    # team-flow-router.mdc — hub-local tests lane (not portal code router)
)
TESTS_EXTRACT_PATHS = (
    "core",
    "plans",
    "verify-gate.md",
    "platform-mark.md",
    "artifact-graph.md",
)
CODE_EXTRACT_PATHS = (
    "core",
    "legacy",  # thin project-config only on portal
    "codegen",
    "platform-mark.md",
    "platform-mark-detect.md",
    "platform-design-registry.md",
    "artifactgraph-phase-hooks.md",
    "artifact-graph.md",
    "test",
    "verify-gate.md",
    "wire",
    "portal-unit-workflow.md",
    "portal-unit-test-tags.md",
    "portal-unit-test-common.md",
)
SHARED_EXTRACT_PATHS = (
    "core",
    "legacy",
    "platform-mark.md",
    "platform-mark-detect.md",
    "artifactgraph-phase-hooks.md",
    "artifact-graph.md",
    "verify-gate.md",
    "wire",
)
DOCS_EXTRACT_PATHS = (
    "core",
    "legacy",
    "legacy-dynamics.md",
    "flow-trace.md",
    "spec",
    "grill",
    "common-ui-spec.md",
    "common-breadcrumb-flow.md",
    "common-delete-flow.md",
    "call-external.md",
    "cross-entity-service.md",
    "derived-data.md",
    "spec-incremental-blocks.md",
    "grill-tech-debt.md",
    "spec-update-delta.md",
    "spec-update-tags.md",
    "feature-lifecycle-status.md",
    "feature-artifact.md",
    "codegen",
    "platform-mark.md",
    "platform-mark-detect.md",
    "artifactgraph-phase-hooks.md",
    "artifact-graph.md",
)

# dirname under workspace → profile
PROFILES: dict[str, str] = {
    "nextjs": "full",
    "nuxt_nest": "full",
    "next_nest": "full",
    "fast-api-base": "shared",
    "api": "shared",
    "integration": "shared",
    "line": "shared",
    "base-docs": "docs",
    "base-tests": "tests",
    "artifactgraph": "shared",
}

SYNC_SCRIPTS = (
    "cursor-export-kilo",
    "platform-ai-link",
    "sync-cursor-ssot-bases.py",
    "sync-platform-repos-bases.py",
    "platform-workspace-from-repos.mjs",
)
MAP_FILES = (
    "platform-repos.example.json",
    "legacy-repos.example.json",
)

GITIGNORE_MIRROR_RE = re.compile(
    r"\n?# platform-ai-link mirror.*?(?=\n# |\nplatform-repos|\nlegacy-repos|\Z)",
    re.S,
)
GITIGNORE_CURSOR_SSOT = """
# Optional Kilo export (SSOT: .cursor/skills|rules|extracts — ./scripts/cursor-export-kilo)
.kilo/skills/
.kilo/instructions/
.kilo/extracts/
.kilo/command/
"""


def load_bases() -> list[str]:
    doc = json.loads((PORTAL / "platform-repos.json").read_text(encoding="utf-8"))
    group = doc["defaultGroup"]
    ids = doc["groups"][group]["projects"]
    out: list[str] = []
    for pid in ids:
        proj = doc["projects"][pid]
        root = proj["root"]
        if root in (".", "./"):
            continue  # portal
        # ../name → name
        name = Path(root).name
        if name and name not in out:
            out.append(name)
    return out


def rsync_tree(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def overlay_file(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() and src.resolve() == dst.resolve():
        return
    shutil.copy2(src, dst)


def sync_skills(src_skills: Path, dst_skills: Path, names: tuple[str, ...] | None) -> int:
    dst_skills.mkdir(parents=True, exist_ok=True)
    count = 0
    for child in sorted(src_skills.iterdir()):
        if not child.is_dir():
            continue
        if names is not None and child.name not in names:
            continue
        rsync_tree(child, dst_skills / child.name)
        count += 1
    return count


def sync_rules(src_rules: Path, dst_rules: Path, names: tuple[str, ...] | None) -> int:
    dst_rules.mkdir(parents=True, exist_ok=True)
    count = 0
    for child in sorted(src_rules.iterdir()):
        if not child.is_file():
            continue
        if names is not None and child.name not in names:
            continue
        overlay_file(child, dst_rules / child.name)
        count += 1
    return count


def sync_extracts_full(src: Path, dst: Path) -> int:
    """Overlay all portal extract files; keep sibling-only paths."""
    dst.mkdir(parents=True, exist_ok=True)
    n = 0
    for path in src.rglob("*"):
        if path.is_dir():
            continue
        rel = path.relative_to(src)
        overlay_file(path, dst / rel)
        n += 1
    return n


def sync_extracts_shared(src: Path, dst: Path, paths: tuple[str, ...] = SHARED_EXTRACT_PATHS) -> int:
    dst.mkdir(parents=True, exist_ok=True)
    n = 0
    for rel in paths:
        p = src / rel
        if not p.exists():
            continue
        if p.is_dir():
            for f in p.rglob("*"):
                if f.is_file():
                    overlay_file(f, dst / f.relative_to(src))
                    n += 1
        else:
            overlay_file(p, dst / rel)
            n += 1
    # Merge registry bundles we care about
    n += merge_registry_bundles(src / "extract-registry.json", dst / "extract-registry.json")
    return n


def merge_registry_bundles(src_reg: Path, dst_reg: Path) -> int:
    if not src_reg.exists():
        return 0
    src = json.loads(src_reg.read_text(encoding="utf-8"))
    if dst_reg.exists():
        dst = json.loads(dst_reg.read_text(encoding="utf-8"))
    else:
        dst = {"version": src.get("version", 1), "bundles": {}}
    dst.setdefault("bundles", {})
    keys = (
        "core",
        "prototype",
        "grill-prototype",
        "test",
        "grill-test",
        "unit",
        "grill-unit",
        "api",
        "grill-api",
        "wire",
        "model",
        "platform-ai",
        "platform-mark",
        "artifactgraph",
    )
    changed = 0
    for k in keys:
        if k in src.get("bundles", {}):
            dst["bundles"][k] = src["bundles"][k]
            changed += 1
    # Force .cursor/extracts/ paths (not platform-ai/)
    text = json.dumps(dst, indent=2, ensure_ascii=False) + "\n"
    text = text.replace("platform-ai/extracts/", ".cursor/extracts/")
    dst_reg.parent.mkdir(parents=True, exist_ok=True)
    dst_reg.write_text(text, encoding="utf-8")
    return changed


def retarget_platform_ai_paths(cursor: Path) -> int:
    n = 0
    for p in list(cursor.rglob("*.md")) + list(cursor.rglob("*.mdc")) + list(cursor.rglob("*.json")):
        t = p.read_text(encoding="utf-8")
        t2 = (
            t.replace("platform-ai/extracts/", ".cursor/extracts/")
            .replace("platform-ai/skills/", ".cursor/skills/")
            .replace("platform-ai/rules/", ".cursor/rules/")
        )
        if t2 != t:
            p.write_text(t2, encoding="utf-8")
            n += 1
    return n


def fix_gitignore(root: Path) -> bool:
    gi = root / ".gitignore"
    if not gi.exists():
        return False
    text = gi.read_text(encoding="utf-8")
    original = text
    if "platform-ai-link mirror" in text or ".cursor/skills/" in text:
        text2, n = GITIGNORE_MIRROR_RE.subn("\n" + GITIGNORE_CURSOR_SSOT.strip() + "\n", text)
        if n:
            text = text2
        else:
            # Fallback: strip cursor ignore lines individually
            lines = []
            skip_block = False
            for line in text.splitlines(keepends=True):
                if "platform-ai-link mirror" in line:
                    skip_block = True
                    continue
                if skip_block:
                    if line.startswith(".cursor/") or line.startswith(".kilo/"):
                        continue
                    if line.strip() == "":
                        continue
                    skip_block = False
                if line.strip() in {
                    ".cursor/skills/",
                    ".cursor/rules/",
                    ".cursor/extracts/",
                }:
                    continue
                lines.append(line)
            text = "".join(lines)
            if "# Optional Kilo export" not in text:
                text = text.rstrip() + "\n" + GITIGNORE_CURSOR_SSOT
    if text != original:
        gi.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
        return True
    # Ensure kilo block exists and cursor is NOT ignored
    if ".cursor/skills/" in text and "Optional Kilo export" not in text:
        text = text.replace(".cursor/skills/\n", "").replace(".cursor/rules/\n", "").replace(
            ".cursor/extracts/\n", ""
        )
        text = text.rstrip() + "\n" + GITIGNORE_CURSOR_SSOT
        gi.write_text(text, encoding="utf-8")
        return True
    return False


def copy_scripts(dest: Path) -> None:
    scripts = dest / "scripts"
    scripts.mkdir(parents=True, exist_ok=True)
    for name in SYNC_SCRIPTS:
        src = PORTAL / "scripts" / name
        if src.exists():
            shutil.copy2(src, scripts / name)
            if not name.endswith(".py") and not name.endswith(".mjs"):
                (scripts / name).chmod(0o755)
            else:
                (scripts / name).chmod(0o755)
    for name in MAP_FILES:
        src = PORTAL / name
        if src.exists():
            shutil.copy2(src, dest / name)
    obsolete = scripts / "platform-ai-migrate-to-ssot"
    if obsolete.exists():
        obsolete.unlink()


def remove_platform_ai_dir(dest: Path) -> bool:
    p = dest / "platform-ai"
    if p.is_dir():
        shutil.rmtree(p)
        return True
    return False


def prune_skills(dst_skills: Path, keep: tuple[str, ...]) -> int:
    if not dst_skills.is_dir():
        return 0
    n = 0
    keep_set = set(keep)
    for child in list(dst_skills.iterdir()):
        if child.is_dir() and child.name not in keep_set:
            shutil.rmtree(child)
            n += 1
    return n


def prune_rules(dst_rules: Path, keep: tuple[str, ...]) -> int:
    if not dst_rules.is_dir():
        return 0
    n = 0
    keep_set = set(keep)
    for child in list(dst_rules.iterdir()):
        if child.is_file() and child.suffix == ".mdc" and child.name not in keep_set:
            child.unlink()
            n += 1
    return n


def prune_extracts_allowlist(dst: Path, allowed: tuple[str, ...]) -> int:
    """Remove extract files/dirs not in allowlist (top-level names)."""
    if not dst.is_dir():
        return 0
    n = 0
    allow = set(allowed) | {"extract-registry.json"}
    for child in list(dst.iterdir()):
        name = child.name
        if name in allow:
            continue
        # allow nested under allowed dirs already synced
        if child.is_dir():
            shutil.rmtree(child)
            n += 1
        elif child.is_file():
            child.unlink()
            n += 1
    return n
    if not dst_skills.is_dir():
        return 0
    n = 0
    for name in DOCS_ONLY_SKILLS:
        p = dst_skills / name
        if p.is_dir():
            shutil.rmtree(p)
            n += 1
    return n


def prune_docs_only_from_code(dst_skills: Path) -> int:
    if not dst_skills.is_dir():
        return 0
    n = 0
    for name in DOCS_ONLY_SKILLS:
        p = dst_skills / name
        if p.is_dir():
            shutil.rmtree(p)
            n += 1
    return n


def skill_rule_for_profile(profile: str) -> tuple[tuple[str, ...] | None, tuple[str, ...] | None]:
    if profile == "full":
        return CODE_SKILLS, CODE_RULES
    if profile == "docs":
        return DOCS_SKILLS, DOCS_RULES
    if profile == "tests":
        return TESTS_SKILLS, TESTS_RULES
    return SHARED_SKILLS, SHARED_RULES


def sync_one(dirname: str, profile: str) -> None:
    dest = WS / dirname
    if not dest.is_dir():
        print(f"SKIP missing {dirname}")
        return
    cursor = dest / ".cursor"
    cursor.mkdir(parents=True, exist_ok=True)

    skill_names, rule_names = skill_rule_for_profile(profile)
    pruned = 0

    if profile == "docs":
        # DNA from portal; docs-tier skills stay on hub (or copied from hub for other docs clones)
        sk = sync_skills(SRC_CURSOR / "skills", cursor / "skills", DNA_SKILLS_DOCS)
        if dirname != "base-docs" and DOCS_CURSOR.is_dir():
            sk += sync_skills(DOCS_CURSOR / "skills", cursor / "skills", DOCS_SKILLS)
        # Ensure docs-local platform-ai stays (not overwritten by portal DNA)
        pruned = prune_skills(cursor / "skills", DOCS_SKILLS)
        ru = sync_rules(SRC_CURSOR / "rules", cursor / "rules", tuple(
            r for r in SHARED_RULES if r != "platform-ai.mdc"
        ))
        if (DOCS_CURSOR / "rules").is_dir():
            for name in ("team-flow-spec.mdc", "team-flow-grill.mdc", "team-flow-router.mdc", "platform-ai.mdc"):
                src_r = DOCS_CURSOR / "rules" / name
                if src_r.exists():
                    overlay_file(src_r, cursor / "rules" / name)
                    ru += 1
        ex = 0
        if (DOCS_CURSOR / "extracts").is_dir():
            ex = sync_extracts_shared(DOCS_CURSOR / "extracts", cursor / "extracts", DOCS_EXTRACT_PATHS)
            if (DOCS_CURSOR / "extracts" / "extract-registry.json").exists():
                overlay_file(
                    DOCS_CURSOR / "extracts" / "extract-registry.json",
                    cursor / "extracts" / "extract-registry.json",
                )
        else:
            ex = sync_extracts_shared(SRC_CURSOR / "extracts", cursor / "extracts", DOCS_EXTRACT_PATHS)
    elif profile == "tests":
        # DNA from portal; plans skills are hub-local (testcase / grill-testcase)
        sk = sync_skills(SRC_CURSOR / "skills", cursor / "skills", DNA_SKILLS)
        pruned = prune_skills(cursor / "skills", TESTS_SKILLS)
        ru = sync_rules(SRC_CURSOR / "rules", cursor / "rules", TESTS_RULES)
        for bad in (
            "team-flow-phase3-e2e.mdc",
            "platform-base-e2e.mdc",
            "platform-base-ui-testid.mdc",
            "team-flow-prototype.mdc",
        ):
            p = cursor / "rules" / bad
            if p.exists():
                p.unlink()
                pruned += 1
        # Do not overwrite hub tests-lane router with portal code router
        tests_router = WS / "base-tests" / ".cursor" / "rules" / "team-flow-router.mdc"
        if tests_router.exists():
            overlay_file(tests_router, cursor / "rules" / "team-flow-router.mdc")
            ru += 1
        hub_ex = WS / "base-tests" / ".cursor" / "extracts"
        if hub_ex.is_dir():
            ex = sync_extracts_shared(hub_ex, cursor / "extracts", TESTS_EXTRACT_PATHS)
        else:
            ex = 0
        pruned += prune_extracts_allowlist(cursor / "extracts", TESTS_EXTRACT_PATHS)
    else:
        sk = sync_skills(SRC_CURSOR / "skills", cursor / "skills", skill_names)
        pruned = prune_skills(cursor / "skills", skill_names or ())
        pruned += prune_docs_only_from_code(cursor / "skills")
        ru = sync_rules(SRC_CURSOR / "rules", cursor / "rules", rule_names)
        # Drop docs-only + unknown rules from code repos
        for bad in DOCS_ONLY_RULES:
            p = cursor / "rules" / bad
            if p.exists():
                p.unlink()
                pruned += 1
        if rule_names:
            pruned += prune_rules(cursor / "rules", rule_names)
        # Drop leftover codegen template under skills
        ref = cursor / "skills" / "platform-base" / "reference.md"
        if ref.exists():
            ref.unlink()
            pruned += 1
        if profile == "full":
            ex = sync_extracts_shared(SRC_CURSOR / "extracts", cursor / "extracts", CODE_EXTRACT_PATHS)
            if (SRC_CURSOR / "extracts" / "extract-registry.json").exists():
                overlay_file(
                    SRC_CURSOR / "extracts" / "extract-registry.json",
                    cursor / "extracts" / "extract-registry.json",
                )
            pruned += prune_extracts_allowlist(cursor / "extracts", CODE_EXTRACT_PATHS)
            # FE AGENTS.md
            agents = PORTAL / "AGENTS.md"
            if agents.exists():
                shutil.copy2(agents, dest / "AGENTS.md")
        else:
            ex = sync_extracts_shared(SRC_CURSOR / "extracts", cursor / "extracts", SHARED_EXTRACT_PATHS)
            pruned += prune_extracts_allowlist(cursor / "extracts", SHARED_EXTRACT_PATHS)

    patch = retarget_platform_ai_paths(cursor)
    gi = fix_gitignore(dest)
    copy_scripts(dest)
    removed = remove_platform_ai_dir(dest)

    if (dest / ".kilo").is_dir():
        export = dest / "scripts" / "cursor-export-kilo"
        if export.exists():
            import subprocess

            subprocess.run([str(export)], cwd=str(dest), check=False)

    print(
        f"OK {dirname} profile={profile} skills={sk} rules={ru} extracts~={ex} "
        f"prune={pruned} retarget={patch} gitignore={gi} rm_platform_ai={removed}"
    )


def main() -> None:
    bases = load_bases()
    print(f"Sync .cursor SSOT from portal → {len(bases)} bases")
    for dirname in bases:
        profile = PROFILES.get(dirname, "shared")
        sync_one(dirname, profile)
    print("Done.")


if __name__ == "__main__":
    main()
