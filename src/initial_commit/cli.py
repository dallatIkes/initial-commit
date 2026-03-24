"""
initial-commit CLI
Kickstart your projects: git init + Makefile generation
"""

import argparse
import importlib.resources
import os
import subprocess
import sys
from pathlib import Path


TEMPLATES_DIR = Path(__file__).parent / "templates"
EXTERNAL_TEMPLATES_DIR = "initial_commit_templates"


def find_template(name: str) -> Path | None:
    """
    Look for a template by name.
    Priority: external templates (in <cwd>/initial_commit_templates/) > internal templates.
    """
    # 1. External templates (user-defined, higher priority)
    external = Path.cwd() / EXTERNAL_TEMPLATES_DIR / name
    if external.is_file():
        return external

    # 2. Internal templates (bundled with the package)
    internal = TEMPLATES_DIR / name
    if internal.is_file():
        return internal

    return None


def cmd_git_init() -> None:
    """Run git init in the current directory."""
    git_dir = Path.cwd() / ".git"
    if git_dir.exists():
        print("⚠  Git repository already initialised in this directory.")
        return

    result = subprocess.run(["git", "init"], capture_output=True, text=True)
    if result.returncode == 0:
        print("✔  Git repository initialised.")
    else:
        print(f"✘  git init failed:\n{result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)


def cmd_generate_makefile(template_name: str) -> None:
    """Copy a template to Makefile in the current directory."""
    template_path = find_template(template_name)

    if template_path is None:
        available = list_available_templates()
        print(
            f"✘  Template '{template_name}' not found.\n"
            f"   Available templates: {', '.join(available) if available else 'none'}",
            file=sys.stderr,
        )
        sys.exit(1)

    makefile = Path.cwd() / "Makefile"
    makefile.write_text(template_path.read_text(encoding="utf-8"), encoding="utf-8")

    source_label = (
        "external"
        if (Path.cwd() / EXTERNAL_TEMPLATES_DIR / template_name).is_file()
        else "internal"
    )
    print(f"✔  Makefile generated from {source_label} template '{template_name}'.")


def list_available_templates() -> list[str]:
    """Return sorted list of all available template names (external first, then internal)."""
    names: set[str] = set()

    external_dir = Path.cwd() / EXTERNAL_TEMPLATES_DIR
    if external_dir.is_dir():
        names.update(p.name for p in external_dir.iterdir() if p.is_file())

    if TEMPLATES_DIR.is_dir():
        names.update(p.name for p in TEMPLATES_DIR.iterdir() if p.is_file())

    return sorted(names)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="initial-commit",
        description="Kickstart your projects: git init + Makefile generation",
    )
    parser.add_argument(
        "--git",
        action="store_true",
        help="Initialise a git repository in the current directory",
    )
    parser.add_argument(
        "--template",
        metavar="NAME",
        help="Generate a Makefile from a template (e.g. python.mk, node.mk)",
    )
    parser.add_argument(
        "--list-templates",
        action="store_true",
        help="List all available templates",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # Show help when called with no arguments
    if not any([args.git, args.template, args.list_templates]):
        parser.print_help()
        sys.exit(0)

    if args.list_templates:
        templates = list_available_templates()
        if templates:
            print("Available templates:")
            for t in templates:
                print(f"  • {t}")
        else:
            print("No templates found.")

    if args.git:
        cmd_git_init()

    if args.template:
        cmd_generate_makefile(args.template)


if __name__ == "__main__":
    main()
