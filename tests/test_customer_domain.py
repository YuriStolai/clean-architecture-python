"""Tests for the customer domain example."""

from __future__ import annotations

import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


from domain.customer import (  # noqa: E402
    CustomerAlreadyActiveError,
    CustomerAlreadyInactiveError,
    CustomerEmail,
    CustomerModel,
    CustomerName,
    InvalidCustomerEmailError,
    InvalidCustomerNameError,
    activate_customer,
    change_customer_email,
    deactivate_customer,
    register_customer,
    rename_customer,
)


class CustomerValueObjectsTestCase(unittest.TestCase):
    def test_customer_name_strips_surrounding_spaces(self) -> None:
        customer_name = CustomerName("  Ada Lovelace  ")

        self.assertEqual(customer_name.value, "Ada Lovelace")

    def test_customer_name_requires_at_least_three_characters(self) -> None:
        with self.assertRaises(InvalidCustomerNameError):
            CustomerName("Al")

    def test_customer_email_is_normalized_to_lowercase(self) -> None:
        customer_email = CustomerEmail("  ADA@Example.COM ")

        self.assertEqual(customer_email.value, "ada@example.com")

    def test_customer_email_must_be_valid(self) -> None:
        with self.assertRaises(InvalidCustomerEmailError):
            CustomerEmail("invalid-email")


class CustomerEntityTestCase(unittest.TestCase):
    def test_register_creates_active_customer(self) -> None:
        customer = register_customer("Ada Lovelace", "ada@example.com")

        self.assertEqual(customer.name.value, "Ada Lovelace")
        self.assertEqual(customer.email.value, "ada@example.com")
        self.assertTrue(customer.is_active)

    def test_customer_model_contains_only_state(self) -> None:
        customer = CustomerModel(
            id=register_customer("Ada Lovelace", "ada@example.com").id,
            name=CustomerName("Ada Lovelace"),
            email=CustomerEmail("ada@example.com"),
        )

        self.assertEqual(customer.name.value, "Ada Lovelace")
        self.assertTrue(customer.is_active)

    def test_customer_can_be_renamed(self) -> None:
        customer = register_customer("Ada Lovelace", "ada@example.com")

        rename_customer(customer, "Ada Byron")

        self.assertEqual(customer.name.value, "Ada Byron")

    def test_customer_can_change_email(self) -> None:
        customer = register_customer("Ada Lovelace", "ada@example.com")

        change_customer_email(customer, "countess@analysis.org")

        self.assertEqual(customer.email.value, "countess@analysis.org")

    def test_deactivate_changes_customer_state(self) -> None:
        customer = register_customer("Ada Lovelace", "ada@example.com")

        deactivate_customer(customer)

        self.assertFalse(customer.is_active)

    def test_deactivate_rejects_inactive_customer(self) -> None:
        customer = register_customer("Ada Lovelace", "ada@example.com")
        deactivate_customer(customer)

        with self.assertRaises(CustomerAlreadyInactiveError):
            deactivate_customer(customer)

    def test_activate_rejects_active_customer(self) -> None:
        customer = register_customer("Ada Lovelace", "ada@example.com")

        with self.assertRaises(CustomerAlreadyActiveError):
            activate_customer(customer)

    def test_activate_reenables_inactive_customer(self) -> None:
        customer = register_customer("Ada Lovelace", "ada@example.com")
        deactivate_customer(customer)

        activate_customer(customer)

        self.assertTrue(customer.is_active)
