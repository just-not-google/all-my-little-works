def check_spouse(attr_name: str):
    """
    Суть: Декоратор для методов, возвращающих данные о супруге. Проверяет наличие супруга
    через метод _check_spouse_exists. Если супруг отсутствует, устанавливает значение указанного
    атрибута в сообщение об отсутствии супруга (no_spouse_message) и возвращает это сообщение.
    Если супруг есть, вызывает оригинальный метод для генерации данных.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if not self._check_spouse_exists():
                setattr(self._data, attr_name, self._data.no_spouse_message)
                return self._data.no_spouse_message
            return func(self, *args, **kwargs)
        return wrapper
    return decorator