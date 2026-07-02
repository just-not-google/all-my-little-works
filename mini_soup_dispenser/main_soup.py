from .data.headers import HEADERS_LIST
import requests
from typing import Optional, List, Dict
from bs4 import BeautifulSoup
import random
from .is_file_not_empty import is_file_non_empty
from .proxies_lst_for_bypass import proxies_lst_for_bypass
from .data.proxies_raw_lst import PROXIES_RAW_LIST
from .requests_with_proxy import requests_with_proxy
import time

def make_soup(url_goal: str, headers_lst: List[Dict] = HEADERS_LIST,
                   min_timeout_value: int = 2, max_timeout_value: int = 5,
                   stream_value: bool = False, is_proxy: bool = False,
                   my_lst_proxies_raw: List = PROXIES_RAW_LIST,
                   retries: int = 3) -> Optional[BeautifulSoup]:
    if is_proxy:
        if not is_file_non_empty("proxies.txt"):
            proxies_lst_for_bypass(proxies_lst=my_lst_proxies_raw, force_update=True)
        if not is_file_non_empty("proxies.txt"):
            is_proxy = False

    for attempt in range(1, retries + 1):
        try:
            chosen_headers = random.choice(headers_lst)
            timeout = random.randint(min_timeout_value, max_timeout_value)

            if is_proxy:
                response = requests_with_proxy(
                    u=url_goal,
                    head=chosen_headers,
                    min_n=min_timeout_value,
                    max_n=max_timeout_value,
                    strm=stream_value
                )
                if response is None:
                    is_proxy = False
                    continue
            else:
                response = requests.get(
                    url=url_goal,
                    headers=chosen_headers,
                    timeout=timeout,
                    stream=stream_value
                )

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                return soup
            else:
                time.sleep(1)

        except requests.exceptions.RequestException as e:
            time.sleep(1)

    return None