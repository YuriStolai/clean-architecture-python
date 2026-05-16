"""Structure checks for the initial domain layer scaffold."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


class DomainStructureTestCase(unittest.TestCase):
    def test_domain_packages_import(self) -> None:
        module_names = (
            "domain",
            "domain.customer",
            "domain.customer.entity",
            "domain.customer.value_objects",
            "domain.customer.exceptions",
            "domain.order",
            "domain.order.entity",
            "domain.order.value_objects",
            "domain.order.services",
            "domain.order.exceptions",
        )

        for module_name in module_names:
            with self.subTest(module_name=module_name):
                module = importlib.import_module(module_name)
                self.assertIsNotNone(module)
