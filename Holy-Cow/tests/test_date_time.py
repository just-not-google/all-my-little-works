from Holy_Cow.functions.date_time.date_time import is_valid_date_time


def test_is_valid_date_time():
    assert is_valid_date_time("2023/10/15 14:30:00") == True
    assert is_valid_date_time("2023-10-15 14:30:00") == True
    assert is_valid_date_time("2023.10.15 14:30:00") == True
    assert is_valid_date_time("2023/10/15") == False
    assert is_valid_date_time("14:30:00") == False
    assert is_valid_date_time("2023/10/15 14:30:00 12") == False
    assert is_valid_date_time("2023/13/15 14:30:00") == False
    assert is_valid_date_time("2023/10/15 25:30:00") == False
    assert is_valid_date_time("2023/10/15 14:30") == False
    assert is_valid_date_time("2023/10/15 14:30:00:00") == False
    assert is_valid_date_time("abc/10/15 14:30:00") == False
    assert is_valid_date_time("2023/10/15 abc:30:00") == False
    assert is_valid_date_time("2023/02/29 14:30:00") == False
    assert is_valid_date_time("2020/02/29 14:30:00") == True
    assert is_valid_date_time("") == False
    assert is_valid_date_time("2023/10/15 ") == False
    assert is_valid_date_time(" 14:30:00") == False