import pytest

def discounted_price(price: float, percentage: float) -> float:
    return price - price * percentage / 100

def discounted_price1(price: float, percentage: float) -> float:
    return price - price * min(100, percentage) / 100

def discounted_price2(price: float, percentage: float) -> float:
    return max(0, price - price * percentage / 100)

def test_discount_basic():
    assert discounted_price(100, 20) == pytest.approx(80.0)

def test_discount_scales_with_price():
    assert discounted_price(200, 20) == pytest.approx(160.0)

def test_discount_above_hundred():
    assert discounted_price(50, 150) == 0.0

def test_price_below_zero():
    assert discounted_price(-50, 10) == 0.0