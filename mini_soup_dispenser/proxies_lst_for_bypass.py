from data.proxies_raw_lst import PROXIES_RAW_LIST
from typing import List
import requests
from requests.exceptions import RequestException
import time
import random
import os

def proxies_lst_for_bypass(proxies_lst: List[str] = PROXIES_RAW_LIST,
                           force_update: bool = False) -> None:
    if not force_update and os.path.exists("proxies.txt") and os.path.getsize("proxies.txt") > 0:
        return

    unique_urls = list(set(proxies_lst))

    working_proxies = set()

    with requests.Session() as session:
        for url in unique_urls:
            try:
                response = session.get(url, timeout=15)
                if response.status_code != 200:
                    continue

                lines = response.text.splitlines()
                for line in lines:
                    clean = line.replace("https://", "").replace("http://", "").strip()
                    if not clean:
                        continue

                    if ":" not in clean or "." not in clean:
                        continue

                    proxy_dict = {
                        "http": f"http://{clean}",
                        "https": f"https://{clean}"
                    }
                    try:
                        test_resp = requests.get(
                            "http://httpbin.org/ip",
                            timeout=random.randint(2, 5),
                            proxies=proxy_dict
                        )
                        if test_resp.status_code == 200:
                            working_proxies.add(clean)
                    except RequestException:
                        continue

                time.sleep(0.5)

            except RequestException as e:
                continue

    with open("proxies.txt", "w", encoding="utf-8") as f:
        for proxy in working_proxies:
            f.write(proxy + "\n")



if __name__ == "__main__":
    proxies_lst_for_bypass(force_update=True)