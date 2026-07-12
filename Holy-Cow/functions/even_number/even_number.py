def is_valid_even_number(number: int) -> bool:
    try:
        return number % 2 == 0
    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False