from Holy_Cow.functions.isogram.isogram import is_valid_isogram


def test_is_valid_isogram():
    assert is_valid_isogram("dermatoglyphics") == True
    assert is_valid_isogram("background") == True
    assert is_valid_isogram("lumberjacks") == True
    assert is_valid_isogram("") == True
    assert is_valid_isogram("a") == True
    assert is_valid_isogram("hello") == False
    assert is_valid_isogram("python") == False
    assert is_valid_isogram("programming") == False
    assert is_valid_isogram("banana") == False
    assert is_valid_isogram("Isogram", True) == True
    assert is_valid_isogram("Background", True) == True
    assert is_valid_isogram("Isogram", False) == False
    assert is_valid_isogram("Background", False) == False
    assert is_valid_isogram(12345) == False
    assert is_valid_isogram(None) == False
    assert is_valid_isogram(["text"]) == False
    assert is_valid_isogram({"text": "isogram"}) == False