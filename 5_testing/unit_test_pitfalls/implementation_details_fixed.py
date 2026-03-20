def multiply(a, b):
    return a * b

def double_value(x):
    return multiply(x, 2)

def test_double_value():
    assert double_value(3) == 6