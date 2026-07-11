from proxy_prompt.additional_functions.text_translation import (text_translator,
                                                                text_translation_with_lang_def)
from typing import Optional
from badwords import ProfanityFilter
from glin_profanity import Filter
from detoxify import Detoxify
from proxy_prompt.data.prohibited_promptings import forbidden_prompts
from proxy_prompt.data.constants import GOOGLE, ENG_TARGET, TOXICITY_VALUE
from social_tools import ToxicityDetection
from nukon_pi_detect import scan as scan_nukon
from prompt_injection_detector import Scanner
from injectguard import scan as scan_inject


class ProxyPrompt:
    def __init__(self,
                 request: str,
                 option_trans: str = GOOGLE,
                 api_key: Optional[str] = None,
                 is_lang_def: bool = True,
                 is_swear_and_toxic: bool = False) -> None:
        self.request = request
        self.option_trans = option_trans
        self.api_key = api_key
        self.is_lang_def = is_lang_def
        self._trans_text = None
        self._is_danger = False
        self.is_swear_and_toxic = is_swear_and_toxic

    def trans_final(self) -> None:
        ANSWER_TRANS = {
            "request": self.request,
            "option_trans": self.option_trans,
            "api_key": self.api_key,
        }

        if self.is_lang_def:
            self._trans_text = text_translation_with_lang_def(**ANSWER_TRANS)
        else:
            self._trans_text = text_translator(**ANSWER_TRANS)

    def _check_1(self) -> None:
        for answer in forbidden_prompts:
            if answer in self._trans_text:
                self._is_danger = True

    def _check_2(self) -> None:
        p = ProfanityFilter()
        p.init(languages=[ENG_TARGET])
        check_2 = p.filter_text(self._trans_text)

        if check_2:
            self._is_danger = True

    def _check_3(self) -> None:
        filter = Filter({"languages": ["english"]})
        check_3 = filter.is_profane(self._trans_text)

        if check_3:
            self._is_danger = True

    def _check_4(self) -> None:
        result_1 = Detoxify("original").predict(self._trans_text)

        if result_1["toxicity"] > TOXICITY_VALUE:
            self._is_danger = True

    def _check_5(self) -> None:
        tox_detector = ToxicityDetection(tool="transformer", model="unitary/toxic-bert")
        result_2 = tox_detector.analyze(self._trans_text)

        if result_2[0]["score"] > TOXICITY_VALUE:
            self._is_danger = True

    def _check_6(self) -> None:
        result = scan_nukon(self._trans_text)

        if result.decision == "MALICIOUS":
            self._is_danger = True

    def _check_7(self) -> None:
        result = Scanner().scan(self._trans_text)
        if result.decision == "high_risk":
            self._is_danger = True

    def _check_8(self) -> None:
        result = scan_inject(self._trans_text)

        if result.is_injection:
            self._is_danger = True

    def main_check(self) -> bool:
        self.trans_final()

        check_lst = [
            self._check_1,
            self._check_7,
            self._check_8,
        ]

        if self.is_swear_and_toxic:
            check_lst.extend([self._check_2, self._check_3,
                              self._check_4, self._check_5,
                              self._check_6])

        for check in check_lst:
            try:
                check()
            except Exception:
                continue
            if self._is_danger:
                return True

        return False
