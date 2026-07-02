from .data.headers import HEADERS_LIST
import requests
from requests import Response
from typing import List, Dict, Optional
import random


def requests_with_proxy(u: str, head: Optional[List[Dict]] = None,
                        min_n: int = 2, max_n: int = 5,
                        strm: bool = False) -> Optional[Response]:
    if head is None:
        head = HEADERS_LIST

    proxies_list = []
    try:
        with open("proxies.txt", "r", encoding="utf-8") as f:
            proxies_list = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return None

    if not proxies_list:
        return None

    proxy_line = random.choice(proxies_list)

    proxies_dict = {
        "http": f"http://{proxy_line}",
        "https": f"https://{proxy_line}"
    }

    try:
        response = requests.get(
            url=u,
            headers=random.choice(head),
            timeout=random.randint(min_n, max_n),
            stream=strm,
            proxies=proxies_dict
        )
        return response
    except requests.exceptions.RequestException:
        return None