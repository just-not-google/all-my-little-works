import random
from typing import List, Dict, Optional, Tuple


def choice_machine_family(
        value: Optional[str],
        age: int,
        gender: str,
        marital_status: str,
        answer_1: List[str],
        gender_answer: List[str],
        male_1: List[str],
        female_1: List[str],
        ml: List[str] | Dict[str, str],
        fml: List[str] | Dict[str, str]) -> Tuple[Optional[str], bool]:
    """
    Суть: Вспомогательная функция для генерации ФИО супруга в зависимости от пола человека,
    его семейного статуса и возраста. Определяет, нужно ли генерировать данные о супруге,
    выбирает соответствующий список имен/фамилий/отчеств (в зависимости от пола супруга) и
    определяет, состоял ли супруг ранее в браке. Возвращает сгенерированное значение и флаг
    о предыдущем браке.
    """
    was_married = False
    if value is not None:
        return value, was_married
    if age < 18:
        return answer_1[5], False
    if gender == gender_answer[0]:
        if marital_status == male_1[0] or marital_status == answer_1[5]:
            return None, False
    else:
        if marital_status == female_1[0] or marital_status == answer_1[5]:
            return None, False
    if gender == gender_answer[0]:
        if isinstance(fml, list):
            value = random.choice(fml)
        elif isinstance(fml, dict):
            value = random.choice(list(fml.keys()))
        was_married = marital_status in male_1[2:]
    else:
        if isinstance(ml, list):
            value = random.choice(ml)
        elif isinstance(ml, dict):
            value = random.choice(list(ml.keys()))
        was_married = marital_status in female_1[2:]
    return value, was_married