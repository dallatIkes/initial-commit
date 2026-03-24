# initial-commit

> Kickstart your projects: interactive git setup + Makefile generation.

`initial-commit` is a lightweight CLI tool that automates the boring first steps of every new project. Run it, answer a few questions, and you're ready to code.

---

## Installation

```bash
pip install initial-commit
```

For local development:

```bash
git clone https://github.com/dallatIkes/initial-commit.git
cd initial-commit
pip install -e .
```

---

## Usage

Just run:

```bash
initial-commit
```

An interactive prompt guides you through the setup:

```
  ✦ initial-commit — project kickstart

  ? Git setup:
    ❯ Init a new repository
      Clone an existing repo
      Skip

  ? Generate a Makefile? (Y/n)

  ? Choose a template:
    ❯ python.mk
      node.mk
```

---

## Built-in templates

| Template    | Stack                   |
| ----------- | ----------------------- |
| `python.mk` | Python (pytest, flake8) |
| `node.mk`   | Node.js (npm, eslint)   |

---

## Custom templates

Drop your own `.mk` files into an `initial_commit_templates/` folder at the root of your project:

```
my-project/
└── initial_commit_templates/
    └── rust.mk
```

`initial-commit` will discover them automatically and give them priority over built-in templates when names collide.

---

## Roadmap

- [ ] Community template registry
- [ ] Shell completion (bash, zsh, fish)
- [ ] Project name prompt + auto-create folder

---

## License

MIT © dallatIkes