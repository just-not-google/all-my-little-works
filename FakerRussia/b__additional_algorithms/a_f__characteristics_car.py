from typing import Dict, List


def characteristics_car(
        value: str | int | float,
        has_car: bool,
        car_model: str,
        lst_cars: Dict[str, List[str]],
        n_a_car: str,
        number_attr: int) -> str | float | int:
    """
    Суть: Вспомогательная функция для получения характеристик автомобиля. Если значение
    еще не сгенерировано, проверяет наличие автомобиля. Если автомобиль есть, извлекает
    соответствующую характеристику (в зависимости от number_attr) из словаря lst_cars по
    модели car_model. Если автомобиля нет, возвращает значение n_a_car. Возвращает
    сгенерированное или существующее значение.
    """
    if value is None:
        if has_car:
            value = lst_cars[car_model][number_attr]
        else:
            value = n_a_car
    return value