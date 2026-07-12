from Holy_Cow.functions.http_status_code.data.http_status_code import http_status_codes

def is_valid_http_status_code(status_code: int) -> bool:
    try:
        return status_code in http_status_codes
    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False