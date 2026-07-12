from Holy_Cow.functions.adulthood.adulthood import is_valid_adulthood


def test_is_valid_adulthood():
    assert is_valid_adulthood(18, "us") == True
    assert is_valid_adulthood(21, "us") == True
    assert is_valid_adulthood(18, "gb") == True
    assert is_valid_adulthood(20, "jp") == True
    assert is_valid_adulthood(16, "kr") == True
    assert is_valid_adulthood(17, "us") == False
    assert is_valid_adulthood(15, "gb") == False
    assert is_valid_adulthood(19, "jp") == False
    assert is_valid_adulthood(15, "kr") == False
    assert is_valid_adulthood(18, "invalid") == False
    assert is_valid_adulthood(18, "xx") == False
    assert is_valid_adulthood("18", "us") == False
    assert is_valid_adulthood(18, 123) == False
    assert is_valid_adulthood(None, "us") == False
    assert is_valid_adulthood(18, None) == False
    assert is_valid_adulthood([18], "us") == False