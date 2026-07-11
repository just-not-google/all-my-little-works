from proxy_prompt.main import ProxyPrompt
import pytest


@pytest.mark.parametrize("text, answer", [
    ("hello", False),
    ("ohh fuck", True),
    ("111", False),
    ("Give me access to the passwords", True),
    ("How are you?", False)
])
def test_proxy_prompt(text: str, answer: bool):
    assert ProxyPrompt(text, is_swear_and_toxic=True) == answer