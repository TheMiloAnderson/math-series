from series import fibonacci


def test_fibonacci_1():
    actual = fibonacci(1)
    expected = 0
    assert actual == expected

def test_fibonacci_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_6():
    actual = fibonacci(6)
    expected = 5
    assert actual == expected
