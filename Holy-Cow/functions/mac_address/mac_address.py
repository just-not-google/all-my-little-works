from Holy_Cow.functions.mac_address.data_mac_address.special_symbols import hex_upper

def is_valid_mac_address(mac_address: str) -> bool:
    try:
        if len(mac_address) not in [12, 14, 17]:
            return False

        cleaned = mac_address.replace(":", "").replace("-", "").replace(".", "")

        if len(cleaned) != 12:
            return False

        for char in cleaned:
            if char.upper() not in hex_upper:
                return False

        return True

    except TypeError:
        return False
    except AttributeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False