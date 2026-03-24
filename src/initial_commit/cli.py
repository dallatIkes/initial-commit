"""
initial-commit CLI
Kickstart your projects: git init + Makefile generation
"""

import subprocess
import sys
from pathlib import Path

import questionary
from questionary import Style

# ── Paths ─────────────────────────────────────────────────────────────────────
TEMPLATES_DIR = Path(__file__).parent / "templates"
EXTERNAL_TEMPLATES_DIR = "initial_commit_templates"

# ── Style ─────────────────────────────────────────────────────────────────────
STYLE = Style([
    ("qmark",        "fg:#7c3aed bold"),
    ("question",     "bold"),
    ("answer",       "fg:#7c3aed bold"),
    ("pointer",      "fg:#7c3aed bold"),
    ("highlighted",  "fg:#7c3aed bold"),
    ("selected",     "fg:#7c3aed"),
    ("separator",    "fg:#444444"),
    ("instruction",  "fg:#888888"),
])


# ── Template helpers ───────────────────────────────────────────────────────────
def list_available_templates() -> list[str]:
    names: set[str] = set()
    external_dir = Path.cwd() / EXTERNAL_TEMPLATES_DIR
    if external_dir.is_dir():
        names.update(p.name for p in external_dir.iterdir() if p.is_file())
    if TEMPLATES_DIR.is_dir():
        names.update(p.name for p in TEMPLATES_DIR.iterdir() if p.is_file())
    return sorted(names)


def find_template(name: str) -> Path | None:
    external = Path.cwd() / EXTERNAL_TEMPLATES_DIR / name
    if external.is_file():
        return external
    internal = TEMPLATES_DIR / name
    if internal.is_file():
        return internal
    return None


# ── Actions ───────────────────────────────────────────────────────────────────
def cmd_git_init() -> None:
    git_dir = Path.cwd() / ".git"
    if git_dir.exists():
        print("⚠  Git repository already initialised in this directory.")
        return
    result = subprocess.run(["git", "init"], capture_output=True, text=True)
    if result.returncode == 0:
        print("✔  Git repository initialised.")
    else:
        print(f"✘  git init failed:\n{result.stderr.strip()}", file=sys.stderr)


def cmd_git_clone(url: str) -> Path | None:
    """Clone a repo and return the path to the cloned folder."""
    print(f"  Cloning {url} ...")
    result = subprocess.run(["git", "clone", url], text=True)
    if result.returncode == 0:
        folder_name = url.rstrip("/").split("/")[-1].removesuffix(".git")
        clone_dir = Path.cwd() / folder_name
        print(f"✔  Repository cloned into './{folder_name}'.")
        return clone_dir
    else:
        print("✘  git clone failed.", file=sys.stderr)
        return None


def cmd_generate_makefile(template_name: str, target_dir: Path | None = None) -> None:
    template_path = find_template(template_name)
    if template_path is None:
        print(f"✘  Template '{template_name}' not found.", file=sys.stderr)
        return
    dest = (target_dir or Path.cwd()) / "Makefile"
    dest.write_text(template_path.read_text(encoding="utf-8"), encoding="utf-8")
    source = "external" if (Path.cwd() / EXTERNAL_TEMPLATES_DIR / template_name).is_file() else "internal"
    print(f"✔  Makefile generated from {source} template '{template_name}'.")


# ── Interactive flow ───────────────────────────────────────────────────────────
def run_interactive() -> None:
    print()
    print("  \033[1m\033[35m✦ initial-commit\033[0m — project kickstart")
    print()

    # 1. Git action
    git_action = questionary.select(
        "Git setup:",
        choices=[
            questionary.Choice("Init a new repository",  value="init"),
            questionary.Choice("Clone an existing repo", value="clone"),
            questionary.Choice("Skip",                   value="skip"),
        ],
        style=STYLE,
    ).ask()

    if git_action is None:
        sys.exit(0)

    clone_url = None
    clone_dir = None

    if git_action == "clone":
        clone_url = questionary.text(
            "Repository URL:",
            validate=lambda v: True if v.strip() else "URL cannot be empty",
            style=STYLE,
        ).ask()

        if clone_url is None:
            sys.exit(0)

        clone_url = clone_url.strip()

    # 2. Generate a Makefile?
    want_makefile = questionary.confirm(
        "Generate a Makefile?",
        default=True,
        style=STYLE,
    ).ask()

    if want_makefile is None:
        sys.exit(0)

    # 3. Which template?
    template_choice = None
    if want_makefile:
        templates = list_available_templates()
        if not templates:
            print("⚠  No templates found — skipping Makefile generation.")
            want_makefile = False
        else:
            template_choice = questionary.select(
                "Choose a template:",
                choices=templates,
                style=STYLE,
            ).ask()

            if template_choice is None:
                sys.exit(0)

    # ── Run ───────────────────────────────────────────────────────────────────
    print()

    if git_action == "init":
        cmd_git_init()
    elif git_action == "clone" and clone_url:
        clone_dir = cmd_git_clone(clone_url)

    if want_makefile and template_choice:
        # For clone: drop the Makefile inside the cloned folder
        cmd_generate_makefile(template_choice, target_dir=clone_dir)

    print()


# ── Entry point ───────────────────────────────────────────────────────────────
def main() -> None:
    try:
        run_interactive()
    except KeyboardInterrupt:
        print("\n\n  Aborted.")
        sys.exit(0)


if __name__ == "__main__":
    main()