from Holy_Cow.functions.currency_codes.currency_codes import is_valid_currency_codes


def test_is_valid_currency_codes():
    assert is_valid_currency_codes("USD") == True
    assert is_valid_currency_codes("EUR") == True
    assert is_valid_currency_codes("GBP") == True
    assert is_valid_currency_codes("JPY") == True
    assert is_valid_currency_codes("CAD") == True
    assert is_valid_currency_codes("ABC") == False
    assert is_valid_currency_codes("XYZ") == False
    assert is_valid_currency_codes("usd") == False
    assert is_valid_currency_codes("Eur") == False
    assert is_valid_currency_codes("") == False
    assert is_valid_currency_codes(None) == False
    assert is_valid_currency_codes(123) == False
    assert is_valid_currency_codes(["USD"]) == False
    assert is_valid_currency_codes({"code": "USD"}) == False