def is_valid_anagram(word_1: str, word_2: str, ignore_register: bool = False) -> bool:
    try:
        if ignore_register:
            word_1 = word_1.lower()
            word_2 = word_2.lower()

        word_1_lst = sorted(word_1)
        word_2_lst = sorted(word_2)

        return word_1_lst == word_2_lst

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False