from Holy_Cow.data_other.other import lowercase, uppercase, special, digits

def is_valid_strength_password(password: str) -> bool:
    try:
        if len(password) < 8:
            return False

        has_lower = False
        has_upper = False
        has_special = False
        has_digit = False

        for char in password:
            if char in lowercase:
                has_lower = True
            elif char in uppercase:
                has_upper = True
            elif char in special:
                has_special = True
            elif char in digits:
                has_digit = True

        strength_score = 0
        if has_lower: strength_score += 1
        if has_upper: strength_score += 1
        if has_special: strength_score += 1
        if has_digit: strength_score += 1
        if len(password) >= 12: strength_score += 1

        return strength_score >= 3

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False
