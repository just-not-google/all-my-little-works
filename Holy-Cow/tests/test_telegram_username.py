from Holy_Cow.functions.telegram_username.telegram_username import is_valid_telegram_username


def test_is_valid_telegram_username():
    assert is_valid_telegram_username("@username") == True
    assert is_valid_telegram_username("@validuser123") == True
    assert is_valid_telegram_username("@abcde") == True
    assert is_valid_telegram_username("@a" * 5 + "b" * 27) == True
    assert is_valid_telegram_username("username") == False
    assert is_valid_telegram_username("@use") == False
    assert is_valid_telegram_username("@" + "a" * 33) == False
    assert is_valid_telegram_username("@12345") == False
    assert is_valid_telegram_username("@aaa") == False
    assert is_valid_telegram_username("@user!name") == False
    assert is_valid_telegram_username("@user@name") == False
    assert is_valid_telegram_username("@user name") == False
    assert is_valid_telegram_username("@admin") == False
    assert is_valid_telegram_username("@telegram") == False
    assert is_valid_telegram_username("") == False
    assert is_valid_telegram_username(None) == False
    assert is_valid_telegram_username(123) == False
    assert is_valid_telegram_username(["@username"]) == False