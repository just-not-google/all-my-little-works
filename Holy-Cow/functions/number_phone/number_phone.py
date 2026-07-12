from Holy_Cow.data_other.other import lowercase, uppercase
from Holy_Cow.functions.number_phone.data_number_phone.special_symbols import special_symbols


def is_valid_number_phone(number_phone: str, country_code: str) -> bool:
    try:
        cleaned_number = number_phone
        for symbol in special_symbols:
            cleaned_number = cleaned_number.replace(symbol, "")

        for char in cleaned_number:
            if char in lowercase or char in uppercase:
                return False

        if not cleaned_number.isdigit():
            return False

        digits = [int(char) for char in cleaned_number]

        if len(digits) == 0:
            return False

        single_code = digits[0]
        double_code = int("".join(map(str, digits[0:2]))) if len(digits) >= 2 else 0
        triple_code = int("".join(map(str, digits[0:3]))) if len(digits) >= 3 else 0

        single_len = len(digits[1:])
        double_len = len(digits[2:])
        triple_len = len(digits[3:])

        if country_code == "af" and triple_code == 93 and triple_len == 9:
            return True
        elif country_code == "al" and triple_code == 355 and triple_len == 9:
            return True
        elif country_code == "dz" and triple_code == 213 and triple_len == 9:
            return True
        elif country_code == "ad" and triple_code == 376 and triple_len == 6:
            return True
        elif country_code == "ao" and triple_code == 244 and triple_len == 9:
            return True
        elif country_code == "ag" and triple_code == 268 and triple_len == 7:
            return True
        elif country_code == "ar" and double_code == 54 and double_len == 10:
            return True
        elif country_code == "am" and triple_code == 374 and triple_len == 8:
            return True
        elif country_code == "au" and double_code == 61 and double_len == 9:
            return True
        elif country_code == "at" and double_code == 43 and double_len == 10:
            return True
        elif country_code == "az" and triple_code == 994 and triple_len == 9:
            return True
        elif country_code == "bs" and triple_code == 242 and triple_len == 7:
            return True
        elif country_code == "bh" and triple_code == 973 and triple_len == 8:
            return True
        elif country_code == "bd" and triple_code == 880 and triple_len == 10:
            return True
        elif country_code == "bb" and triple_code == 246 and triple_len == 7:
            return True
        elif country_code == "by" and triple_code == 375 and triple_len == 9:
            return True
        elif country_code == "be" and double_code == 32 and double_len == 9:
            return True
        elif country_code == "bz" and triple_code == 501 and triple_len == 7:
            return True
        elif country_code == "bj" and triple_code == 229 and triple_len == 8:
            return True
        elif country_code == "bt" and triple_code == 975 and triple_len == 8:
            return True
        elif country_code == "bo" and triple_code == 591 and triple_len == 8:
            return True
        elif country_code == "ba" and triple_code == 387 and triple_len == 8:
            return True
        elif country_code == "bw" and triple_code == 267 and triple_len == 7:
            return True
        elif country_code == "br" and double_code == 55 and (double_len == 10 or double_len == 11):
            return True
        elif country_code == "bn" and triple_code == 673 and triple_len == 7:
            return True
        elif country_code == "bg" and triple_code == 359 and triple_len == 8:
            return True
        elif country_code == "bf" and triple_code == 226 and triple_len == 8:
            return True
        elif country_code == "bi" and triple_code == 257 and triple_len == 8:
            return True
        elif country_code == "cv" and triple_code == 238 and triple_len == 7:
            return True
        elif country_code == "kh" and triple_code == 855 and triple_len == 9:
            return True
        elif country_code == "cm" and triple_code == 237 and triple_len == 9:
            return True
        elif country_code == "ca" and single_code == 1 and single_len == 10:
            return True
        elif country_code == "cf" and triple_code == 236 and triple_len == 8:
            return True
        elif country_code == "td" and triple_code == 235 and triple_len == 8:
            return True
        elif country_code == "cl" and double_code == 56 and double_len == 9:
            return True
        elif country_code == "cn" and double_code == 86 and double_len == 11:
            return True
        elif country_code == "co" and double_code == 57 and double_len == 10:
            return True
        elif country_code == "km" and triple_code == 269 and triple_len == 7:
            return True
        elif country_code == "cg" and triple_code == 242 and triple_len == 9:
            return True
        elif country_code == "cd" and triple_code == 243 and triple_len == 9:
            return True
        elif country_code == "cr" and triple_code == 506 and triple_len == 8:
            return True
        elif country_code == "ci" and triple_code == 225 and triple_len == 10:
            return True
        elif country_code == "hr" and triple_code == 385 and triple_len == 8:
            return True
        elif country_code == "cu" and triple_code == 53 and triple_len == 8:
            return True
        elif country_code == "cy" and triple_code == 357 and triple_len == 8:
            return True
        elif country_code == "cz" and triple_code == 420 and triple_len == 9:
            return True
        elif country_code == "dk" and double_code == 45 and double_len == 8:
            return True
        elif country_code == "dj" and triple_code == 253 and triple_len == 8:
            return True
        elif country_code == "dm" and triple_code == 767 and triple_len == 7:
            return True
        elif country_code == "do" and triple_code == 809 and triple_len == 7:
            return True
        elif country_code == "ec" and triple_code == 593 and triple_len == 8:
            return True
        elif country_code == "eg" and double_code == 20 and double_len == 10:
            return True
        elif country_code == "sv" and triple_code == 503 and triple_len == 8:
            return True
        elif country_code == "gq" and triple_code == 240 and triple_len == 9:
            return True
        elif country_code == "er" and triple_code == 291 and triple_len == 7:
            return True
        elif country_code == "ee" and triple_code == 372 and triple_len == 7:
            return True
        elif country_code == "sz" and triple_code == 268 and triple_len == 8:
            return True
        elif country_code == "et" and triple_code == 251 and triple_len == 9:
            return True
        elif country_code == "fj" and triple_code == 679 and triple_len == 7:
            return True
        elif country_code == "fi" and triple_code == 358 and triple_len == 9:
            return True
        elif country_code == "fr" and double_code == 33 and double_len == 9:
            return True
        elif country_code == "ga" and triple_code == 241 and triple_len == 7:
            return True
        elif country_code == "gm" and triple_code == 220 and triple_len == 7:
            return True
        elif country_code == "ge" and triple_code == 995 and triple_len == 9:
            return True
        elif country_code == "de" and double_code == 49 and (double_len == 10 or double_len == 11):
            return True
        elif country_code == "gh" and triple_code == 233 and triple_len == 9:
            return True
        elif country_code == "gr" and double_code == 30 and double_len == 10:
            return True
        elif country_code == "gd" and triple_code == 473 and triple_len == 7:
            return True
        elif country_code == "gt" and triple_code == 502 and triple_len == 8:
            return True
        elif country_code == "gn" and triple_code == 224 and triple_len == 9:
            return True
        elif country_code == "gw" and triple_code == 245 and triple_len == 7:
            return True
        elif country_code == "gy" and triple_code == 592 and triple_len == 7:
            return True
        elif country_code == "ht" and triple_code == 509 and triple_len == 8:
            return True
        elif country_code == "hn" and triple_code == 504 and triple_len == 8:
            return True
        elif country_code == "hu" and double_code == 36 and double_len == 9:
            return True
        elif country_code == "is" and triple_code == 354 and triple_len == 7:
            return True
        elif country_code == "in" and double_code == 91 and double_len == 10:
            return True
        elif country_code == "id" and double_code == 62 and (double_len == 9 or double_len == 10 or double_len == 11):
            return True
        elif country_code == "ir" and triple_code == 98 and triple_len == 10:
            return True
        elif country_code == "iq" and triple_code == 964 and triple_len == 10:
            return True
        elif country_code == "ie" and triple_code == 353 and triple_len == 9:
            return True
        elif country_code == "il" and triple_code == 972 and triple_len == 9:
            return True
        elif country_code == "it" and double_code == 39 and (double_len == 9 or double_len == 10):
            return True
        elif country_code == "jm" and triple_code == 876 and triple_len == 7:
            return True
        elif country_code == "jp" and double_code == 81 and (double_len == 9 or double_len == 10):
            return True
        elif country_code == "jo" and triple_code == 962 and triple_len == 9:
            return True
        elif country_code == "kz" and triple_code == 77 and triple_len == 9:
            return True
        elif country_code == "ke" and triple_code == 254 and triple_len == 9:
            return True
        elif country_code == "ki" and triple_code == 686 and triple_len == 8:
            return True
        elif country_code == "kp" and triple_code == 850 and triple_len == 10:
            return True
        elif country_code == "kr" and double_code == 82 and (
                double_len == 8 or double_len == 9 or double_len == 10 or double_len == 11):
            return True
        elif country_code == "kw" and triple_code == 965 and triple_len == 8:
            return True
        elif country_code == "kg" and triple_code == 996 and triple_len == 9:
            return True
        elif country_code == "la" and triple_code == 856 and triple_len == 10:
            return True
        elif country_code == "lv" and triple_code == 371 and triple_len == 8:
            return True
        elif country_code == "lb" and triple_code == 961 and triple_len == 8:
            return True
        elif country_code == "ls" and triple_code == 266 and triple_len == 8:
            return True
        elif country_code == "lr" and triple_code == 231 and triple_len == 8:
            return True
        elif country_code == "ly" and triple_code == 218 and triple_len == 9:
            return True
        elif country_code == "li" and triple_code == 423 and triple_len == 9:
            return True
        elif country_code == "lt" and triple_code == 370 and triple_len == 8:
            return True
        elif country_code == "lu" and triple_code == 352 and triple_len == 9:
            return True
        elif country_code == "mg" and triple_code == 261 and triple_len == 9:
            return True
        elif country_code == "mw" and triple_code == 265 and triple_len == 9:
            return True
        elif country_code == "my" and double_code == 60 and double_len == 9:
            return True
        elif country_code == "mv" and triple_code == 960 and triple_len == 7:
            return True
        elif country_code == "ml" and triple_code == 223 and triple_len == 8:
            return True
        elif country_code == "mt" and triple_code == 356 and triple_len == 8:
            return True
        elif country_code == "mh" and triple_code == 692 and triple_len == 7:
            return True
        elif country_code == "mr" and triple_code == 222 and triple_len == 8:
            return True
        elif country_code == "mu" and triple_code == 230 and triple_len == 8:
            return True
        elif country_code == "mx" and double_code == 52 and double_len == 10:
            return True
        elif country_code == "fm" and triple_code == 691 and triple_len == 7:
            return True
        elif country_code == "md" and triple_code == 373 and triple_len == 8:
            return True
        elif country_code == "mc" and triple_code == 377 and triple_len == 9:
            return True
        elif country_code == "mn" and triple_code == 976 and triple_len == 8:
            return True
        elif country_code == "me" and triple_code == 382 and triple_len == 8:
            return True
        elif country_code == "ma" and triple_code == 212 and triple_len == 9:
            return True
        elif country_code == "mz" and triple_code == 258 and triple_len == 9:
            return True
        elif country_code == "mm" and triple_code == 95 and triple_len == 9:
            return True
        elif country_code == "na" and triple_code == 264 and triple_len == 9:
            return True
        elif country_code == "nr" and triple_code == 674 and triple_len == 7:
            return True
        elif country_code == "np" and triple_code == 977 and triple_len == 10:
            return True
        elif country_code == "nl" and double_code == 31 and double_len == 9:
            return True
        elif country_code == "nz" and double_code == 64 and double_len == 9:
            return True
        elif country_code == "ni" and triple_code == 505 and triple_len == 8:
            return True
        elif country_code == "ne" and triple_code == 227 and triple_len == 8:
            return True
        elif country_code == "ng" and triple_code == 234 and triple_len == 10:
            return True
        elif country_code == "mk" and triple_code == 389 and triple_len == 8:
            return True
        elif country_code == "no" and double_code == 47 and double_len == 8:
            return True
        elif country_code == "om" and triple_code == 968 and triple_len == 8:
            return True
        elif country_code == "pk" and triple_code == 92 and triple_len == 10:
            return True
        elif country_code == "pw" and triple_code == 680 and triple_len == 7:
            return True
        elif country_code == "ps" and triple_code == 970 and triple_len == 9:
            return True
        elif country_code == "pa" and triple_code == 507 and triple_len == 8:
            return True
        elif country_code == "pg" and triple_code == 675 and triple_len == 8:
            return True
        elif country_code == "py" and triple_code == 595 and triple_len == 9:
            return True
        elif country_code == "pe" and double_code == 51 and double_len == 9:
            return True
        elif country_code == "ph" and double_code == 63 and double_len == 10:
            return True
        elif country_code == "pl" and double_code == 48 and double_len == 9:
            return True
        elif country_code == "pt" and triple_code == 351 and triple_len == 9:
            return True
        elif country_code == "qa" and triple_code == 974 and triple_len == 8:
            return True
        elif country_code == "ro" and double_code == 40 and double_len == 9:
            return True
        elif country_code == "ru" and single_code == 7 and single_len == 10:
            return True
        elif country_code == "rw" and triple_code == 250 and triple_len == 9:
            return True
        elif country_code == "kn" and triple_code == 869 and triple_len == 7:
            return True
        elif country_code == "lc" and triple_code == 758 and triple_len == 7:
            return True
        elif country_code == "vc" and triple_code == 784 and triple_len == 7:
            return True
        elif country_code == "ws" and triple_code == 685 and triple_len == 7:
            return True
        elif country_code == "sm" and triple_code == 378 and triple_len == 10:
            return True
        elif country_code == "st" and triple_code == 239 and triple_len == 7:
            return True
        elif country_code == "sa" and triple_code == 966 and triple_len == 9:
            return True
        elif country_code == "sn" and triple_code == 221 and triple_len == 9:
            return True
        elif country_code == "rs" and triple_code == 381 and triple_len == 8:
            return True
        elif country_code == "sc" and triple_code == 248 and triple_len == 7:
            return True
        elif country_code == "sl" and triple_code == 232 and triple_len == 8:
            return True
        elif country_code == "sg" and double_code == 65 and double_len == 8:
            return True
        elif country_code == "sk" and triple_code == 421 and triple_len == 9:
            return True
        elif country_code == "si" and triple_code == 386 and triple_len == 8:
            return True
        elif country_code == "sb" and triple_code == 677 and triple_len == 7:
            return True
        elif country_code == "so" and triple_code == 252 and triple_len == 8:
            return True
        elif country_code == "za" and double_code == 27 and double_len == 9:
            return True
        elif country_code == "ss" and triple_code == 211 and triple_len == 9:
            return True
        elif country_code == "es" and double_code == 34 and double_len == 9:
            return True
        elif country_code == "lk" and triple_code == 94 and triple_len == 9:
            return True
        elif country_code == "sd" and triple_code == 249 and triple_len == 9:
            return True
        elif country_code == "sr" and triple_code == 597 and triple_len == 7:
            return True
        elif country_code == "se" and double_code == 46 and double_len == 9:
            return True
        elif country_code == "ch" and double_code == 41 and double_len == 9:
            return True
        elif country_code == "sy" and triple_code == 963 and triple_len == 9:
            return True
        elif country_code == "tw" and triple_code == 886 and triple_len == 9:
            return True
        elif country_code == "tj" and triple_code == 992 and triple_len == 9:
            return True
        elif country_code == "tz" and triple_code == 255 and triple_len == 9:
            return True
        elif country_code == "th" and double_code == 66 and double_len == 9:
            return True
        elif country_code == "tl" and triple_code == 670 and triple_len == 8:
            return True
        elif country_code == "tg" and triple_code == 228 and triple_len == 8:
            return True
        elif country_code == "to" and triple_code == 676 and triple_len == 7:
            return True
        elif country_code == "tt" and triple_code == 868 and triple_len == 7:
            return True
        elif country_code == "tn" and triple_code == 216 and triple_len == 8:
            return True
        elif country_code == "tr" and double_code == 90 and double_len == 10:
            return True
        elif country_code == "tm" and triple_code == 993 and triple_len == 8:
            return True
        elif country_code == "tv" and triple_code == 688 and triple_len == 6:
            return True
        elif country_code == "ug" and triple_code == 256 and triple_len == 9:
            return True
        elif country_code == "ua" and triple_code == 380 and triple_len == 9:
            return True
        elif country_code == "ae" and triple_code == 971 and triple_len == 9:
            return True
        elif country_code == "gb" and double_code == 44 and (double_len == 10 or double_len == 11):
            return True
        elif country_code == "us" and single_code == 1 and single_len == 10:
            return True
        elif country_code == "uy" and triple_code == 598 and triple_len == 8:
            return True
        elif country_code == "uz" and triple_code == 998 and triple_len == 9:
            return True
        elif country_code == "vu" and triple_code == 678 and triple_len == 7:
            return True
        elif country_code == "va" and triple_code == 379 and triple_len == 10:
            return True
        elif country_code == "ve" and double_code == 58 and double_len == 10:
            return True
        elif country_code == "vn" and double_code == 84 and (double_len == 9 or double_len == 10):
            return True
        elif country_code == "ye" and triple_code == 967 and triple_len == 9:
            return True
        elif country_code == "zm" and triple_code == 260 and triple_len == 9:
            return True
        elif country_code == "zw" and triple_code == 263 and triple_len == 9:
            return True

        return False

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False