import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import requests
from fake_useragent import UserAgent
from fp.fp import FreeProxy
import random
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from data import url_all, http, https, socks4, socks5

def check_single_proxy(proxy_url, test_url="http://www.youtube.com", timeout=5):
    try:
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }
        response = requests.get(test_url, timeout=timeout, proxies=proxies)
        if response.status_code == 200:
            return proxy_url
    except:
        pass
    return None

def proxy_sources(proxy_urls):
    y = []
    all_proxies = []
    for url in proxy_urls:
        try:
            scrolledtext_1.insert(tk.END, f"Получение прокси с {url}...\n")
            scrolledtext_1.see(tk.END)
            root.update()
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            text = response.text
            lines = text.split('\n')
            for line in lines:
                cleaned_line = line.strip()
                if cleaned_line:
                    all_proxies.append(cleaned_line)
            scrolledtext_1.insert(tk.END, f"Получено {len(lines)} прокси с {url}\n")
            scrolledtext_1.see(tk.END)
            root.update()
        except Exception as e:
            scrolledtext_1.insert(tk.END, f"Ошибка при получении с {url}: {str(e)}\n")
            scrolledtext_1.see(tk.END)
            root.update()
            continue

    scrolledtext_1.insert(tk.END, f"Проверка {len(all_proxies)} прокси из источников...\n")
    scrolledtext_1.see(tk.END)
    root.update()

    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_proxy = {
            executor.submit(check_single_proxy, proxy): proxy
            for proxy in all_proxies
        }

        for future in as_completed(future_to_proxy):
            result = future.result()
            if result:
                y.append(result)
                scrolledtext_1.insert(tk.END, f"Рабочий прокси: {result}\n")
                scrolledtext_1.see(tk.END)
                root.update()

    return y

def http_proxy():
    y = []
    for i in proxy_sources(http):
        y.append(f"http://{i}")
    return y

def https_proxy():
    y = []
    for i in proxy_sources(https):
        y.append(f"https://{i}")
    return y

def socks5_proxy():
    y = []
    for i in proxy_sources(socks5):
        y.append(f"socks5://{i}")
    return y

def socks4_proxy():
    y = []
    for i in proxy_sources(socks4):
        y.append(f"socks4://{i}")
    return y

def main_proxy_check():
    all_proxies = []
    scrolledtext_1.insert(tk.END, "Запуск проверки прокси из источников...\n")
    scrolledtext_1.see(tk.END)
    root.update()

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(http_proxy),
            executor.submit(https_proxy),
            executor.submit(socks5_proxy),
            executor.submit(socks4_proxy),
            executor.submit(lambda: proxy_sources(url_all))
        ]

        for future in as_completed(futures):
            try:
                result = future.result()
                all_proxies.extend(result)
                scrolledtext_1.insert(tk.END, f"Получено {len(result)} рабочих прокси из потока\n")
                scrolledtext_1.see(tk.END)
                root.update()
            except Exception as e:
                scrolledtext_1.insert(tk.END, f"Ошибка в потоке: {str(e)}\n")
                scrolledtext_1.see(tk.END)
                root.update()
                continue

    return set(all_proxies)

def common_req(url, minimal, maximum):
    try:
        random_timeout = random.randint(minimal, maximum)
        random_headers = {"User-Agent": UserAgent().chrome}
        scrolledtext_1.insert(tk.END, f"Проверка доступности {url} с таймаутом {random_timeout}с...\n")
        scrolledtext_1.see(tk.END)
        root.update()
        response = requests.get(f"https://{url}", timeout=random_timeout, headers=random_headers)
        if response.status_code == 200:
            scrolledtext_1.insert(tk.END, f"{url} доступен\n")
            scrolledtext_1.see(tk.END)
            root.update()
            return True
        else:
            scrolledtext_1.insert(tk.END, f"{url} недоступен (код: {response.status_code})\n")
            scrolledtext_1.see(tk.END)
            root.update()
            return False
    except Exception as e:
        scrolledtext_1.insert(tk.END, f"Ошибка при проверке {url}: {str(e)}\n")
        scrolledtext_1.see(tk.END)
        root.update()
        return False

def check_free_proxy(proxy_dict, timeout_val, headers):
    try:
        scrolledtext_1.insert(tk.END, f"Проверка FreeProxy {proxy_dict['http']}...\n")
        scrolledtext_1.see(tk.END)
        root.update()
        response = requests.get("https://www.youtube.com", timeout=timeout_val,
                               headers=headers, proxies=proxy_dict)
        if response.status_code == 200:
            scrolledtext_1.insert(tk.END, f"Рабочий FreeProxy: {proxy_dict['http']}\n")
            scrolledtext_1.see(tk.END)
            root.update()
            return proxy_dict
    except Exception as e:
        scrolledtext_1.insert(tk.END, f"Ошибка FreeProxy {proxy_dict['http']}: {str(e)}\n")
        scrolledtext_1.see(tk.END)
        root.update()
        pass
    return None

def uncommon_req(timeout_on_proxy, minimal, maximum):
    try:
        scrolledtext_1.insert(tk.END, "Получение прокси через FreeProxy...\n")
        scrolledtext_1.see(tk.END)
        root.update()
        proxy_list = FreeProxy(timeout=timeout_on_proxy).get_proxy_list()
        proxy_dicts = []

        for p in proxy_list:
            proxies = {
                'http': p,
                'https': p
            }
            proxy_dicts.append(proxies)

        random_timeout = random.randint(minimal, maximum)
        random_headers = {"User-Agent": UserAgent().chrome}

        working_proxies = []

        scrolledtext_1.insert(tk.END, f"Проверка {len(proxy_dicts)} FreeProxy с таймаутом {random_timeout}с...\n")
        scrolledtext_1.see(tk.END)
        root.update()

        with ThreadPoolExecutor(max_workers=15) as executor:
            future_to_proxy = {
                executor.submit(check_free_proxy, proxy, random_timeout, random_headers): proxy
                for proxy in proxy_dicts
            }

            for future in as_completed(future_to_proxy):
                result = future.result()
                if result:
                    working_proxies.append(result)

        return working_proxies
    except Exception as e:
        scrolledtext_1.insert(tk.END, f"Ошибка в FreeProxy: {str(e)}\n")
        scrolledtext_1.see(tk.END)
        root.update()
        return []

def free_proxy_check(url, timeout_on_proxy, minimal, maximum):
    if not common_req(url, minimal, maximum):
        return uncommon_req(timeout_on_proxy, minimal, maximum)
    scrolledtext_1.insert(tk.END, f"{url} доступен напрямую, пропускаем FreeProxy\n")
    scrolledtext_1.see(tk.END)
    root.update()
    return []

def start_scan():
    def scan_thread():
        try:
            min_timeout = int(entry_1.get())
            max_timeout = int(entry_2.get())
            check_url = entry_3.get()

            if min_timeout <= 0 or max_timeout <= 0:
                scrolledtext_1.delete(1.0, tk.END)
                scrolledtext_1.insert(tk.END, "Ошибка: timeout должен быть положительным числом\n")
                scrolledtext_1.see(tk.END)
                root.update()
                return

            if min_timeout > max_timeout:
                scrolledtext_1.delete(1.0, tk.END)
                scrolledtext_1.insert(tk.END, "Ошибка: минимальный timeout не может быть больше максимального\n")
                scrolledtext_1.see(tk.END)
                root.update()
                return

            scrolledtext_1.delete(1.0, tk.END)
            scrolledtext_1.insert(tk.END, "Начинается многопоточное сканирование прокси...\nПожалуйста, подождите...\n")
            scrolledtext_1.see(tk.END)
            root.update()

            working_proxies = main_proxy_check()
            scrolledtext_1.insert(tk.END, f"\n=== Многопоточная проверка прокси из источников ===\n")
            scrolledtext_1.insert(tk.END, f"Найдено рабочих прокси: {len(working_proxies)}\n")
            scrolledtext_1.see(tk.END)
            root.update()

            for proxy in working_proxies:
                scrolledtext_1.insert(tk.END, f"{proxy}\n")
                scrolledtext_1.see(tk.END)
                root.update()

            scrolledtext_1.insert(tk.END, "\n=== Многопоточная проверка прокси через FreeProxy ===\n")
            scrolledtext_1.see(tk.END)
            root.update()

            free_proxy_result = free_proxy_check(check_url, 1, min_timeout, max_timeout)
            scrolledtext_1.insert(tk.END, f"Найдено рабочих прокси через FreeProxy: {len(free_proxy_result)}\n")
            scrolledtext_1.see(tk.END)
            root.update()

            for proxy in free_proxy_result:
                scrolledtext_1.insert(tk.END, f"{proxy}\n")
                scrolledtext_1.see(tk.END)
                root.update()

            scrolledtext_1.insert(tk.END, f"\n=== ИТОГО ===\nВсего рабочих прокси: {len(working_proxies) + len(free_proxy_result)}\n")
            scrolledtext_1.see(tk.END)
            root.update()

        except ValueError:
            scrolledtext_1.delete(1.0, tk.END)
            scrolledtext_1.insert(tk.END, "Ошибка: введите корректные числовые значения для timeout\n")
            scrolledtext_1.see(tk.END)
            root.update()
        except Exception as e:
            scrolledtext_1.delete(1.0, tk.END)
            scrolledtext_1.insert(tk.END, f"Произошла ошибка: {str(e)}\n")
            scrolledtext_1.see(tk.END)
            root.update()

    threading.Thread(target=scan_thread, daemon=True).start()

root = tk.Tk()
root.geometry("630x700")
root.resizable(False, False)
root.title("Scan-Proxy-Ip")

heading = tk.Label(root, text="Scan-Proxy-Ip", font=("Times New Roman", 25, "bold"))
heading.pack()

label_1 = tk.Label(root, text="Минимальный Timeout", font=("Times New Roman", 20))
label_1.place(x=20, y=50)

label_2 = tk.Label(root, text="Максимальный Timeout", font=("Times New Roman", 20))
label_2.place(x=20, y=100)

label_3 = tk.Label(root, text="Сайт для проверки", font=("Times New Roman", 20))
label_3.place(x=20, y=150)

label_4 = tk.Label(root, text="(По умолчанию: www.youtube.com)", font=("Times New Roman", 12), foreground="red")
label_4.place(x=20, y=180)

entry_1 = tk.Entry(root, font=("Times New Roman", 20))
entry_1.place(x=320, y=50)
entry_1.insert(0, "2")

entry_2 = tk.Entry(root, font=("Times New Roman", 20))
entry_2.place(x=320, y=100)
entry_2.insert(0, "5")

entry_3 = tk.Entry(root, font=("Times New Roman", 20))
entry_3.place(x=320, y=150)
entry_3.insert(0, "www.youtube.com")

button_1 = tk.Button(root, text=">> Начать проверку Proxy <<",
                     font=("Times New Roman", 16, "bold"), foreground="white",
                     background="red", width=40, command=start_scan)
button_1.place(x=20, y=220)

scrolledtext_1 = ScrolledText(root, font=("Times New Roman", 12, "bold"),
                             width=52, height=16)
scrolledtext_1.place(x=20, y=290)

status_label = tk.Label(root, text="Готов к работе", font=("Times New Roman", 12), foreground="green")
status_label.place(x=20, y=650)

root.mainloop()