from series import fibonacci, lucas


def test_fibonacci_1():
    """ test fibonacci(1) """
    actual = fibonacci(1)
    expected = 0
    assert actual == expected


def test_fibonacci_2():
    """ test fibonacci(2) """
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_6():
    """ test fibonacci(6) """
    actual = fibonacci(6)
    expected = 5
    assert actual == expected


def test_lucas_1():
    """ test lucas(1) """
    actual = lucas(1)
    expected = 2
    assert actual == expected


def test_lucas_3():
    """ test lucas(3) """
    actual = lucas(3)
    expected = 3
    assert actual == expected


def test_lucas_7():
    """ test lucas(7) """
    actual = lucas(7)
    expected = 18
    assert actual == expected
