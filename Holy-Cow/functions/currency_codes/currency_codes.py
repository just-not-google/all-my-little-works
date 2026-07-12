from Holy_Cow.functions.currency_codes.data.currency_codes import currency_codes

def is_valid_currency_codes(currency_code: str) -> bool:
    try:
        if not currency_code in currency_codes:
            return False
        return True
    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False