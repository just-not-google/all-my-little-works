import logging

def log_errors(func):
    def wrapper(self, *args, **kwargs):
        method_name = func.__name__
        try:
            return func(self, *args, **kwargs)
        except TypeError:
            self.logger2.error(f"TypeError в {method_name}")
            return "Введён неправильный тип данных"
        except ValueError:
            self.logger2.error(f"ValueError в {method_name}")
            return "Введены неправильные данные"
        except Exception as e:
            self.logger2.exception(f"Неизвестная ошибка в {method_name}: {e}")
            return f"Неизвестная ошибка: {str(e)[:100]}..."
    return wrapper

class MineVersionDataBase:
    def __init__(self):
        self.database = {}
        self.logger2 = logging.getLogger(__name__)
        self.logger2.setLevel(logging.INFO)
        handler2 = logging.FileHandler(f"{__name__}.log", mode="w")
        formatter2 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        handler2.setFormatter(formatter2)
        self.logger2.addHandler(handler2)

    def _validate_database(self) -> bool:
        if len(self.database) < 1:
            self.logger2.error("Произошла ошибка - validate_database")
            return False
        self.logger2.info("Всё прошло успешно - validate_database")
        return True

    def _column_exists(self, column: str) -> bool:
        if not column:
            self.logger2.error("Произошла ошибка - column_exists")
            return False
        if column in self.database:
            self.logger2.warning("Всё прошло успешно - column_exists")
            return True
        self.logger2.error("Произошла ошибка - column_exists")
        return False

    @log_errors
    def add_column(self, column: str) -> str:
        if len(column) < 1:
            raise ValueError
        self.database[column] = []
        self.logger2.info("Всё прошло успешно - add_column")
        return "Колонка была добавлена"

    @log_errors
    def add_columns(self, columns: list[str]) -> str:
        if len(columns) < 1:
            raise ValueError
        for column in columns:
            if len(column) < 1:
                raise ValueError
            self.database[column] = []
        self.logger2.info("Всё прошло успешно - add_columns")
        return "Колонки были добавлены"

    @log_errors
    def add_data(self, data: str, column: str) -> str:
        if len(data) < 1 or len(column) < 1:
            raise ValueError
        if not self._column_exists(column):
            raise ValueError
        self.database[column].append(data)
        self.logger2.info("Всё прошло успешно - add_data")
        return "Были добавлены все нужные данные в столбец"

    @log_errors
    def add_datas(self, datas: list[str], column: str) -> str:
        if not self._column_exists(column):
            raise ValueError
        if len(column) < 1:
            raise ValueError
        for data in datas:
            if len(data) < 1:
                raise ValueError
            self.database[column].append(data)
        self.logger2.info("Всё прошло успешно - add_datas")
        return "Были добавлены все нужные данные в столбец"

    @log_errors
    def replace_datas(self, column: str, datas: list[str]) -> str:
        if not self._validate_database():
            raise ValueError
        if not self._column_exists(column):
            raise ValueError
        if len(column) < 1:
            raise ValueError
        for data in datas:
            if len(data) < 1:
                raise ValueError
        self.database[column] = datas
        self.logger2.info("Всё прошло успешно - replace_datas")
        return "Все данные в определённом столбце были заменены"

    @log_errors
    def delete_datas_column(self, column: str) -> str:
        if not self._validate_database():
            raise ValueError
        if not self._column_exists(column):
            raise ValueError
        if len(column) < 1:
            raise ValueError
        self.database[column] = []
        self.logger2.info("Всё прошло успешно - delete_datas_column")
        return "Были убраны все данные из нужного столбца"

    @log_errors
    def delete_datas_columns(self, columns: list[str]) -> str:
        if not self._validate_database():
            raise ValueError
        for column in columns:
            if not self._column_exists(column):
                raise ValueError
            if len(column) < 1:
                raise ValueError
            self.database[column] = []
        self.logger2.info("Всё прошло успешно - delete_datas_columns")
        return "Были убраны все данные из всех нужных столбцов"

    @log_errors
    def delete_all_column(self, column: str) -> str:
        if not self._validate_database():
            raise ValueError
        if not self._column_exists(column):
            raise ValueError
        if len(column) < 1:
            raise ValueError
        self.database.pop(column)
        self.logger2.info("Всё прошло успешно - delete_all_column")
        return "Столбец был убран"

    @log_errors
    def delete_all_columns(self, columns: list[str]) -> str:
        if not self._validate_database():
            raise ValueError
        for column in columns:
            if not self._column_exists(column):
                raise ValueError
            if len(column) < 1:
                raise ValueError
            self.database.pop(column)
        self.logger2.info("Всё прошло успешно - delete_all_columns")
        return "Все столбцы были убраны"

    @log_errors
    def get_data(self, column: str, number_column: int) -> str:
        if not self._validate_database():
            raise ValueError
        if not self._column_exists(column):
            raise ValueError
        if len(column) < 1:
            raise ValueError
        if number_column < 0:
            raise ValueError
        if number_column >= len(self.database[column]):
            raise ValueError
        self.logger2.info("Всё прошло успешно - get_data")
        return self.database[column][number_column]

    @log_errors
    def get_column(self, column: str) -> str:
        if not self._validate_database():
            raise ValueError
        if not self._column_exists(column):
            raise ValueError
        if len(column) < 1:
            raise ValueError
        answer = "\n".join(self.database[column])
        self.logger2.info("Всё прошло успешно - get_column")
        return answer

    @log_errors
    def get_all_data(self) -> str:
        if not self._validate_database():
            raise ValueError
        answer_lst = []
        for key, value in self.database.items():
            answer_lst.append(f"{key} - {', '.join(value)}\n")
        self.logger2.info("Всё прошло успешно - get_all_data")
        return "".join(answer_lst)
