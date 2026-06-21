from Holy_Cow.functions.anagram.anagram import is_valid_anagram


def test_is_valid_anagram():
    assert is_valid_anagram("listen", "silent") == True
    assert is_valid_anagram("triangle", "integral") == True
    assert is_valid_anagram("anagram", "nagaram") == True
    assert is_valid_anagram("", "") == True
    assert is_valid_anagram("a", "a") == True
    assert is_valid_anagram("hello", "world") == False
    assert is_valid_anagram("python", "java") == False
    assert is_valid_anagram("abc", "abcd") == False
    assert is_valid_anagram("a", "b") == False
    assert is_valid_anagram("Listen", "Silent", True) == True
    assert is_valid_anagram("Race", "Care", True) == True
    assert is_valid_anagram("Listen", "Silent", False) == False
    assert is_valid_anagram("Race", "Care", False) == False
    assert is_valid_anagram(123, 321) == False
    assert is_valid_anagram("hello", 123) == False
    assert is_valid_anagram(None, "test") == False
    assert is_valid_anagram(["listen"], ["silent"]) == False