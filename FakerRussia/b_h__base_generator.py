import json
import os


class BaseGenerator:
    """
    Суть: Базовый класс для всех генераторов данных проекта. Обеспечивает общую функциональность
    для загрузки данных из JSON-файлов, предоставляет доступ к общим константам и настройкам,
    используемым во всех дочерних генераторах (биографии, адреса, контактов, документов, финансов,
    работы, транспорта). Загружает данные из файла 'a__data/other/other_data.json', а также
    дополнительные данные для малолетних возрастов и заболеваний.
    """

    def __init__(self):
        """
        Суть: Инициализация базового генератора. При создании экземпляра автоматически загружает
        все общие данные из JSON-файлов через метод _load_all_data, делая их доступными для всех
        дочерних классов.
        """
        self._load_all_data()

    def _get_data_path(self, relative_path):
        """
        Суть: Формирование абсолютного пути к файлу данных. Преобразует относительный путь к
        файлу (относительно расположения текущего файла) в абсолютный путь для корректной
        загрузки данных независимо от места запуска программы.
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, relative_path)

    def _load_json(self, filepath):
        """
        Суть: Загрузка JSON-файла с данными. Открывает файл по указанному пути, считывает его
        содержимое и возвращает десериализованный объект Python (обычно словарь или список).
        """
        full_path = self._get_data_path(filepath)
        with open(full_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _load_all_data(self):
        """
        Суть: Загрузка всех общих данных, используемых генераторами. Загружает основные константы
        и настройки из файла 'a__data/other/other_data.json', ответы для малолетних из файла
        'a__data/small_age/small_age.json', список заболеваний из файла 'a__data/disease/diseases.json'.
        Сохраняет все данные в атрибуты класса для использования дочерними генераторами.
        """
        other_data = self._load_json('a__data/other/other_data.json')
        self.GENDER = other_data.get("GENDER", ["male", "female"])
        self.TYPE_BUILDINGS = other_data.get("TYPE_BUILDINGS", ["д.", "корп."])
        self.WEIGHT_FACTORS_1 = other_data.get("WEIGHT_FACTORS_1", [7, 2, 4, 10, 3, 5, 9, 4, 6, 8])
        self.WEIGHT_FACTORS_2 = other_data.get("WEIGHT_FACTORS_2", [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8])
        self.COUNTRY_CODE = other_data.get("COUNTRY_CODE", "+7")
        self.PREFIX = other_data.get("PREFIX")
        self.LEVEL_WORK = other_data.get("LEVEL_WORK", [])
        self.N_A = other_data.get("N_A", "N/A")
        self.LETTERS_NUMBER_CAR = other_data.get("LETTERS_NUMBER_CAR", [])
        self.ZODIAC_SIGNS = other_data.get("ZODIAC_SIGNS", [])
        self.STRING_IPv6 = other_data.get("STRING_IPv6")
        self.N_A_CAR = other_data.get("N_A_CAR")
        self.GAMING_PLATFORMS = other_data.get("GAMING_PLATFORMS", [])
        self.HEARING_STATUS = other_data.get("HEARING_STATUS", [])
        self.DISABILITY_DEGREES = other_data.get("DISABILITY_DEGREES", [])
        self.PENSION = other_data.get("PENSION")
        self.AGE_MAJORITY = other_data.get("AGE_MAJORITY")
        self.AGE_FOR_CARD = other_data.get("AGE_FOR_CARD")
        self.CARD_TYPE = other_data.get("CARD_TYPE", [])
        self.N_A_STUDY_PLACE = other_data.get("N_A_STUDY_PLACE")
        small_age_data = self._load_json('a__data/small_age/small_age.json')
        self.SMALL_AGE_ANSWERS = small_age_data.get("SMALL_AGE_ANSWERS", [])
        diseases_data = self._load_json('a__data/disease/diseases.json')
        self.DISEASES = diseases_data.get("DISEASES", {})