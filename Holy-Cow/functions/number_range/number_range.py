def is_valid_number_range(number_lst: list[int], min_value: int, max_value: int) -> list[bool]:
    try:
        range_lst = []
        bool_lst = []
        for i in range(min_value, max_value + 1):
            range_lst.append(i)
        for j in number_lst:
            if j in range_lst:
                bool_lst.append(True)
            else:
                bool_lst.append(False)

        return bool_lst

    except TypeError:
        return [False] * len(number_lst)
    except AttributeError:
        return [False] * len(number_lst)
    except Exception:
        return [False] * len(number_lst)