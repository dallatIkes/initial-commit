# initial-commit

> Kickstart your projects: `git init` + Makefile generation in one command.

`initial-commit` is a lightweight CLI tool that automates the boring first steps of every new project: initialising a Git repository and dropping a ready-to-use `Makefile` — all in a single command.

---

## Installation

```bash
pip install initial-commit
```

Or, for local development:

```bash
git clone https://github.com/dallatIkes/initial-commit.git
cd initial-commit
pip install -e .
```

---

## Usage

### Initialise a Git repo

```bash
initial-commit --git
```

### Generate a Makefile from a built-in template

```bash
initial-commit --template python.mk
# or
initial-commit --template node.mk
```

### Do both at once

```bash
initial-commit --git --template python.mk
```

### List available templates

```bash
initial-commit --list-templates
```

---

## Built-in templates

| Template    | Language / Stack |
|-------------|-----------------|
| `python.mk` | Python (pytest, flake8) |
| `node.mk`   | Node.js (npm, eslint) |

---

## Custom templates

Drop your own `.mk` files into an `initial_commit_templates/` folder at the root of your project:

```
my-project/
└── initial_commit_templates/
    └── rust.mk
```

`initial-commit` will automatically discover them and give them priority over built-in templates when names collide.

---

## Roadmap

- [ ] Premium / community template registry
- [ ] `--list-templates` with source labels (internal / external)
- [ ] Interactive mode (`--interactive`)
- [ ] Shell completion (bash, zsh, fish)

---

## License

MIT © dallatIkes
