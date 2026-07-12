from Holy_Cow.functions.swift_bic.data.country_code import COUNTRIES
from Holy_Cow.data_other.other import special


def is_valid_swift_bic(code: str) -> bool:
    try:
        if " " in code:
            code = code.replace(" ", "")

        if len(code) not in (8, 11):
            return False

        institution_code = code[:4]
        country_code = code[4:6]
        location_code = code[6:8]

        branch_code = None
        if len(code) == 11:
            branch_code = code[8:11]

        if not institution_code.isupper() or not country_code.isupper() or not location_code.isupper():
            return False

        if branch_code and not branch_code.isupper():
            return False

        for part in [institution_code, country_code, location_code]:
            for char in part:
                if char in special:
                    return False

        if branch_code:
            for char in branch_code:
                if char in special:
                    return False

        if country_code not in COUNTRIES:
            return False

        return True

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False


