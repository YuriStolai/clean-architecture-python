"""Customer value objects."""

from __future__ import annotations

from dataclasses import dataclass
import re
from uuid import UUID, uuid4

from domain.customer.exceptions import (
    InvalidCustomerEmailError,
    InvalidCustomerNameError,
)


EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass(frozen=True, slots=True)
class CustomerId:
    """Stable identifier for a customer."""

    value: UUID

    @classmethod
    def new(cls) -> "CustomerId":
        """Create a new customer identifier."""
        return cls(value=uuid4())


@dataclass(frozen=True, slots=True)
class CustomerName:
    """Customer display name with basic invariants."""

    value: str

    def __post_init__(self) -> None:
        normalized_value = self.value.strip()

        if not normalized_value:
            raise InvalidCustomerNameError("Customer name cannot be blank.")

        if len(normalized_value) < 3:
            raise InvalidCustomerNameError(
                "Customer name must have at least 3 characters."
            )

        object.__setattr__(self, "value", normalized_value)


@dataclass(frozen=True, slots=True)
class CustomerEmail:
    """Customer email normalized for domain use."""

    value: str

    def __post_init__(self) -> None:
        normalized_value = self.value.strip().lower()

        if not EMAIL_PATTERN.match(normalized_value):
            raise InvalidCustomerEmailError("Customer email must be valid.")

        object.__setattr__(self, "value", normalized_value)
