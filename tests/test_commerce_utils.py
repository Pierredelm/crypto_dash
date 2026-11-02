import pytest

from commerce_utils import calculate_discount, calculate_vat


def test_calculate_vat():
    assert calculate_vat(100.0) == 20.0


def test_calculate_discount_valid():
    assert calculate_discount(100.0, 20.0) == 80.0


def test_calculate_discount_invalid():
    # This test expects a ValueError when an invalid discount is passed
    with pytest.raises(ValueError):
        calculate_discount(100.0, 150.0)     

def test_calculate_discount_negative():
    with pytest.raises(ValueError, match="Discount percent must be positive."):
        calculate_discount(100.0, -20.0)           
