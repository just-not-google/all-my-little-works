from Holy_Cow.functions.percentage.data.min_max_percentage import MIN_PERC, MAX_PERS

def is_valid_percentage(percentage: int) -> bool:
    try:
        return MIN_PERC <= percentage <= MAX_PERS
    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False