def is_valid_ccv_cvc(code: int) -> bool:
    try:
        return 100 <= code <= 999 or 1000 <= code <= 9999
    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False