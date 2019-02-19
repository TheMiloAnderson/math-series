from series import fibonacci


def test_fibonacci():
    actual = fibonacci(6)
    expected = 5
    assert actual == expected
