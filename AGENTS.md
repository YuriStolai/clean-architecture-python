# AGENTS.md

## Purpose

This repository is a learning project for practicing Clean Architecture in
Python while studying Robert C. Martin's ideas. The codebase is expected to
change as the understanding of the book evolves.

Agents working in this repository should optimize for architectural clarity,
small refactorable steps, and decisions that keep business rules independent
from external details.

## Current State

The repository is intentionally minimal right now.

- `src/` exists for application code.
- `tests/` exists for automated tests.
- The concrete module layout is still expected to evolve.

Do not assume that every Clean Architecture layer already has a dedicated
package. Prefer introducing structure only when the code justifies it.

## Core Architectural Rule

The dependency direction must point inward.

- Inner layers must not depend on frameworks, databases, web libraries, CLIs,
  ORMs, or delivery mechanisms.
- Business rules should stay readable without needing infrastructure context.
- External details may depend on application and domain code, never the reverse.

When in doubt, ask: "Can this code still make sense if the framework or storage
technology changes?" If not, it probably belongs closer to the edge.

## Layer Responsibilities

Use these responsibilities as guidance when organizing code.

### Entities

- Hold the most stable business rules and domain concepts.
- Avoid infrastructure concerns and delivery-specific data shapes.
- Prefer plain Python objects and explicit behavior over framework coupling.

### Use Cases / Application

- Orchestrate application-specific business flows.
- Coordinate entities and abstract ports/interfaces.
- Contain no knowledge of HTTP, CLI parsing, ORM models, or database drivers.

### Interface Adapters

- Translate between external formats and internal models.
- Implement presenters, controllers, gateways, repositories, or mappers when
  needed.
- Keep translation logic here instead of leaking it into use cases or entities.

### Frameworks and Drivers

- Contain infrastructure details such as persistence, web frameworks, CLI
  entrypoints, configuration loading, and third-party integrations.
- Stay replaceable.
- Depend on inner layers through explicit contracts where useful.

## Evolution Rules

This project should follow Clean Architecture seriously, but not dogmatically.

- Prefer incremental improvement over premature restructuring.
- Avoid over-architecting features before there is enough code to justify the
  abstraction.
- Temporary shortcuts are acceptable only when they are easy to identify and
  easy to remove later.
- If a shortcut mixes concerns, keep the blast radius small and leave a clear
  path for extraction.
- If a design choice is mainly for learning, document that in code comments,
  commit messages, or supporting docs when relevant.

## Implementation Guidance

When adding or changing code:

- Start from the use case or business behavior, not from the framework.
- Keep business logic out of controllers, route handlers, ORM models, and
  scripts.
- Introduce external dependencies at the edges first, then connect them inward.
- Add abstractions when they protect business rules or isolate unstable
  dependencies, not just to satisfy a pattern.
- Prefer explicit names that reflect business intent over generic technical
  names.

Before placing code, ask:

1. Is this business policy, application flow, translation, or infrastructure?
2. What should this code depend on?
3. What should remain unchanged if we swap the outer technology?

## Testing Guidance

Tests should reflect the architecture.

- Prioritize tests for entities and use cases.
- Test business rules without requiring real databases, networks, or frameworks.
- Add adapter or integration tests when crossing external boundaries.
- Use end-to-end style tests sparingly and mainly to validate wiring between
  layers.

If a test for a core rule requires heavy infrastructure setup, revisit the
design before accepting it.

## Agent Instructions

Agents contributing here should follow these defaults:

- Preserve the inward dependency rule.
- Prefer reversible refactors over broad rewrites.
- Do not invent package structure that the code does not need yet.
- When adding infrastructure code, keep the seam with inner layers explicit.
- If a change intentionally violates Clean Architecture for now, say so clearly
  in the final report and limit the violation to one place.
- Do not create commits automatically after making changes.

## Commit Conventions

Commits in this repository must follow these rules:

- Write commit messages in English.
- Use a market-standard intent prefix such as `feat:`, `fix:`, `refactor:`,
  `test:`, `docs:`, or `chore:`.
- Write the title in the imperative mood.
- Structure each commit message with a title and a body.
- Group commits by context so each commit represents one coherent change.
- Avoid single large commits that bundle many unrelated files or concerns.
- Keep the body descriptive and no longer than 100 characters.

## Memory File

Every committed change must also be reflected in `agents/memory.md`.

- Treat `agents/memory.md` as a context file for future agents, not as a
  commit-by-commit changelog.
- Organize entries around implemented features, repository capabilities,
  working rules, and important decisions.
- Add a short summary of what was changed.
- Add a short explanation of why the change was made.
- Update the file whenever a committed change materially affects architecture,
  contributor workflow, repository conventions, or implemented behavior.
- Keep the file updated as part of the same delivery context so the project
  history remains understandable from inside the repository without requiring a
  full repository survey.

The goal is not to mimic the book mechanically. The goal is to learn the
architecture by building, observing pressure points, and improving the design
without losing conceptual integrity.
