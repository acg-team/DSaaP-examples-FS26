from datetime import datetime

def is_weekend(now):
    return now.weekday() >= 5

def test_is_not_weekend():
    assert is_weekend(datetime(2026, 3, 20)) is False

def test_is_weekend():
    assert is_weekend(datetime(2026, 3, 22))