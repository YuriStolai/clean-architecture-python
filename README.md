# Clean Architecture Python

This repository is a learning project for practicing Clean Architecture in
Python while studying Robert C. Martin's ideas. The structure is expected to
evolve as the project grows and the architectural understanding becomes more
concrete.

## Content Language

Generated content in this repository should be written in English. This
includes documentation, comments, commit messages, and contributor-facing
text, unless a future repository rule explicitly states otherwise.

## Initial Setup

The project requires Python 3.14 or newer, Poetry, and Make. Run the initial
setup from the repository root:

```bash
make setup
```

Common development commands:

```bash
make test
make test-verbose
make check
make env-info
make clean
```

Run `make help` to see the complete command list. The Make targets wrap Poetry
commands so contributors use the project-managed environment consistently.

## Commit Guidelines

When you create commits in this repository, follow these rules:

- Write commit messages in English.
- Use a standard intent prefix.
- Write the title in the imperative mood.
- Structure the message with a title and a body.
- Keep the body descriptive and no longer than 100 characters.
- Group commits by context.
- Avoid a single large commit with many unrelated files or concerns.

Use this structure:

```text
<prefix>: <imperative title>

<short description with up to 100 characters>
```

Example:

```text
docs: add commit guidelines to README

Explain commit message rules and prefix usage for contributors.
```

## Commit Prefixes

Use the prefix to make the intent of the change clear before anyone reads the
diff. This improves code review, navigation through history, and release notes.

- `feat:` adds a new feature or new user-facing capability.
- `fix:` corrects a bug or unintended behavior.
- `refactor:` changes the internal structure without changing behavior.
- `test:` adds or updates automated tests.
- `docs:` creates or updates documentation.
- `chore:` handles maintenance tasks, configuration, tooling, or repository
  housekeeping.

Choose the prefix based on the main purpose of the commit. If a change mixes
multiple concerns, split it into smaller commits by context whenever possible.
