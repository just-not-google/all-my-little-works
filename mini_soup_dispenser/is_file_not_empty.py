import os

def is_file_non_empty(filepath: str) -> bool:
    try:
        if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
            return True
        return False
    except OSError:
        return False