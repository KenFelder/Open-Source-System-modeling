import Calculate


def test_multiply():
    assert Calculate.multiply(2, 2) == 4
    assert Calculate.multiply(1, 2) == 2
    assert Calculate.multiply(5, 3) == 15


def test_divide():
    assert Calculate.divide(2, 2) == 1
    assert Calculate.divide(1, 2) == 0.5
    assert Calculate.divide(6, 3) == 2


def test_square():
    assert Calculate.square(5) == 25
    assert Calculate.square(1) == 1
    assert Calculate.square(-6) == 36
