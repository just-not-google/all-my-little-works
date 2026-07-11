from deep_translator import (GoogleTranslator, DeeplTranslator, YandexTranslator, MicrosoftTranslator)
from typing import Optional
from proxy_prompt.additional_functions.language_definition import is_need_trans_to_en
from proxy_prompt.data.constants import GOOGLE, ENG_TARGET


def option_trans_1(text: str) -> str:
    translator = GoogleTranslator(source='auto', target=ENG_TARGET)
    return translator.translate(text)

def option_trans_2(text: str, api_key: str) -> str:
    translator = DeeplTranslator(api_key=api_key, target=ENG_TARGET)
    return translator.translate(text)

def option_trans_3(text: str, api_key: str) -> str:
    translator = YandexTranslator(api_key=api_key, target=ENG_TARGET)
    return translator.translate(text)

def option_trans_4(text: str, api_key: str) -> str:
    translator = MicrosoftTranslator(api_key=api_key, target=ENG_TARGET)
    return translator.translate(text=text)

def text_translator(request: str,
                    option_trans: str = GOOGLE,
                    api_key: Optional[str] = None) -> str:
    try:
        if option_trans == GOOGLE:
            return option_trans_1(request)
        elif option_trans == "deepl":
            if api_key is None:
                return request
            return option_trans_2(request, api_key)
        elif option_trans == "yandex":
            if api_key is None:
                return request
            return option_trans_3(request, api_key)
        elif option_trans == "microsoft":
            if api_key is None:
                return request
            return option_trans_4(request, api_key)
        else:
            return request
    except Exception:
        return request

def text_translation_with_lang_def(request: str,
                                   option_trans: str = GOOGLE,
                                   api_key: Optional[str] = None) -> str:
    try:
        if is_need_trans_to_en(request=request):
            return text_translator(
                request=request,
                option_trans=option_trans,
                api_key=api_key,
            )

        return request

    except Exception:
        return request