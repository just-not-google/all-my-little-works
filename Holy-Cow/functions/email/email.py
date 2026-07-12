from Holy_Cow.functions.email.data_email.email_domains import email_domains
from Holy_Cow.data_other.other import lowercase, digits, uppercase
from Holy_Cow.functions.email.data_email.special_symbols import AT_SIGN, DASH
from Holy_Cow.data_other.other import DOT


def is_valid_email(email: str) -> bool:
    try:
        if not email or len(email) > 254:
            return False

        if email.count(AT_SIGN) != 1:
            return False

        local_part, domain_part = email.split(AT_SIGN)

        if len(local_part) < 1 or len(local_part) > 64:
            return False
        if local_part.startswith(DOT) or local_part.endswith(DOT):
            return False
        if '..' in local_part:
            return False

        for char in local_part:
            if char not in lowercase + uppercase + digits + "!#$%&'*+/=?^_`{|}~-.":
                return False

        if len(domain_part) < 1 or len(domain_part) > 253:
            return False

        domain_labels = domain_part.split(DOT)
        if len(domain_labels) < 2:
            return False

        tld = domain_labels[-1]
        if len(tld) < 2:
            return False
        if tld.lower() not in email_domains:
            return False

        domain_name = DOT.join(domain_labels[:-1])

        for label in domain_name.split(DOT):
            if not label:
                return False
            if label.startswith(DASH) or label.endswith(DASH):
                return False
            if len(label) > 63:
                return False
            for char in label:
                if char not in lowercase + uppercase + digits + DASH:
                    return False

        return True

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False