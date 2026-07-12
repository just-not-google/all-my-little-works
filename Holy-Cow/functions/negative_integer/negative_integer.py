def is_valid_negative_integer(integer: int) -> bool:
    try:
        return integer < 0
    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False