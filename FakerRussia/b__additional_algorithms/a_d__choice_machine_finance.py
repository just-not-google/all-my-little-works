from typing import List, Dict


def choice_machine_finance(
        inn_kpp_bank: str,
        age: int,
        age_for_card: int,
        small_age: List[str],
        banks: List[str],
        bank_var: Dict[str, List[str]],
        variant: int,
        visualization: bool = False,) -> List[str] | str:
    """
    Суть: Вспомогательная функция для генерации списка ИНН или КПП банков.
    Если данные еще не сгенерированы, проверяет возраст: для лиц младше
    age_for_card возвращает соответствующий ответ из small_age. Для остальных
    формирует список ИНН или КПП (в зависимости от параметра variant: 0 - ИНН,
    1 - КПП) для каждого банка из списка banks, извлекая данные из словаря bank_var.
    При необходимости возвращает строку с элементами через запятую.
    """
    if inn_kpp_bank is None:
        if age < age_for_card:
            inn_kpp_bank = small_age[10]
        lst_inn = []
        for bank_name in banks:
            lst_inn.append(bank_var[bank_name][variant])
        inn_kpp_bank = lst_inn
    if visualization:
        return ", ".join(inn_kpp_bank)
    return inn_kpp_bank