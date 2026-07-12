import random
from typing import Optional, List


def choice_value(
        value: Optional[str],
        variants: List[str]) -> str:
    """
    Суть: Вспомогательная функция для выбора случайного значения из списка вариантов.
    Если переданное значение отсутствует (None), выбирает случайный элемент из списка
    variants. Если значение уже существует, возвращает его без изменений. Используется
    в генераторах для обеспечения согласованности данных при повторных обращениях к
    одному свойству.
    """
    if value is None:
        value = random.choice(variants)
    return value