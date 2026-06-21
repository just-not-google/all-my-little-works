import random
from string import punctuation
from other_data import MIN_LENGTH_PASS, MAX_LENGTH_PASS
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PhraseGenerator:
    def __init__(self, phrase: str, is_register_replace: bool = False) -> None:
        logger.debug(f"The PhraseGenerator class has been created")
        try:
            if MIN_LENGTH_PASS <= len(phrase) <= MAX_LENGTH_PASS:
                self.phrase = phrase
            else:
                self.phrase = None
                logger.info("The length of the phrase was not verified")
            self.is_register_replace = is_register_replace
        except TypeError:
            self.phrase = None
            self.is_register_replace = False
            logger.warning("Incorrect type")
        except ValueError:
            self.phrase = None
            self.is_register_replace = False
            logger.warning("Incorrect value")

    def _letter_replace(self, letter: str) -> str:
        answer = random.randint(0, 1)
        if answer == 1:
            if letter.isupper():
                return letter.lower()
            elif letter.islower():
                return letter.upper()
            else:
                return letter
        else:
            return letter

    def generate_phrase(self) -> str:
        if self.phrase is None:
            logger.info("The phrase was not set")
            return ""

        lst_word_1 = list(self.phrase)
        lst_word_2 = []

        for letter in lst_word_1:
            random_let = random.randint(0, 1)
            if random_let == 1:
                if self.is_register_replace:
                    lst_word_2.append(f"{self._letter_replace(letter) + random.choice(punctuation)}")
                else:
                    lst_word_2.append(letter + random.choice(punctuation))
            else:
                if self.is_register_replace:
                    lst_word_2.append(self._letter_replace(letter))
                else:
                    lst_word_2.append(letter)
        answer = "".join(lst_word_2)
        return answer

    def __str__(self):
        logger.debug("__str__ PhraseGenerator is called")
        return f"{self.generate_phrase()}"