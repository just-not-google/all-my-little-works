from Holy_Cow.functions.negative_integer.negative_integer import is_valid_negative_integer


def test_is_valid_negative_integer():
    assert is_valid_negative_integer(-1) == True
    assert is_valid_negative_integer(-5) == True
    assert is_valid_negative_integer(-100) == True
    assert is_valid_negative_integer(-999) == True
    assert is_valid_negative_integer(0) == False
    assert is_valid_negative_integer(1) == False
    assert is_valid_negative_integer(5) == False
    assert is_valid_negative_integer(100) == False
    assert is_valid_negative_integer(" -1") == False
    assert is_valid_negative_integer(-1.5) == False
    assert is_valid_negative_integer(None) == False
    assert is_valid_negative_integer([-1]) == False
    assert is_valid_negative_integer({-1}) == False