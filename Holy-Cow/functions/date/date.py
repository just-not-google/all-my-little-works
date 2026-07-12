from Holy_Cow.data_other.other import DOT

def is_valid_date(date: str) -> bool:
    try:
        date_1 = date
        if "/" in date:
            date_1 = date.replace("/", DOT)
        elif "-" in date:
            date_1 = date.replace("-", DOT)

        if not DOT in date_1:
            return False

        date_lst = date_1.split(DOT)
        dt_list = []

        for i in date_lst:
            if not i.isdigit():
                return False
            if int(i) < 0:
                return False
            else:
                dt_list.append(int(i))

        if len(dt_list) != 3:
            return False

        year = dt_list[0]
        month = dt_list[1]
        day = dt_list[2]

        if year < 0:
            return False
        if not (1 <= month <= 12):
            return False
        if not (1 <= day <= 31):
            return False

        if month in [4, 6, 9, 11] and day > 30:
            return False

        if month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            if day > 29 or (day == 29 and not is_leap):
                return False

        return True

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False


