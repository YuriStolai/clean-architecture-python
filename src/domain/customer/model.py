"""Customer data model."""

from __future__ import annotations

from dataclasses import dataclass

from domain.customer.value_objects import CustomerEmail, CustomerId, CustomerName


@dataclass(slots=True)
class CustomerModel:
    """Customer state without business behavior."""

    id: CustomerId
    name: CustomerName
    email: CustomerEmail
    is_active: bool = True
