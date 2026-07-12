from Holy_Cow.functions.file_sizes.data.units_to_bytes import units_to_bytes

def is_valid_file_sizes(original_size: int, original_unit: str, changed_size: int, changed_unit: str) -> bool:
    try:
        original_unit = original_unit.lower()
        changed_unit = changed_unit.lower()

        if original_unit not in units_to_bytes or changed_unit not in units_to_bytes:
            return False

        if original_size < 0 or changed_size < 0:
            return False

        original_bytes = original_size * units_to_bytes[original_unit]
        changed_bytes = changed_size * units_to_bytes[changed_unit]

        return abs(original_bytes - changed_bytes) < 1e-9

    except TypeError:
        return False
    except KeyError:
        return False
    except ValueError:
        return False
    except Exception:
        return False