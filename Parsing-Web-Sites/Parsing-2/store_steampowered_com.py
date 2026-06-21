import requests
from Game_Aggregator_Torrent.Data.parsing_data import timeout, headers
from bs4 import BeautifulSoup
from Game_Aggregator_Torrent.Working_On_Links.final_version_url_1 import final_version_url_1

def parsing_store_steampowered_com(name_game):
    try:
        api_url = api_url = final_version_url_1(
            "https://store.steampowered.com/api/storesearch/?term=",
            name_game, "&l=english&cc=US")
        response = requests.get(url=api_url, headers=headers, timeout=timeout)
        if response.status_code == 200:
            print(f"Страничка была прогружена - {response.status_code}")
            data = response.json()
            if data["total"] > 0:
                answer = data["items"][0]["id"]
                url_str = f"https://store.steampowered.com/app/{answer}"
                print(f"Ссылка - {url_str}")
                response_1 = requests.get(url=url_str, headers=headers, timeout=timeout)
                if response_1.status_code == 200:
                    html = response_1.text
                    soup = BeautifulSoup(html, "html.parser")
                    header = soup.find("div", class_="apphub_AppName")
                    if header:
                        header_1 = header.text
                        developer = soup.find("div", class_="dev_row").text
                        dd = " ".join(developer.split()[1:])
                        publisher = soup.find("a",
                                              href="https://store.steampowered.com/publisher/panic?snr=1_5_9__2000")
                        if publisher:
                            publisher_1 = publisher.text
                        else:
                            publisher_1 = dd
                        price = soup.find("div", class_="game_purchase_price price").text
                        about = soup.find("div", class_="game_description_snippet").text
                        ss = " ".join(about.split()[:10]) + "..."
                        date = soup.find("div", class_="date").text
                        print(f"Название: {header_1}")
                        print(f"Дата выхода: {date}")
                        print(f"Создатель: {dd}")
                        print(f"Издатель: {publisher_1}")
                        print(f"Об игре: {ss}")
                        print(f"Цена: {price[7:]}")
                else:
                    print("Странички игры не найдено")
            else:
                print("Такой игры не найдено на данном сайте")
        else:
            print("Что-то не работает")
    except Exception as e:
        print(f"Неизвестная ошибка - {e}")


if __name__ == "__main__":
    x = input(">> ")
    parsing_store_steampowered_com(x)