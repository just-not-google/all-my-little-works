def is_valid_age(age: int, min_age: int, max_age: int) -> bool:
    try:
        if min_age < 0:
            return False
        if age < 0:
            return False
        if not min_age <= age <= max_age:
            return False

        return True


    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False
