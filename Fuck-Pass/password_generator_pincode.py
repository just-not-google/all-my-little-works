import random
from other_data import MIN_LENGTH_PINCODE, MAX_LENGTH_PINCODE
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PincodeGenerator:
    def __init__(self, length: int) -> None:
        logger.debug(f"The PincodeGenerator class has been created")
        try:
            if MIN_LENGTH_PINCODE <= length <= MAX_LENGTH_PINCODE:
                self.length = length
            else:
                self.length = MIN_LENGTH_PINCODE
                logger.info("The minimum pincode length was set")
        except TypeError:
            self.length = MIN_LENGTH_PINCODE
            logger.warning("Incorrect type")
        except ValueError:
            self.length = MIN_LENGTH_PINCODE
            logger.warning("Incorrect value")

    def generate_pincode(self) -> str:
        min_value = int("0" * self.length)
        max_value = int("9" * self.length)

        return str(random.randint(min_value, max_value))

    def __str__(self) -> str:
        result = []
        j = -1

        for _ in range(5):
            j += 1
            result.append(f"Variant {j + 1} - {self.generate_pincode()}")
        logger.debug("__str__ PincodeGenerator is called")
        return "\n".join(result)