import pytest

def discounted_price(price: float, percentage: float) -> float:
    return max(0, price - price * percentage / 100)

def test_discount_float_precision_approx():
    assert discounted_price(10.75, 100/3) == pytest.approx(7.1666666667)

def test_discount_float_precision_approx_rounding():
    assert discounted_price(10.75, 100/3) == pytest.approx(7.1666666667, rel=1e-2)
