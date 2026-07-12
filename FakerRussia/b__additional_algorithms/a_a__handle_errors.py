from json import JSONDecodeError


def handle_errors(func):
    """
    Суть: Декоратор для обработки исключений в методах генераторов. Перехватывает
    различные типы исключений, которые могут возникнуть при генерации данных
    (ошибки доступа к данным, некорректные значения, ошибки файловой системы и другие),
    и возвращает понятные текстовые сообщения вместо возникновения ошибок. Позволяет
    обеспечить стабильную работу генераторов даже при отсутствии или некорректности данных.
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "Информация отсутствует"
        except ValueError:
            return "Некорректные данные"
        except IndexError:
            return "Данные не найдены"
        except AttributeError:
            return "Ошибка в данных"
        except TypeError:
            return "Ошибка обработки"
        except JSONDecodeError:
            return "Ошибка чтения данных"
        except ZeroDivisionError:
            return "Ошибка вычислений"
        except FileNotFoundError:
            return "Файл не найден"
        except Exception:
            return "Нет данных"
    return wrapper