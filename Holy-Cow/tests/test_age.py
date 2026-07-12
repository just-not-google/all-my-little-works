from Holy_Cow.functions.age.age import is_valid_age


def test_is_valid_age():
    assert is_valid_age(100, 1, 100) == True
    assert is_valid_age(6, -1, 100) == False
    assert is_valid_age(28, 0, -1) == False
    assert is_valid_age(0, 0, 0) == True
    assert is_valid_age(-65, 5, 10) == False
    assert is_valid_age(50, 0, 10) == False
    assert is_valid_age(0, 0, 100) == True
    assert is_valid_age(100, 0, 100) == True
    assert is_valid_age(1, 1, 1) == True
    assert is_valid_age(25, 18, 65) == True
    assert is_valid_age(-1, 0, 100) == False
    assert is_valid_age(10, -5, 100) == False
    assert is_valid_age(50, 50, 100) == True
    assert is_valid_age(100, 50, 100) == True
    assert is_valid_age(49, 50, 100) == False
    assert is_valid_age(101, 50, 100) == False
    assert is_valid_age("25", 0, 100) == False
    assert is_valid_age(25, "0", 100) == False
    assert is_valid_age(25, 0, "100") == False
    assert is_valid_age(None, 0, 100) == False
    assert is_valid_age(25, None, 100) == False
    assert is_valid_age(0, 0, 1) == True
    assert is_valid_age(1, 0, 1) == True
    assert is_valid_age(2, 0, 1) == False
    assert is_valid_age(999, 0, 1000) == True
    assert is_valid_age(1000, 0, 1000) == True
    assert is_valid_age(1001, 0, 1000) == False