from Holy_Cow.functions.number_phone.number_phone import is_valid_number_phone


def test_is_valid_number_phone():
    assert is_valid_number_phone("+1-555-123-4567", "us") == True
    assert is_valid_number_phone("15551234567", "us") == True
    assert is_valid_number_phone("+44 20 7946 0958", "gb") == True
    assert is_valid_number_phone("442079460958", "gb") == True
    assert is_valid_number_phone("+91 9876543210", "in") == True
    assert is_valid_number_phone("919876543210", "in") == True
    assert is_valid_number_phone("1555123456", "us") == False
    assert is_valid_number_phone("155512345678", "us") == False
    assert is_valid_number_phone("91987654321", "in") == False
    assert is_valid_number_phone("9198765432101", "in") == False
    assert is_valid_number_phone("abc5551234567", "us") == False
    assert is_valid_number_phone("55-512-34567", "us") == False
    assert is_valid_number_phone("+1-555-123-4567", "invalid") == False
    assert is_valid_number_phone("", "us") == False
    assert is_valid_number_phone(None, "us") == False
    assert is_valid_number_phone(15551234567, "us") == False
    assert is_valid_number_phone("15551234567", None) == False
    assert is_valid_number_phone("15551234567", 123) == False