import pytest
from unittest.mock import patch
from email_validator import EmailNotValidError
from app.utils.validators import validate_email_address
def test_validate_email_address_invalid_email():
    """
    Test that the function returns False for an invalid email address.
    """
    assert validate_email_address("invalid_email") is False

def test_validate_email_address_empty_email():
    """
    Test that the function returns False for an empty email address.
    """
    assert validate_email_address("") is False
