from Holy_Cow.functions.no_special_chars.no_special_chars import is_valid_no_special_chars


def test_is_valid_no_special_chars():
    assert is_valid_no_special_chars("hello") == True
    assert is_valid_no_special_chars("Hello World") == True
    assert is_valid_no_special_chars("123abc") == True
    assert is_valid_no_special_chars("") == True
    assert is_valid_no_special_chars("hello!") == False
    assert is_valid_no_special_chars("hello@world") == False
    assert is_valid_no_special_chars("hello#") == False
    assert is_valid_no_special_chars("$hello") == False
    assert is_valid_no_special_chars("hello%world") == False
    assert is_valid_no_special_chars(123) == False
    assert is_valid_no_special_chars(None) == False
    assert is_valid_no_special_chars(["hello"]) == False
    assert is_valid_no_special_chars({"text": "hello"}) == False