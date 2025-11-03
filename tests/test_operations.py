# tests/test_operations.py

import pytest
from app import operations


def test_add():
    result = operations.add(5, 3)
    assert result == 8


def test_subtract():
    result = operations.subtract(10, 4)
    assert result == 6


def test_multiply():
    result = operations.multiply(6, 7)
    assert result == 42


def test_divide():
    result = operations.divide(20, 4)
    assert result == 5


def test_divide_by_zero():
    """Test that dividing by zero raises ValueError."""
    with pytest.raises(ValueError) as exc_info:
        operations.divide(5, 0)
    assert str(exc_info.value) == "Cannot divide by zero."

