import pycld2
from fast_langdetect import detect
from fast_langdetect import FastLangdetectError
from lingua import LanguageDetectorBuilder
from typing import Optional, List
from proxy_prompt.data.language_codes import language_codes
from proxy_prompt.data.constants import ENG_TARGET


def _is_all_special(text: str) -> bool:
    if not text:
        return False

    return all(not ch.isalnum() and not ch.isspace() for ch in text)

def _option_trans_1(text: str) -> Optional[List]:
    try:
        answer = pycld2.detect(text)[2][0]
        language = answer[1]
        scr = answer[2]
        score = True

        if scr < 70:
            score = False

        if answer == "un":
            return None

        return [language, score]

    except pycld2.error:
        return None

def _option_trans_2(text: str) -> Optional[List]:
    try:
        answer = detect(text, model="lite", k=1)[0]
        language = answer["lang"]
        scr = int(round(answer["score"], 2) * 100)
        score = True

        if scr < 85:
            score = False

        return [language, score]

    except FastLangdetectError:
        return None

def _option_trans_3(text: str) -> Optional[List]:
    try:
        detector = LanguageDetectorBuilder.from_all_languages().build()
        lang = detector.compute_language_confidence_values(text)[0]
        language = language_codes[lang.language.name]
        scr = int(round(lang.value, 2) * 100)
        score = True

        if scr < 64:
            score = False

        return [language, score]

    except Exception:
        return None

def is_need_trans_to_en(request: str) -> bool:
    if request.isdigit():
        return False

    if _is_all_special(request):
        return False

    results = [
        _option_trans_1(request),
        _option_trans_2(request),
        _option_trans_3(request)
    ]

    valid = [r for r in results if r is not None]

    if not valid:
        return True

    for lang, _ in valid:
        if lang.lower() not in (ENG_TARGET, "english"):
            return True

    return False