import pytest

def discounted_price(price: float, percentage: float) -> float:
    return price - price * percentage / 100

def test_discount_basic():
    assert discounted_price(100, 20) == pytest.approx(80.0)

def test_discount_scales_with_price():
    assert discounted_price(200, 20) == pytest.approx(160.0)