from Holy_Cow.functions.palindrome.palindrome import is_valid_palindrome


def test_is_valid_palindrome():
    assert is_valid_palindrome("radar") == True
    assert is_valid_palindrome("level") == True
    assert is_valid_palindrome("madam") == True
    assert is_valid_palindrome("a") == True
    assert is_valid_palindrome("") == True
    assert is_valid_palindrome("hello") == False
    assert is_valid_palindrome("world") == False
    assert is_valid_palindrome("python") == False
    assert is_valid_palindrome("Racecar", True) == True
    assert is_valid_palindrome("Aba", True) == True
    assert is_valid_palindrome("Racecar", False) == False
    assert is_valid_palindrome("Aba", False) == False
    assert is_valid_palindrome(12321) == False
    assert is_valid_palindrome(None) == False
    assert is_valid_palindrome(["radar"]) == False
    assert is_valid_palindrome({"text": "radar"}) == False