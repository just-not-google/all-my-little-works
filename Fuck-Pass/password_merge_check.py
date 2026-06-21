from other_data import NAMES_FILES
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MergeCheck:
    def __init__(self, password: str) -> None:
        logger.debug(f"The MergeCheck class has been created")
        try:
            if len(password) == 0:
                self.password = None
            else:
                self.password = password
        except TypeError:
            self.password = None
            logger.warning("Incorrect type")
        except ValueError:
            self.password = None
            logger.warning("Incorrect value")

    def local_check(self) -> bool:
        if self.password is None:
            logger.info("No password was found")
            return False

        for name_file in NAMES_FILES:
            try:
                with open(name_file, "r", encoding="utf-8") as file:
                    for line in file:
                        if self.password == line:
                            return True
            except FileNotFoundError:
                logger.warning("The file was not found")
                continue
            except Exception:
                logger.warning("An error has occurred")
                continue

        return False

    def __str__(self) -> str:
        logger.debug("__str__ MergeCheck is called")
        return (f"Has your password been leaked to the network?\n"
                f"Local verification: {self.local_check()}\n")
