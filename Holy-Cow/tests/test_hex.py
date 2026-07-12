from Holy_Cow.functions.hex.hex import is_valid_hex


def test_is_valid_hex():
    assert is_valid_hex("#fff") == True
    assert is_valid_hex("#ffff") == True
    assert is_valid_hex("#ffffff") == True
    assert is_valid_hex("#ffffffff") == True
    assert is_valid_hex("#abc123") == True
    assert is_valid_hex("#123456") == True
    assert is_valid_hex("#ABCDEF") == True
    assert is_valid_hex("fff") == False
    assert is_valid_hex("#") == False
    assert is_valid_hex("#ff") == False
    assert is_valid_hex("#fffff") == False
    assert is_valid_hex("#fffffff") == False
    assert is_valid_hex("#ggg") == False
    assert is_valid_hex("#12345g") == False
    assert is_valid_hex("#12 3456") == False
    assert is_valid_hex("#12-3456") == False
    assert is_valid_hex("") == False
    assert is_valid_hex(None) == False
    assert is_valid_hex(123) == False
    assert is_valid_hex(["#fff"]) == False