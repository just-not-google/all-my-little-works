from Holy_Cow.functions.positive_integer.positive_integer import is_valid_positive_integer


def test_is_valid_positive_integer():
    assert is_valid_positive_integer(1) == True
    assert is_valid_positive_integer(5) == True
    assert is_valid_positive_integer(100) == True
    assert is_valid_positive_integer(999) == True
    assert is_valid_positive_integer(0) == False
    assert is_valid_positive_integer(-1) == False
    assert is_valid_positive_integer(-5) == False
    assert is_valid_positive_integer(-100) == False
    assert is_valid_positive_integer("1") == False
    assert is_valid_positive_integer(1.5) == False
    assert is_valid_positive_integer(None) == False
    assert is_valid_positive_integer([1]) == False
    assert is_valid_positive_integer({1}) == False