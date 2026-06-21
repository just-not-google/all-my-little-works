from Holy_Cow.functions.strength_password.strength_password import is_valid_strength_password


def test_is_valid_strength_password():
    assert is_valid_strength_password("Password123!") == True
    assert is_valid_strength_password("StrongPass1!") == True
    assert is_valid_strength_password("Abcdefg1!") == True
    assert is_valid_strength_password("VeryLongPassword123!") == True
    assert is_valid_strength_password("short") == False
    assert is_valid_strength_password("password") == False
    assert is_valid_strength_password("PASSWORD") == False
    assert is_valid_strength_password("12345678") == False
    assert is_valid_strength_password("!@#$%^&*") == False
    assert is_valid_strength_password("Pass123") == False
    assert is_valid_strength_password("onlylowercase") == False
    assert is_valid_strength_password("ONLYUPPERCASE") == False
    assert is_valid_strength_password("123456789") == False
    assert is_valid_strength_password("!@#$%^&*()") == False
    assert is_valid_strength_password("") == False
    assert is_valid_strength_password(None) == False
    assert is_valid_strength_password(12345678) == False
    assert is_valid_strength_password(["Password123!"]) == False