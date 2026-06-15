"""Customer domain exceptions."""


class CustomerDomainError(Exception):
    """Base exception for customer domain rule violations."""


class InvalidCustomerNameError(CustomerDomainError):
    """Raised when a customer name does not satisfy domain rules."""


class InvalidCustomerEmailError(CustomerDomainError):
    """Raised when a customer email does not satisfy domain rules."""


class CustomerAlreadyActiveError(CustomerDomainError):
    """Raised when trying to activate an already active customer."""


class CustomerAlreadyInactiveError(CustomerDomainError):
    """Raised when trying to deactivate an already inactive customer."""
