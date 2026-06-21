import requests
from bs4 import BeautifulSoup
from Game_Aggregator_Torrent.Data.parsing_data import timeout
from Game_Aggregator_Torrent.Working_On_Links.final_version_url_2 import final_version_url_2

def parsing_xatab_org(name_game):
    try:
        url = "https://xatab.org/"
        final_url = final_version_url_2("https://xatab.org/search.php?comun=", name_game)
        response = requests.get(url=final_url, timeout=timeout)
        if response.status_code == 200:
            html = response.text
            print(f"Страничка была прогружена - {response.status_code}")
            soup = BeautifulSoup(html, "html.parser")
            ss_1 = soup.find("div", class_="wide-list__item")
            if ss_1:
                links = soup.find_all("a")
                y = []
                for link in links:
                    href = link.get("href")
                    y.append(href)
                y_1 = max(list(set(y)), key=len)
                url_2 = url + y_1
                print(f"Ссылка - {url_2}")
                response_1 = requests.get(url_2, timeout=timeout)
                if response_1.status_code == 200:
                    html_1 = response_1.text
                    soup_1 = BeautifulSoup(html_1, "html.parser")
                    header_1 = soup_1.find("h1")
                    if header_1:
                        header = header_1.text
                        rating = soup_1.find("div", class_="rating").find("span").text
                        print(header[34:])
                        print(f"Рейтинг: {rating}/10")
                    else:
                        print(f"Странички игры не найдено - {response.status_code}")
            else:
                print("Такой игры не найдено на данном сайте")
        else:
            print("Что-то не работает")
    except TimeoutError:
        print("Ошибка тайм-аута")
    except requests.RequestException:
        print(f"Ошибка при соединении страницы")
    except Exception as e:
        print(f"Неизвестная ошибка - {e}")


if __name__ == "__main__":
    x = input(">> ")
    parsing_xatab_org(x)