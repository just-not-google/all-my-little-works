from proxy_prompt.additional_functions.language_definition import is_need_trans_to_en
import pytest


@pytest.mark.parametrize("text, answer", [
    ("hello", False),
    ("111", False),
    ("@#$%", False),
    ("привет", True),
    ("привет, how are you?", True)
])
def test_is_need_trans_to_en(text: str, answer: bool):
    assert is_need_trans_to_en(text) == answer