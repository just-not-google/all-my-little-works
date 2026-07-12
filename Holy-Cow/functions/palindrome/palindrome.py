def is_valid_palindrome(text: str, ignore_register: bool = False) -> bool:
    try:
        if ignore_register:
            return text.lower() == text.lower()[::-1]

        return text == text[::-1]

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False