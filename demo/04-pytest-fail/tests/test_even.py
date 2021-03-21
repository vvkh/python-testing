from even import is_even


def test_negative_even_numbers_are_even():
    assert is_even(-2)
    assert is_even(-4)
    assert is_even(-6)


def test_negative_odd_numbers_are_not_even():
    assert not is_even(-1)
    assert not is_even(-3)
    assert not is_even(-5)


def test_zero_is_even():
    assert is_even(0)


def test_even_numbers_are_even():
    assert is_even(2)
    assert is_even(4)
    assert is_even(6)


def test_odd_numbers_are_not_even():
    assert not is_even(1)
    assert not is_even(3)
    assert not is_even(5)