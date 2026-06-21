import time
from tkinter.constants import DISABLED, NORMAL, END
import bs4
import requests
from bs4 import BeautifulSoup
import random
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading


def parsing_vacancy(scrolled_text=None, status_label=None, progress_bar=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    timeout = random.randint(20, 40)
    sleep_time = random.randint(1, 3)
    url = "https://career.habr.com/vacancies/programmist_python?page="
    j = 0
    hh = []

    def log_message(message):
        if scrolled_text:
            scrolled_text.config(state=NORMAL)
            scrolled_text.insert(END, f"{message}\n")
            scrolled_text.see(END)
            scrolled_text.config(state=DISABLED)
        print(message)

    def update_status(message):
        if status_label:
            status_label.config(text=message)

    try:
        while True:
            j += 1
            url_1_1 = url + str(j)
            update_status(f"Парсинг страницы {j}...")
            response = requests.get(url_1_1, timeout=timeout, headers=headers)
            if response.status_code == 200:
                log_message("Подключение успешно")
                soup = BeautifulSoup(response.text, "html.parser")
                vacancies = soup.find_all('div', class_="vacancy-card")
                if not vacancies:
                    log_message("Не найдено вакансий, конец")
                    update_status("Завершено")
                    break
                hh.append(len(vacancies))
                log_message(f"Найдено вакансий (суммируются): {sum(hh)}")
                i = 0
                urls = []
                for vacancy in vacancies:
                    heading_soup = vacancy.find(class_="vacancy-card__title-link")
                    company_soup = vacancy.find('a', class_="link-comp link-comp--appearance-dark")
                    salary_soup = vacancy.find(class_="basic-salary")
                    gg_url = "https://career.habr.com"
                    url_to = heading_soup["href"]
                    url_button = gg_url + url_to
                    urls.append(url_button)
                    for url in urls:
                        response_about = requests.get(url, timeout=timeout, headers=headers)
                        if response_about.status_code == 200:
                            soup_about = BeautifulSoup(response_about.text, "html.parser")
                            abouts = soup_about.find('div', class_="style-ugc").text
                        else:
                            log_message(f"Допуск к подробной информации не был получен: {response_about.status_code}")
                    heading = heading_soup.text.strip()
                    company = company_soup.text.strip()
                    salary = salary_soup.text.strip() if salary_soup else "Цена не указана"
                    i += 1

                    log_message("")
                    log_message(f"=== Вакансия {i} ===")
                    log_message(f"НАЗВАНИЕ: {heading}")
                    log_message(f"ССЫЛКА: {url_button}")
                    log_message(f"КОМПАНИЯ: {company}")
                    log_message(f"ЗАРПЛАТА: {salary}")
                    log_message(f"О КОМПАНИИ: \n{abouts[:221]}...")
                    log_message("")
                    time.sleep(sleep_time)
            else:
                log_message(f"Подключение прервано: {response.status_code}")
                update_status("Ошибка подключения")
                break
            time.sleep(sleep_time)
    except requests.exceptions.RequestException as e:
        log_message(f"Ошибка подключения - {e}")
        update_status("Ошибка подключения")
    except Exception as e:
        log_message(f"Иные ошибки - {e}")
        update_status("Ошибка")


def start_parsing():
    thread = threading.Thread(target=parsing_vacancy, args=(scrolled_text, status_label))
    thread.daemon = True
    thread.start()


def gui():
    global scrolled_text, status_label

    root = tk.Tk()
    root.geometry("700x700")
    root.title("Parsing Vacancies")
    root.resizable(False, False)

    heading = tk.Label(text="Parsing Vacancies", font=("Times New Roman", 30, "bold"))
    heading.pack(pady=(5, 15))

    button = tk.Button(text=">> Начать <<", font=("Times New Roman", 18, "bold"),
                       width=22, background="green", foreground="white",
                       command=start_parsing)
    button.pack(pady=(5, 10))

    status_label = tk.Label(text="Готов к работе", font=("Times New Roman", 12))
    status_label.pack(pady=(0, 10))

    scrolled_text = ScrolledText(width=52, height=18, font=("Times New Roman", 18))
    scrolled_text.pack(pady=(5, 10), padx=10)
    scrolled_text.config(state=DISABLED)

    root.mainloop()


if __name__ == "__main__":
    gui()