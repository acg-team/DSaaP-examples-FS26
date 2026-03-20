from datetime import datetime

def is_weekend():
    return datetime.now().weekday() >= 5

def test_is_not_weekend():
    assert is_weekend() is False