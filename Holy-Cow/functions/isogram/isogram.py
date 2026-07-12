def is_valid_isogram(text: str, ignore_register: bool = False) -> bool:
    try:
        if ignore_register:
            text = text.lower()

        return sorted(text) == sorted(list(set(text)))

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False