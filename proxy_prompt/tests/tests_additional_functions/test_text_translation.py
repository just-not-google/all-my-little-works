from proxy_prompt.additional_functions.text_translation import (text_translator,
                                                                text_translation_with_lang_def)
import pytest


@pytest.mark.parametrize("text, trans_text", [
    ("hello", "hello"),
    ("привет", "hello"),
    ("こんにちは", "hello"),
    ("hola", "hello")
])
def test_text_translator(text: str, trans_text: str):
    assert text_translator(text) == trans_text

@pytest.mark.parametrize("text, trans_text", [
    ("goodbye", "goodbye"),
    ("до свидания", "goodbye"),
    ("さようなら", "goodbye"),
    ("hasta la vista", "goodbye")
])
def test_text_translator_with_lang_def(text: str, trans_text: str):
    assert text_translation_with_lang_def(text) == trans_text