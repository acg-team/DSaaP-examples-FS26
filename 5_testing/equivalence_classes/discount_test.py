import pytest

def discounted_price(price, percentage):
    return max(0, price - price * percentage / 100)

# Equivalence class 1: basic functionality
def test_discount_basic():
    assert discounted_price(100, 20) == pytest.approx(80.0)

def test_discount_scales_with_price():
    assert discounted_price(200, 20) == pytest.approx(160.0)

# Equivalence class 1.5: basic functionality with float inputs
def test_discount_float_price():
    # real value is 8.0625, but should it be 8.0625 or 8.06?
    # prices are often rounded to 2 decimal places, so we should adjust the implementation
    # to round to 2 decimals, or adjust the test to allow for rounding differences
    assert discounted_price(10.75, 25) == pytest.approx(8.0625)
    # assert discounted_price(10.75, 25) == pytest.approx(8.0625, rel=1e-2)

def test_discount_float_discount():
    assert discounted_price(180, 2.5) == pytest.approx(175.5)

# Equivalence class 2: edge case, price is zero
def test_price_zero():
    assert discounted_price(0, 20) == 0.0

# Equivalence class 3: edge case, price below zero
def test_price_below_zero():
    assert discounted_price(-50, 10) == 0.0

# Equivalence class 4: edge case, percentage is zero
def test_discount_zero_percent():
    assert discounted_price(100, 0) == pytest.approx(100.0)

# Equivalence class 5: edge case, percentage above 100%
def test_discount_above_hundred():
    assert discounted_price(50, 150) == 0.0

# Equivalence class 6: edge case, percentage below zero
def test_discount_percentage_below_zero():
    # should this result in a higher price? Or should it be treated as zero discount?
    assert discounted_price(100, -20) == pytest.approx(120.0)
    # assert discounted_price(100, -20) == pytest.approx(100.0)

# Equivalence class 7: invalid input types
def test_invalid_input_price():
    with pytest.raises(TypeError):
        discounted_price("100", 20)

def test_invalid_input_percentage():
    with pytest.raises(TypeError):
        discounted_price(100, "20")