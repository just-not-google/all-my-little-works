import datetime
import inspect
import os
import json
from typing import Optional, Callable, Any
from .data.languages import LANGUAGES


class AutoDocstr:
    def __init__(
        self,
        language: str = 'en',
        output_file: str = 'README.md',
        visualization: bool = False,
        write_document: bool = True,
        json_output: bool = False,
        ignore: bool = False,
    ):
        self.language = language if language in LANGUAGES else 'en'
        self.output_file = output_file
        self.visualization = visualization
        self.write_document = write_document
        self.json_output = json_output
        self.ignore = ignore

        self._counter = 0
        self._doc_funcs = set()

        self._lang = LANGUAGES[self.language]

    def __call__(self, func: Callable) -> Callable:
        if self.ignore:
            return func

        func_name = func.__name__
        if func_name in self._doc_funcs:
            return func

        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            info = self._extract_info(func, args, kwargs, result)

            if self.write_document:
                self._write_to_file(info)

            if self.visualization:
                print(info['markdown'])

            if self.json_output:
                self._append_json(info)

            self._doc_funcs.add(func_name)

            return result

        return wrapper

    def _extract_info(self, func, args, kwargs, result) -> dict:
        self._counter += 1
        number = self._counter
        name = func.__name__
        doc = func.__doc__.strip() if func.__doc__ else self._lang[6]  # "Нет данных"
        sig = inspect.signature(func)
        input_data = str(sig).strip('()') or self._lang[6]
        args_str = ", ".join(repr(a) for a in args) if args else self._lang[6]
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) if kwargs else self._lang[6]

        return_annotation = sig.return_annotation
        if return_annotation is inspect.Signature.empty:
            return_type = "None"
        else:
            return_type = str(return_annotation).replace("typing.", "")

        result_str = f"{result} (тип: {return_type})" if result is not None else f"None (тип: {return_type})"

        md = (
            f"## {self._lang[1]}: {name}\n\n"
            f"{self._lang[0]}: {number}\n\n"
            f"{self._lang[2]}: {doc}\n\n"
            f"{self._lang[3]}: `{input_data}`\n\n"
            f"{self._lang[4]}: {args_str}\n\n"
            f"{self._lang[5]}: {kwargs_str}\n\n"
            f"{self._lang[9]}: {result_str}\n\n"
            f"---\n\n"
        )

        return {
            'number': number,
            'name': name,
            'doc': doc,
            'input_data': input_data,
            'args': args_str,
            'kwargs': kwargs_str,
            'result': result_str,
            'return_type': return_type,
            'markdown': md,
            'json': {
                'number': number,
                'name': name,
                'doc': doc,
                'signature': input_data,
                'args': args_str,
                'kwargs': kwargs_str,
                'result': result_str,
                'return_type': return_type,
            }
        }

    def _write_to_file(self, info: dict):
        file_path = self.output_file
        write_header = False
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            write_header = True

        mode = 'a' if os.path.exists(file_path) else 'w'
        with open(file_path, mode, encoding='utf-8') as f:
            if write_header:
                f.write(f"# Автодокументация функций\n\n")
                f.write(f"_Сгенерировано: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n\n")
            f.write(info['markdown'])

    def _append_json(self, info: dict):
        json_path = self.output_file.rsplit('.', 1)[0] + '.json'
        # Читаем существующий массив, если есть
        data = []
        if os.path.exists(json_path):
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except:
                data = []
        data.append(info['json'])
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

def auto_docstr_readme(
    func=None,
    language: str = 'en',
    output_file: str = 'README.md',
    visualization: bool = False,
    write_document: bool = True,
    json_output: bool = False,
    ignore: bool = False,
):
    
    def decorator(f):
        return AutoDocstr(
            language=language,
            output_file=output_file,
            visualization=visualization,
            write_document=write_document,
            json_output=json_output,
            ignore=ignore,
        )(f)

    if func is not None:
        return decorator(func)
    return decorator
