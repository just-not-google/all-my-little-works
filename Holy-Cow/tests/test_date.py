from Holy_Cow.functions.date.date import is_valid_date


def test_is_valid_date():
    assert is_valid_date("2023/10/15") == True
    assert is_valid_date("2023-10-15") == True
    assert is_valid_date("2023.10.15") == True
    assert is_valid_date("2023/02/30") == False
    assert is_valid_date("2023/04/31") == False
    assert is_valid_date("2023/06/31") == False
    assert is_valid_date("2023/13/15") == False
    assert is_valid_date("2023/00/15") == False
    assert is_valid_date("2023/02/29") == False
    assert is_valid_date("2020/02/29") == True
    assert is_valid_date("2023/12/32") == False
    assert is_valid_date("2023/12/00") == False
    assert is_valid_date("2023/10") == False
    assert is_valid_date("2023/10/15/20") == False
    assert is_valid_date("2023/10/15abc") == False
    assert is_valid_date("abc/10/15") == False
    assert is_valid_date("2023 10 15") == False
    assert is_valid_date("") == False
    assert is_valid_date("-2023/10/15") == False
    assert is_valid_date("2023/-10/15") == False
    assert is_valid_date("2023/10/-15") == False