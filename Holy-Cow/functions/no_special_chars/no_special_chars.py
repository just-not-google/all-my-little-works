from Holy_Cow.data_other.other import special

def is_valid_no_special_chars(text: str, special_chars: list[str] = special) -> bool:
    try:
        for i in special_chars:
            if i in text:
                return False
        return True
    except TypeError:
        return False
    except AttributeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False