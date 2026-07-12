from Holy_Cow.functions.percentage.percentage import is_valid_percentage


def test_is_valid_percentage():
    assert is_valid_percentage(0) == True
    assert is_valid_percentage(50) == True
    assert is_valid_percentage(100) == True
    assert is_valid_percentage(25) == True
    assert is_valid_percentage(75) == True
    assert is_valid_percentage(-1) == False
    assert is_valid_percentage(101) == False
    assert is_valid_percentage(150) == False
    assert is_valid_percentage(-50) == False
    assert is_valid_percentage("50") == False
    assert is_valid_percentage(50.5) == False
    assert is_valid_percentage(None) == False
    assert is_valid_percentage([50]) == False
    assert is_valid_percentage({"percentage": 50}) == False