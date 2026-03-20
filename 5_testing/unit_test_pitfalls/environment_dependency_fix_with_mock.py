from datetime import datetime

def is_weekend():
    return datetime.now().weekday() >= 5

def test_is_not_weekend(mocker):
    mock_datetime = mocker.patch(f'{__name__}.datetime')
    mock_datetime.now.return_value.weekday.return_value = 0
    assert is_weekend() is False