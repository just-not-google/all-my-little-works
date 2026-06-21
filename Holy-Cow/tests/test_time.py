from Holy_Cow.functions.time.time import is_valid_time


def test_is_valid_time():
    assert is_valid_time("14:30:00") == True
    assert is_valid_time("14.30.00") == True
    assert is_valid_time("14-30-00") == True
    assert is_valid_time("14/30/00") == True
    assert is_valid_time("00:00:00") == True
    assert is_valid_time("23:59:59") == True
    assert is_valid_time("14:30") == False
    assert is_valid_time("14:30:00:00") == False
    assert is_valid_time("14.30") == False
    assert is_valid_time("24:00:00") == False
    assert is_valid_time("14:60:00") == False
    assert is_valid_time("14:30:60") == False
    assert is_valid_time("-1:30:00") == False
    assert is_valid_time("14:-1:00") == False
    assert is_valid_time("14:30:-1") == False
    assert is_valid_time("abc:30:00") == False
    assert is_valid_time("14:abc:00") == False
    assert is_valid_time("14:30:abc") == False
    assert is_valid_time("14 30 00") == False
    assert is_valid_time("") == False
    assert is_valid_time(None) == False
    assert is_valid_time(143000) == False