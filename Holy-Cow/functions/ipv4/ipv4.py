from Holy_Cow.data_other.other import DOT


def is_valid_ipv4(ipv4: str) -> bool:
    try:
        if " " in ipv4:
            ipv4 = ipv4.replace(" ", DOT)

        parts = ipv4.split(DOT)

        if len(parts) != 4:
            return False

        for part in parts:
            if not part:
                return False

            num = int(part)
            if num < 0 or num > 255:
                return False

            if len(part) > 1 and part.startswith('0'):
                return False

        return True

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False