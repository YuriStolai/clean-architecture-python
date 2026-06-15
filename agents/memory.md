# Memory

This file exists to give agents fast project context without requiring a full
 repository survey. Record relevant implemented changes here in terms of
 project capability, repository rules, and important decisions. Focus on what
 was done and why it matters.

## Project Purpose

What:
- This repository is a learning project for practicing Clean Architecture in
  Python.
- The project is evolving alongside the study of Robert C. Martin's ideas.

Why:
- Agents should treat the current structure as intentionally incomplete and
  prefer decisions that preserve room for architectural refinement.

## Repository Baseline

What:
- The repository has a minimal Python project scaffold with `src/`, `tests/`,
  `pyproject.toml`, and documentation files at the root.
- There is no fully expanded Clean Architecture package layout yet.

Why:
- Agents should not assume that every architectural layer already has a module
  or package.
- New structure should be introduced only when justified by real code and use
  cases.

## Architectural Guidance

What:
- `AGENTS.md` was created as the main operating guide for agents.
- The project explicitly adopts the inward dependency rule from Clean
  Architecture.
- The intended roles of entities, use cases/application, interface adapters,
  and frameworks/drivers are documented.
- The repository guidance favors incremental improvement over premature
  abstraction.

Why:
- Agents need a stable architectural reference even while the project is still
  in an early learning phase.
- This reduces the risk of placing business logic in framework code or creating
  structure that is more ceremonial than useful.

## Domain Structure

What:
- `src/domain/` was introduced as the first explicit architecture package.
- The domain layer is currently organized by business concept, with initial
  `customer` and `order` packages.
- Each concept package starts with focused modules such as `entity.py`,
  `value_objects.py`, `services.py`, and `exceptions.py` only where relevant.
- `src/domain/README.md` documents how new domain concepts should be added.
- `tests/test_domain_structure.py` verifies that the initial domain packages
  can be imported without framework or infrastructure setup.

Why:
- The project now has a concrete place for business rules before application
  and infrastructure layers are introduced.
- Grouping by concept keeps related rules together and avoids a flat
  technology-oriented domain package.
- The structure remains small and easy to refactor as the real business model
  becomes clearer.

## Customer Domain

What:
- The customer concept now includes `CustomerId`, `CustomerName`, and
  `CustomerEmail` value objects with identifier generation, name validation,
  and email normalization.
- `CustomerModel` holds customer state while functions in `entity.py` implement
  registration, renaming, email changes, activation, and deactivation.
- Customer-specific exceptions represent invalid values and repeated status
  transitions.
- The customer package exports its public domain API, and focused tests cover
  value-object invariants and customer state transitions.

Why:
- The project now has its first executable business rules in the domain layer,
  independent of frameworks and infrastructure.
- Separating state from domain operations makes the current learning design
  explicit while keeping it easy to refactor as the model evolves.

## Commit Conventions

What:
- Commit messages must be written in English.
- Commits must use a standard intent prefix such as `feat:`, `fix:`,
  `refactor:`, `test:`, `docs:`, or `chore:`.
- Commit titles must use the imperative mood.
- Commit messages must contain a title and a body.
- The body must be descriptive and no longer than 100 characters.
- Commits must be grouped by context.
- Large single commits with mixed concerns should be avoided.
- Changes must not be committed automatically after they are made.

Why:
- The repository history is meant to be readable, reviewable, and useful for
  learning.
- Agents should create commits that communicate intent clearly and keep changes
  easy to inspect in isolation.

## Contributor Documentation

What:
- `README.md` was populated with an introductory project description.
- `README.md` now explains how commit messages must be written.
- `README.md` includes a short explanation of the common prefixes `feat`,
  `fix`, `refactor`, `test`, `docs`, and `chore`.
- `README.md` includes an example of the expected commit message structure.
- `docs/poetry/cheat-sheet.md` was added as the initial focused documentation
  subtree for Poetry day-to-day usage.
- `docs/testing/cheat-sheet.md` was added as a focused reference for running and
  narrowing tests with `unittest` and Poetry.
- The Poetry cheat sheet includes common commands for installation,
  dependency management, lockfile handling, environment inspection, and IDE
  interpreter discovery.
- The test cheat sheet includes commands for full-suite runs, targeted module
  runs, single test methods, and useful `unittest` flags.
- `README.md` and `AGENTS.md` now explicitly require generated repository
  content to be written in English.

Why:
- Human contributors need direct, instructional guidance in the main project
  documentation, not only in `AGENTS.md`.
- This makes contribution rules visible without requiring contributors to infer
  them from the Git history.
- A dedicated `docs/` subtree keeps operational references organized as the
  repository grows.
- The explicit language rule prevents mixed-language documentation and keeps
  generated content consistent.

## Repository Hygiene

What:
- `.gitignore` was added with common ignore rules for Python caches, bytecode,
  virtual environments, coverage output, build artifacts, editor files, and OS
  files.
- `.idea/` files were removed from version control and are now ignored.

Why:
- Local development artifacts should not pollute the repository.
- This keeps the versioned content focused on source, tests, and meaningful
  documentation.

## Poetry Configuration

What:
- `pyproject.toml` now sets `tool.poetry.package-mode = false`.
- The explicit `tool.poetry.packages` entry was removed after the package
  directory under `src/` was flattened away.
- `poetry.lock` was added even though the project currently has no runtime
  dependencies.

Why:
- The repository is currently used as a learning workspace, not as a Python
  package to be built and published.
- Disabling package mode keeps Poetry aligned with that workflow while still
  allowing dependency locking and reproducible environment setup.
- Removing the stale package include keeps Poetry configuration aligned with
  the current source layout and avoids references to a non-existent package
  path.

## Git Identity and History Normalization

What:
- The repository-local Git identity was configured as:
  `user.name = Yuri Stolai`
  `user.email = ystolai@gmail.com`
- Recent commit messages and metadata were rewritten to match the repository
  standards.

Why:
- Future commits should use the intended author identity.
- The recent history should reflect the same rules that the repository now
  requires from future contributors.

## Memory File Rule

What:
- `AGENTS.md` now requires every committed change to be reflected in this file.
- `AGENTS.md` now instructs agents to read this file at the start of each new
  session before doing other repository work.
- Each relevant entry should explain what was changed and why the change was
  made.

Why:
- Agents should be able to recover project context quickly from inside the
  repository.
- Reading this file first gives each new session an immediate baseline context
  before deeper inspection begins.
- This file is intended to reduce repeated discovery work and preserve the
  reasoning behind important changes.

## Current Agent Expectations

What:
- Agents should preserve inward dependencies.
- Agents should avoid inventing package structure too early.
- Agents should keep business logic out of framework and delivery code.
- Agents should update this file whenever a committed change materially changes
  repository rules, architecture, or implemented capabilities.

Why:
- The project is still being shaped.
- Consistent documentation helps future agents make correct decisions with less
  rework.
