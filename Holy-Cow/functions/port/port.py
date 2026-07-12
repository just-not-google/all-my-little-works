def is_valid_port(port: int, is_system: bool = False) -> bool:
    try:
        if port < 0:
            return False
        if is_system:
            if not port <= 1023:
                return False
        else:
            if not 1024 <= port <= 65535:
                return False

        return True

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False