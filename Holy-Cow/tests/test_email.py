from Holy_Cow.functions.email.email import is_valid_email


def test_is_valid_email():
    assert is_valid_email("test@example.com") == True
    assert is_valid_email("user.name@domain.co") == True
    assert is_valid_email("user_name@domain.org") == True
    assert is_valid_email("user-name@domain.net") == True
    assert is_valid_email("user123@domain.info") == True
    assert is_valid_email("TEST@EXAMPLE.COM") == True
    assert is_valid_email("") == False
    assert is_valid_email("test@") == False
    assert is_valid_email("@example.com") == False
    assert is_valid_email("test@example") == False
    assert is_valid_email("test@example.") == False
    assert is_valid_email("test@.com") == False
    assert is_valid_email("test@@example.com") == False
    assert is_valid_email("test@example@com") == False
    assert is_valid_email(".test@example.com") == False
    assert is_valid_email("test.@example.com") == False
    assert is_valid_email("te..st@example.com") == False
    assert is_valid_email("test@-example.com") == False
    assert is_valid_email("test@example-.com") == False
    assert is_valid_email("a" * 65 + "@example.com") == False
    assert is_valid_email("test@" + "a" * 254) == False
    assert is_valid_email("test@invalid.tld") == False
    assert is_valid_email("test@example.a") == False
    assert is_valid_email("test@sub.domain.com") == True
    assert is_valid_email("test@multiple.sub.domains.com") == True