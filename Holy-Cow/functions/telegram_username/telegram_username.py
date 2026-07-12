from Holy_Cow.functions.telegram_username.data.special_characters import special_characters
from Holy_Cow.functions.telegram_username.data.blocked_usernames_words import blocked_usernames, blocked_words

def is_valid_telegram_username(username: str) -> bool:
    try:
        if not username.startswith("@"):
            return False

        username_1 = username.split("@")

        if not (5 <= len(username_1[1]) <= 32):
            return False

        if username_1[1].isdigit():
            return False

        if len(set(username_1[1])) < 3:
            return False

        for i in username_1[1]:
            if i in special_characters:
                return False

        for i in blocked_usernames:
            if i in username_1[1]:
                return False

        for i in blocked_words:
            if i in username_1[1]:
                return False

        return True

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False