import tkinter as tk
from tkinter import ttk, scrolledtext
from bs4 import BeautifulSoup
import requests
import threading
from queue import Queue
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data_queue = Queue()
parsing_active = False


def update_text_widget():
    """Функция для обновления текстового виджета из основного потока"""
    global parsing_active

    try:
        while not data_queue.empty():
            text = data_queue.get_nowait()
            text1.config(state="normal")
            text1.insert(tk.END, text)
            text1.config(state="disabled")
            text1.see(tk.END)
    except:
        pass

    if parsing_active:
        root.after(100, update_text_widget)
    else:
        button.config(state="normal")


def get_price(lst: list) -> None:
    '''
    A function that requests an empty list and adds data
    on the share price of a particular company to it after
    parsing the site. This is done so that on the main site
    where the information in percentage change of the stock
    is taken, it is not possible to get price data
    '''
    urls1 = {
        "Nvidia": "https://finance.yahoo.com/quote/NVDA/",
        "AMD": "https://finance.yahoo.com/quote/AMD/",
        "Netflix": "https://finance.yahoo.com/quote/NFLX/",
        "Tesla": "https://finance.yahoo.com/quote/TSLA/",
        "Samsung": "https://finance.yahoo.com/quote/005930.KS/",
        "Xiaomi": "https://finance.yahoo.com/quote/1810.HK/",
        "Microsoft": "https://finance.yahoo.com/quote/MSFT/",
        "Tencent": "https://finance.yahoo.com/quote/TCEHY/",
        "Walmart": "https://finance.yahoo.com/quote/WMT/",
        "Google": "https://finance.yahoo.com/quote/GOOG/"
    }

    for key, value in urls1.items():
        try:
            response1 = requests.get(value, headers=headers, timeout=40)
            soup1 = BeautifulSoup(response1.content, 'html.parser')
            element33 = soup1.find(class_="yf-ipw1h0 base")
            if element33:
                data_queue.put(f"{key}: {element33.text} $\n")
                lst.append(element33.text)
            else:
                data_queue.put(f"{key}: Price not found\n")
                lst.append("N/A")
        except Exception as e:
            data_queue.put(f"{key}: Error - {str(e)}\n")
            lst.append("N/A")


def get_data_thread():
    '''
    The main function that collects basic information
    from the main site and outputs everything in total,
    taking into account the get_price() function.
    '''
    global parsing_active

    try:
        data_queue.put("=== Starting parsing ===\n")

        lst = []
        get_price(lst)

        urls = {
            "Nvidia": ["https://ru.tradingview.com/symbols/NASDAQ-NVDA/?timeframe=12M",lst[0] if len(lst) > 0 else "N/A"],
            "AMD": ["https://ru.tradingview.com/symbols/NASDAQ-AMD/", lst[1] if len(lst) > 1 else "N/A"],
            "Netflix": ["https://ru.tradingview.com/symbols/NASDAQ-NFLX/", lst[2] if len(lst) > 2 else "N/A"],
            "Tesla": ["https://ru.tradingview.com/symbols/NASDAQ-TSLA/", lst[3] if len(lst) > 3 else "N/A"],
            "Samsung": ["https://ru.tradingview.com/symbols/KRX-005930/", lst[4] if len(lst) > 4 else "N/A"],
            "Xiaomi": ["https://ru.tradingview.com/symbols/HKEX-1810/", lst[5] if len(lst) > 5 else "N/A"],
            "Microsoft": ["https://ru.tradingview.com/symbols/NASDAQ-MSFT/", lst[6] if len(lst) > 6 else "N/A"],
            "Tencent": ["https://ru.tradingview.com/symbols/HKEX-700/", lst[7] if len(lst) > 7 else "N/A"],
            "Walmart": ["https://ru.tradingview.com/symbols/NYSE-WMT/", lst[8] if len(lst) > 8 else "N/A"],
            "Google": ["https://ru.tradingview.com/symbols/NASDAQ-GOOG/", lst[9] if len(lst) > 9 else "N/A"]
        }

        for key, value in urls.items():
            try:
                data_queue.put(f"\n--- Parsing {key} ---\n")
                response = requests.get(value[0], headers=headers, timeout=40)
                soup = BeautifulSoup(response.content, 'html.parser')
                heading = soup.find(class_="apply-overflow-tooltip title-HDE_EEoW")

                if heading:
                    data_queue.put(f"{heading.text} - {value[1]}$\n")
                else:
                    data_queue.put(f"{key} - {value[1]} (Title not found)\n")

                all_elements = soup.find_all(class_="change-o1CQs_Mg")
                time_periods = ["1 day", "5 days", "1 month", "6 months", "Since the beginning of the year",
                                "1 year", "5 years", "For all the time"]

                for i, element in zip(time_periods, all_elements):
                    text = element.get_text(strip=True)
                    data_queue.put(f"{i}: {text}")
                    data_queue.put(f"\n\n")

            except Exception as e:
                data_queue.put(f"Error processing {key}: {str(e)}\n")

        data_queue.put("\n=== Parsing completed ===\n")

    except Exception as e:
        data_queue.put(f"Critical error: {str(e)}\n")
    finally:
        parsing_active = False


def get_data():
    global parsing_active
    button.config(state="disabled")
    parsing_active = True
    text1.config(state="normal")
    text1.delete(1.0, tk.END)
    text1.config(state="disabled")
    thread = threading.Thread(target=get_data_thread)
    thread.daemon = True
    thread.start()
    update_text_widget()

root = tk.Tk()
root.title("Parsing Shares Of Different Companies")
root.geometry("800x600")
root.resizable(False, False)
root.config(background="black")

button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=10)

button = tk.Button(button_frame,text="Find out information about company shares",font=("Arial", 14, "bold"),foreground="white",background="#262626",command=get_data,width=40,height=2)
button.pack()

text_frame = tk.Frame(root, bg="black")
text_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

text1 = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, width=90, height=25, font=("Consolas", 16), bg="#1a1a1a", fg="white", insertbackground="white")
text1.config(state="disabled")
text1.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root.mainloop()