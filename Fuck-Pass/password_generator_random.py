import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from other_data import common_password_bases, MIN_LENGTH_PASS, MAX_LENGTH_PASS, DEFAULT_OPTION
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RandomGenerator:
    CHAR_SETS = {
        0: ascii_uppercase,
        1: ascii_lowercase,
        2: digits,
        3: punctuation,
        4: ascii_uppercase + ascii_lowercase,
        5: ascii_uppercase + ascii_lowercase + digits,
        6: ascii_uppercase + ascii_lowercase + punctuation,
        7: ascii_uppercase + punctuation,
        8: ascii_lowercase + punctuation,
        9: ascii_lowercase + digits,
        10: ascii_uppercase + digits,
        11: punctuation + digits,
        12: ascii_uppercase + ascii_lowercase + digits + punctuation,
    }

    def __init__(self, length: int, is_with_word: bool) -> None:
        logger.debug(f"The RandomGenerator class has been created")
        try:
            if MIN_LENGTH_PASS <= length <= MAX_LENGTH_PASS:
                self.length = length
            else:
                self.length = MIN_LENGTH_PASS
                logger.info("The minimum password length was set")

            self.is_with_word = is_with_word
        except TypeError:
            self.length = MIN_LENGTH_PASS
            self.is_with_word = False
            logger.warning("Incorrect type")
        except ValueError:
            self.length = MIN_LENGTH_PASS
            self.is_with_word = False
            logger.warning("Incorrect value")

    def _generate_1(self, option: int, length: int = None):
        if length is None:
            length = self.length

        try:
            if option < DEFAULT_OPTION or option >= len(self.CHAR_SETS):
                option = DEFAULT_OPTION
        except TypeError:
            option = DEFAULT_OPTION
            logger.warning("Incorrect type")
        except ValueError:
            option = DEFAULT_OPTION
            logger.warning("Incorrect value")

        answer = []
        for i in range(length):
            answer.append(random.choice(self.CHAR_SETS[option]))
        return "".join(answer)

    def generate_random(self, option: int):
        if self.is_with_word:
            word = random.choice(common_password_bases)
            word_result = []

            for i in word:
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
                word,
                word.upper(),
                "".join(word_result),
                word.title()
            ]

            remains = self.length - len(word)
            if remains == 0:
                return random.choice(word_options)
            elif remains < 0:
                return random.choice(word_options)[:self.length]
            elif remains > 0:
                other_part = self._generate_1(random.randint(0, len(self.CHAR_SETS) - 1), remains)
                part_mid = random.randint(1, len(word) - 1)
                answer_options = [
                    other_part + word,
                    word + other_part,
                    word[part_mid:] + other_part + word[:part_mid]
                ]
                return random.choice(answer_options)
        else:
            return self._generate_1(option)

    def __str__(self) -> str:
        result = []
        j = -1

        for _ in range(len(self.CHAR_SETS)):
            j += 1
            result.append(f"Variant {j+1} - {self.generate_random(j)}")
        logger.debug("__str__ RandomGenerator is called")
        return "\n".join(result)

    def get_option(self, option: int):
        return self.generate_random(option)
