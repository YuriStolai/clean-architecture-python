# Poetry Cheat Sheet

Quick reference for useful day-to-day `poetry` commands.

## Quick checks

```bash
poetry --version
poetry check
poetry env info
poetry env list
```

Tips:
- Use `poetry check` to validate `pyproject.toml`.
- Use `poetry env info` to confirm which virtual environment is active.

## Install dependencies

```bash
poetry install
```

Tips:
- Run this when you start working on the project.
- In this repository, `package-mode = false`, so the focus is the workspace
  environment rather than packaging and publishing.

## Add dependencies

```bash
poetry add requests
poetry add pytest --group dev
poetry add ruff --group dev
```

Tips:
- Use `poetry add package-name` for runtime dependencies.
- Use `--group dev` for development and test tooling.

## Remove dependencies

```bash
poetry remove requests
poetry remove pytest --group dev
```

## Refresh the lock file

```bash
poetry lock
poetry lock --no-update
```

Tips:
- `poetry lock` recalculates `poetry.lock`.
- `poetry lock --no-update` preserves already resolved versions when possible.

## Update dependencies

```bash
poetry update
poetry update pytest
```

Tips:
- `poetry update` upgrades everything allowed by `pyproject.toml`.
- Prefer updating one package at a time when you want tighter control.

## Run commands inside the virtual environment

```bash
poetry run python -V
poetry run pytest
poetry run python -m clean_architecture_python
```

Tips:
- `poetry run` avoids relying on manual shell activation.
- It is the most predictable way to run tests, scripts, and project CLIs.

## Open a shell inside the virtual environment

```bash
poetry shell
```

Tips:
- Useful for longer development sessions.
- If you want to avoid an interactive shell, prefer `poetry run`.

## Manage virtual environments

```bash
poetry env use python3.14
poetry env remove python3.14
poetry env info --path
```

Tips:
- Use `poetry env use` to pin the Python version for the project.
- Remove old environments when changing Python versions.
- Use `poetry env info --path` to get the virtual environment directory when
  configuring your IDE interpreter.

## Inspect installed dependencies

```bash
poetry show
poetry show --tree
```

Tips:
- `poetry show` lists installed packages.
- `poetry show --tree` helps inspect transitive dependencies.

## Common workflow

```bash
poetry install
poetry add pytest --group dev
poetry run pytest
poetry lock
```

## Common issues

- If a command cannot find the expected package, confirm the active
  environment with `poetry env info`.
- If the lock file looks outdated, run `poetry lock` and then `poetry install`.
- If the project Python version changes, recreate the environment with
  `poetry env use ...`.
