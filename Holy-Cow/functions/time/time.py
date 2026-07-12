from Holy_Cow.data_other.other import DOT

def is_valid_time(time: str) -> bool:
    try:
        time_1 = time
        if "/" in time:
            time_1 = time.replace("/", DOT)
        elif "-" in time:
            time_1 = time.replace("-", DOT)
        elif ":" in time:
            time_1 = time.replace(":", DOT)

        if not DOT in time_1:
            return False

        time_lst = time_1.split(DOT)
        tm_list = []

        for i in time_lst:
            if not i.isdigit():
                return False
            if int(i) < 0:
                return False
            else:
                tm_list.append(int(i))

        if len(tm_list) != 3:
            return False

        hour = tm_list[0]
        minute = tm_list[1]
        second = tm_list[2]

        if hour < 0 or minute < 0 or second < 0:
            return False

        if minute > 60 or second > 60:
            return False

        return True

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False

