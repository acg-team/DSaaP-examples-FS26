import implementation_details as impl

def multiply(a, b):
    return a * b

def double_value(x):
    return multiply(x, 2)

def test_double_value_calls_helper(mocker):
    spy = mocker.spy(impl, "multiply")

    impl.double_value(3)

    spy.assert_called_once_with(3, 2)