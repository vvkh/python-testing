from prime import is_prime


def test_prime():
    assert is_prime(5)
    assert not is_prime(4)
