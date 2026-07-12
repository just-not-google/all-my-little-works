from Holy_Cow.functions.adulthood.data.adulthood_country_code import countries_age

def is_valid_adulthood(age: int, country_code: str) -> bool:
    try:
        if country_code in countries_age:
            return age >= countries_age[country_code]

        return False

    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False