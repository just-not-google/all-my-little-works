from Holy_Cow.functions.date.date import is_valid_date
from Holy_Cow.functions.time.time import is_valid_time

def is_valid_date_time(date_time: str) -> bool:
    try:
        if not " " in date_time:
            return False

        dt_tm_lst = date_time.split(" ")
        if len(dt_tm_lst) != 2:
            return False

        if not is_valid_date(dt_tm_lst[0]):
            return False

        if not is_valid_time(dt_tm_lst[1]):
            return False

        return True

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False