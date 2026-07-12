def is_valid_ipv6(ipv6: str) -> bool:
    try:
        if not ipv6 or not isinstance(ipv6, str):
            return False

        ipv6 = ipv6.strip()

        valid_chars = set('0123456789abcdefABCDEF:')
        if not all(c in valid_chars for c in ipv6):
            return False

        if ipv6 == '::':
            return True

        if ipv6 == '::1':
            return True


        if ':::' in ipv6:
            return False

        parts = ipv6.split(':')

        if len(parts) < 3 or len(parts) > 8:
            return False

        double_colon_count = ipv6.count('::')
        if double_colon_count > 1:
            return False

        has_compression = double_colon_count == 1

        if has_compression:
            compression_index = parts.index('')

            left_parts = parts[:compression_index]
            right_parts = parts[compression_index + 1:]

            left_parts = [p for p in left_parts if p != '']
            right_parts = [p for p in right_parts if p != '']

            for part in left_parts + right_parts:
                if len(part) > 4:
                    return False

            total_groups = len(left_parts) + len(right_parts)
            if total_groups > 7:
                return False
            if total_groups < 1 and ipv6 != '::':
                return False

            all_parts = left_parts + right_parts
            for part in all_parts:
                if not part:
                    return False
                try:
                    int(part, 16)
                except ValueError:
                    return False

            return True

        else:
            if len(parts) != 8:
                return False

            for part in parts:
                if not part:
                    return False

                if len(part) > 4:
                    return False

                try:
                    int(part, 16)
                except ValueError:
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