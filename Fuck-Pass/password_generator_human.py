import random
from string import punctuation
from other_data import common_password_bases, DEFAULT_OPTION, MAX_LENGTH_PASS
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class HumanGenerator:
    def __init__(self, length: int = None, identical_value: int = False) -> None:
        self.identical_value = identical_value
        self.length = length
        logger.debug(f"The HumanGenerator class has been created")

    def _is_valid(self, length: int) -> bool:
        if self.identical_value:
            length = self.length
        try:
            if DEFAULT_OPTION <= length:
                return True
            return False
        except TypeError:
            logger.warning("Incorrect type")
            return False
        except ValueError:
            logger.warning("Incorrect value")
            return False

    def _generator_digits(self, length: int) -> str:
        if not (self._is_valid(length)):
            logger.info("Word generation skipped — incorrect length")
            return ""

        min_value = int("1" + f"0" * (length - 1))
        max_value = int("9" * length)
        answer = random.randint(min_value, max_value)

        if not (len(str(answer)) <= MAX_LENGTH_PASS):
            return ""
        return str(answer)

    def _generator_word(self, length: int) -> str:
        if not (self._is_valid(length)):
            logger.info("Digit generation skipped — incorrect length")
            return ""

        max_len = len(sorted(common_password_bases, key=len)[-1])
        if max_len < length:
            logger.info("The final output length is greater than the maximum value")
            return ""

        right_words = []
        for word in common_password_bases:
            if len(word) == length:
                right_words.append(word)
        word_answer = random.choice(right_words)
        word_result = []

        for i in word_answer:
            answer = random.randint(0, 1)
            if answer == 1:
                if i.isupper():
                    word_result.append(i.lower())
                elif i.islower():
                    word_result.append(i.upper())
                else:
                    word_result.append(i)
            else:
                word_result.append(i)

        word_options = [
            word_answer,
            word_answer.upper(),
            "".join(word_result),
            word_answer.title()
        ]

        return random.choice(word_options)

    def _generator_punctuation(self, length: int) -> str:
        if not (self._is_valid(length)):
            return ""

        result = []
        for _ in range(length):
            result.append(random.choice(punctuation))

        if not (len(str(result)) <= MAX_LENGTH_PASS):
            logger.info("The final output length is greater than the maximum value")
            return ""
        return "".join(result)

    def _generator_punctuation_1(self) -> str:
        return random.choice(punctuation)

    def generate_human(self, length_word: int = 5, length_digits: int = 5, length_punctuation: int = 5, option: int = None) -> str:
        if self.identical_value:
            length_word = length_digits = length_punctuation = self.length

        for length in (length_word, length_digits, length_punctuation):
            if not (self._is_valid(length)):
                logger.info("Incorrect length")
                return ""

        choice_random = [
            f"{self._generator_word(length_word)}{self._generator_punctuation_1()}{self._generator_digits(length_digits)}",
            f"{self._generator_word(length_word)}{self._generator_digits(length_digits)}{self._generator_punctuation_1()}",
            f"{self._generator_digits(length_digits)}{self._generator_punctuation_1()}{self._generator_word(length_word)}",
            f"{self._generator_digits(length_digits)}{self._generator_word(length_word)}{self._generator_punctuation_1()}",
            f"{self._generator_word(length_word)}{self._generator_digits(length_digits)}",
            f"{self._generator_digits(length_digits)}{self._generator_word(length_word)}",
            f"{self._generator_punctuation_1()}{self._generator_word(length_word)}{self._generator_digits(length_digits)}",
            f"{self._generator_punctuation_1()}{self._generator_digits(length_digits)}{self._generator_word(length_word)}",
            f"{self._generator_word(length_word)}{self._generator_punctuation_1()}{self._generator_digits(length_digits)}{self._generator_punctuation_1()}",
            f"{self._generator_digits(length_digits)}{self._generator_punctuation_1()}{self._generator_word(length_word)}{self._generator_punctuation_1()}",
            f"{self._generator_punctuation_1()}{self._generator_word(length_word)}{self._generator_punctuation_1()}{self._generator_digits(length_digits)}",
            f"{self._generator_punctuation_1()}{self._generator_digits(length_digits)}{self._generator_punctuation_1()}{self._generator_word(length_word)}",
            f"{self._generator_word(length_word)}{self._generator_punctuation_1()}{self._generator_word(length_word)}",
            f"{self._generator_punctuation_1()}{self._generator_word(length_word)}{self._generator_punctuation_1()}{self._generator_word(length_word)}",
            f"{self._generator_digits(length_digits)}{self._generator_punctuation_1()}{self._generator_digits(length_digits)}",
            f"{self._generator_punctuation_1()}{self._generator_digits(length_digits)}{self._generator_punctuation_1()}",
            f"{self._generator_word(length_word)}{self._generator_punctuation_1()}{self._generator_digits(length_digits)}{self._generator_punctuation_1()}{self._generator_word(length_word)}",
            f"{self._generator_digits(length_digits)}{self._generator_punctuation_1()}{self._generator_word(length_word)}{self._generator_punctuation_1()}{self._generator_digits(length_digits)}",
            f"{self._generator_word(length_word)}{self._generator_punctuation(length_punctuation)}{self._generator_digits(length_digits)}",
            f"{self._generator_digits(length_digits)}{self._generator_punctuation(length_punctuation)}{self._generator_word(length_word)}",
            f"{self._generator_punctuation(length_punctuation)}{self._generator_word(length_word)}{self._generator_digits(length_digits)}",
            f"{self._generator_word(length_word)}{self._generator_digits(length_digits)}{self._generator_punctuation(length_punctuation)}",
            f"{self._generator_digits(length_digits)}{self._generator_word(length_word)}{self._generator_punctuation(length_punctuation)}",
            f"{self._generator_punctuation(length_punctuation)}",
            f"{self._generator_word(length_word)}{self._generator_punctuation_1()}{self._generator_digits(length_digits)}{self._generator_punctuation_1()}{self._generator_punctuation_1()}",
        ]

        if option is None:
            return random.choice(choice_random)
        else:
            if not (self._is_valid(option)):
                return ""
            if option > len(choice_random):
                return ""
            else:
                return choice_random[option]

    def __str__(self) -> str:
        result = []
        j = -1
        for _ in range(25):
            j += 1
            result.append(f"Variant {j + 1} - {self.generate_human(option=j)}")
        logger.debug("__str__ HumanGenerator is called")
        return "\n".join(result)