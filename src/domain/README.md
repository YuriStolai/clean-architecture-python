# Domain Layer

This package is the starting point for business rules.

Organize code by business concept instead of by technical role. Add a new
sub-package when a concept earns its own language and rules.

Recommended files inside each concept package:

- `entity.py` for objects with identity and lifecycle
- `value_objects.py` for small immutable types with invariants
- `services.py` for domain behavior that does not fit naturally in one entity
- `exceptions.py` for domain-specific rule violations

Do not introduce repositories, framework adapters, or infrastructure concerns
in this layer.
