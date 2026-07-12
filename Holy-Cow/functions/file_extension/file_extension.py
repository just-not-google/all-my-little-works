from Holy_Cow.data_other.other import DOT
from Holy_Cow.functions.file_extension.data_file_extension.file_formats import file_formats

def is_valid_file_extension(files: list[str], extensions: list[str] = file_formats) -> list[bool]:
    if not files:
        return []

    answer_bool = []
    try:
        for file in files:
            if not DOT in file:
                answer_bool.append(False)
                continue
            file_lst = file.partition(DOT)
            file_part = file_lst[2]
            if not file_part in extensions:
                answer_bool.append(False)
                continue
            answer_bool.append(True)

        return answer_bool

    except TypeError:
        return [False] * len(files)
    except AttributeError:
        return [False] * len(files)
    except ValueError:
        return [False] * len(files)
    except Exception:
        return [False] * len(files)
