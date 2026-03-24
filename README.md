# initial-commit

> Kickstart your projects: interactive git setup + Makefile generation.

`initial-commit` is a lightweight CLI tool that removes friction when starting a new project.
Initialize your repo, generate a clean Makefile, and start coding in seconds.

---

## 🚀 Installation

```bash
pip install initial-commit
```

For development:

```bash
git clone https://github.com/dallatIkes/initial-commit.git
cd initial-commit
pip install -e .
```

---

## ⚡ Quick Start

```bash
initial-commit
```

Follow the interactive prompts:

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

## 🧠 Non-interactive usage

Perfect for scripts and advanced users:

```bash
initial-commit --init
initial-commit --clone https://github.com/user/repo
initial-commit --template python.mk
initial-commit --init --template python.mk --force
```

List available templates:

```bash
initial-commit --list-templates
```

---

## 📦 Built-in templates

| Template    | Stack                   |
| ----------- | ----------------------- |
| `python.mk` | Python (pytest, flake8) |
| `node.mk`   | Node.js (npm, eslint)   |

---

## 🧩 Custom templates

You can extend `initial-commit` with your own templates.

Create a folder named `initial_commit_templates/` at the root of your project:

```
my-project/
└── initial_commit_templates/
    └── rust.mk
```

Your templates will:

* be automatically detected
* override built-in templates with the same name

---

## ✨ Features

* Interactive CLI (guided setup)
* Non-interactive mode (scriptable)
* Git init & clone support
* Built-in and custom Makefile templates
* Safe overwrite with `--force`

---

## 🛣️ Roadmap

* [ ] Community template registry
* [ ] Shell completion (bash, zsh, fish)
* [ ] Project name prompt + auto-create folder
* [ ] Template packs (advanced setups)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## 📄 License

MIT © dallatIkes
