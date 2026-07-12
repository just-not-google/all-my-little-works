from Holy_Cow.functions.even_number.even_number import is_valid_even_number


def test_is_valid_even_number():
    assert is_valid_even_number(2) == True
    assert is_valid_even_number(4) == True
    assert is_valid_even_number(0) == True
    assert is_valid_even_number(100) == True
    assert is_valid_even_number(-2) == True
    assert is_valid_even_number(-4) == True
    assert is_valid_even_number(1) == False
    assert is_valid_even_number(3) == False
    assert is_valid_even_number(5) == False
    assert is_valid_even_number(99) == False
    assert is_valid_even_number(-1) == False
    assert is_valid_even_number(-3) == False
    assert is_valid_even_number("2") == False
    assert is_valid_even_number(2.5) == False
    assert is_valid_even_number(None) == False
    assert is_valid_even_number([2]) == False
    assert is_valid_even_number({"number": 2}) == False