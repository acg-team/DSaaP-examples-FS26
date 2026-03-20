def discounted_price(price: float, percentage: float) -> float:
    return max(0, price - price * percentage / 100)

def test_discount_float_precision_too_strict():
    assert discounted_price(10.75, 100/3) == 7.1666666667