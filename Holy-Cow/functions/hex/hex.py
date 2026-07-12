from Holy_Cow.data_other.other import special
from Holy_Cow.functions.hex.data.special_symbols import special_symbols

def is_valid_hex(color_code: str) -> bool:
    try:
        if not color_code.startswith("#"):
            return False

        clr_cd = color_code.split("#")
        if len(clr_cd) != 2:
            return False

        clr_cd_1 = clr_cd[1]
        for i in special:
            if i in clr_cd_1:
                return False

        valid_lengths = [3, 4, 6, 8]
        length_ok = False
        for i in valid_lengths:
            if len(clr_cd_1) == i:
                length_ok = True
                break

        if not length_ok:
            return False

        for char in clr_cd_1:
            if char not in special_symbols:
                return False

        return True

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False