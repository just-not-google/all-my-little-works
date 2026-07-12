from Holy_Cow.functions.url.data.uri_schemes import uri_schemes
from Holy_Cow.functions.port.port import is_valid_port


def is_valid_url(url: str, uri_schem: list[str] = uri_schemes) -> bool:
    try:
        if not url or "://" not in url:
            return False

        scheme, rest = url.split("://", 1)
        if scheme not in uri_schem:
            return False

        if "/" in rest:
            host_part, path_part = rest.split("/", 1)
        else:
            host_part, path_part = rest, ""

        if ":" in host_part:
            host, port_str = host_part.split(":", 1)
            try:
                port = int(port_str)
                if not is_valid_port(port, False):
                    return False
            except ValueError:
                return False
        else:
            host = host_part

        if not host or ".." in host:
            return False

        if "." in host:
            domain_parts = host.split(".")
            for part in domain_parts:
                if not part or part.startswith("-") or part.endswith("-"):
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