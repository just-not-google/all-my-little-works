from string import ascii_uppercase, ascii_lowercase, digits, punctuation
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SecurityCheck:
    def __init__(self, password: str) -> None:
        logger.debug(f"The SecurityCheck class has been created")
        self.password = password
        self.security = 0
        self.length = False
        self.has_lower = False
        self.has_upper = False
        self.has_digit = False
        self.has_special = False
        self.not_popular = False
        self.not_same = False

    def checker(self):
        if len(self.password) >= 8:
            self.length = True

        with open("files/10_million_password_list_top_1000000.txt", "r") as file:
            result = []

            for i in file:
                result.append(i.strip())

            if not (self.password in result):
                self.not_popular = True

        if len(set(self.password)) != 1:
            self.not_same = True

        for i in self.password:
            if i in ascii_uppercase:
                self.has_upper = True
            if i in ascii_lowercase:
                self.has_lower = True
            if i in digits:
                self.has_digit = True
            if i in punctuation:
                self.has_special = True

    def calculator_answer(self) -> int:
        self.security = 0
        self.checker()

        if self.length:
            self.security += 1

        if self.not_popular:
            self.security += 1

        if self.not_same:
            self.security += 1

        if self.has_upper:
            self.security += 1

        if self.has_lower:
            self.security += 1

        if self.has_digit:
            self.security += 1

        if self.has_special:
            self.security += 1

        return self.security

    def __str__(self) -> str:
        result = [f"Password Strength: {self.calculator_answer()}/7\n"]
        if self.length:
            result.append("(+) The length is more than 8 characters\n")
        else:
            result.append("(-) Length less than 8 characters\n")

        if self.not_popular:
            result.append("(+) There are no popular passwords in the database\n")
        else:
            result.append("(-) It is in the database of popular passwords\n")

        if self.not_same:
            result.append("(+) It doesn't consist of identical characters\n")
        else:
            result.append("(-) It consists of identical characters\n")

        if self.has_upper:
            result.append("(+) There are uppercase letters\n")
        else:
            result.append("(-) There is no uppercase letter\n")

        if self.has_lower:
            result.append("(+) There are lowercase letters\n")
        else:
            result.append("(-) There is no lowercase letter\n")

        if self.has_digit:
            result.append("(+) There are numbers\n")
        else:
            result.append("(-) There is no number\n")

        if self.has_special:
            result.append("(+) There are special characters (punctuation)\n")
        else:
            result.append("(-) No special characters (punctuation)")

        logger.debug("__str__ SecurityCheck is called")
        return "".join(result)