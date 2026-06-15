"""Customer entity module."""

from __future__ import annotations

from domain.customer.exceptions import (
    CustomerAlreadyActiveError,
    CustomerAlreadyInactiveError,
)
from domain.customer.model import CustomerModel
from domain.customer.value_objects import CustomerEmail, CustomerId, CustomerName


def register_customer(name: str, email: str) -> CustomerModel:
    """Create a new active customer from raw external values."""
    return CustomerModel(
        id=CustomerId.new(),
        name=CustomerName(name),
        email=CustomerEmail(email),
    )


def rename_customer(customer: CustomerModel, name: str) -> None:
    """Update the customer's business name."""
    customer.name = CustomerName(name)


def change_customer_email(customer: CustomerModel, email: str) -> None:
    """Update the customer's contact email."""
    customer.email = CustomerEmail(email)


def deactivate_customer(customer: CustomerModel) -> None:
    """Disable the customer for future operations."""
    if not customer.is_active:
        raise CustomerAlreadyInactiveError("Customer is already inactive.")

    customer.is_active = False


def activate_customer(customer: CustomerModel) -> None:
    """Re-enable the customer for future operations."""
    if customer.is_active:
        raise CustomerAlreadyActiveError("Customer is already active.")

    customer.is_active = True
