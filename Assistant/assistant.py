import time
import tkinter as tk
import random
import requests
from tkinter.scrolledtext import ScrolledText
import webbrowser
from googletrans import Translator
import pyperclip
import pyautogui
import speedtest
from data import lst_pass, keys, motivations

i = 0


def copy_text_1():
    try:
        global i
        green_get = label4.cget('text')
        pyperclip.copy(green_get)
        i += 1
        bu_tton.config(text=f"Скопировано ({i})")
        if i >= 99:
            bu_tton.config(text=f"Скопировано (100+)")
    except Exception as e:
        label4.config(text=f"{e}")


def help_func(y):
    root1 = tk.Toplevel()
    root1.title("Help")
    root1.resizable(False, False)
    root1.geometry("940x420")

    label1 = tk.Label(root1, text="Help", font=("Arial", 20, "bold"))
    label1.pack()

    label = tk.Label(root1, text="/ethernet - узнать скорость интернета\n"
                                 "/calculate <пример> - посчитать пример\n"
                                 "/rock paper scissors - сыграть в Камень-ножницы-бумага\n"
                                 "/generate password <длина пароля (6-32)> - сгенерировать пароль\n"
                                 "/converter <сумма> <валюта до перевода> <валюта после перевода> - сконвертировать валюту\n"
                                 "/guess the number - сыграть в Угадай число\n"
                                 "/analyze <текст> - анализ текста\n"
                                 "/search <поисковый запрос> - сделать поисковой запрос в браузер\n"
                                 "/translate <текст, который хочешь перевести> to <язык> - перевести текст\n"
                                 "/screenshot - сделать скриншот экрана\n"
                                 "/motivate - получить мотивационную речь\n", font=("Arial", 15), anchor='w',
                     justify="left")
    label.pack()


def about_func(y):
    root2 = tk.Toplevel()
    root2.title("About")
    root2.geometry("750x200")
    root2.resizable(False, False)

    label1 = tk.Label(root2, text="About", font=("Arial", 20, "bold"))
    label1.pack()

    label = tk.Label(root2, text="Привет! Я твой цифровой компаньон, этакий швейцарский армейский\n"
                                 "нож, но в мире чатов. У меня нет лишних деталей, только чистый \n"
                                 "функционал. Со мной не заскучаешь — просто выбери команду из \n"
                                 "списка, как выбираешь фильм вечером, и я исполню свою маленькую\n"
                                 "роль. Не обещаю философских бесед о смысле бытия, но с конкретными\n"
                                 "задачками справляюсь на ура. Давай же начнем?", font=("Arial", 15), anchor='w',
                     justify="left")
    label.pack()


def ethernet_func(y):
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000
        label4.config(text=f"Ответ машины: {download_speed:.2f} Мб/с")
    except Exception as e:
        label4.config(text=f"{e}")


def calculate_func(y):
    try:
        label4.config(text=f"Ответ машины: {eval(y[1])}")
    except Exception as e:
        label4.config(text=f"Ответ машины: {e}")


def rock_paper_scissors_func(y):
    def r_p_s():
        try:
            lst = ["камень", "ножницы", "бумага"]
            entr = entry_1.get().lower()
            if entr not in lst:
                label2.config(text="Ошибка: введите 'камень', 'ножницы' или 'бумага'")
                return

            random_gg = random.choice(lst)
            label3.config(text=f"Выбор машины: {random_gg}")

            if entr == random_gg:
                label2.config(text="Итоги раунда: Ничья")
            elif (entr == "камень" and random_gg == "ножницы") or \
                    (entr == "ножницы" and random_gg == "бумага") or \
                    (entr == "бумага" and random_gg == "камень"):
                label2.config(text="Итоги раунда: Победа")
            else:
                label2.config(text="Итоги раунда: Поражение")
        except Exception as e:
            label2.config(text=f"{e}")

    root4 = tk.Toplevel()
    root4.geometry("500x300")
    root4.resizable(False, False)
    root4.title("Rock Paper Scissors")

    label1 = tk.Label(root4, text="Rock Paper Scissors", font=("Arial", 20, "bold"))
    label1.pack()

    label = tk.Label(root4, text="Напишите: камень, ножницы, бумага", font=("Arial", 15), anchor='w', justify="left")
    label.pack(pady=(0, 15))

    entry_1 = tk.Entry(root4, font=("Arial", 20, "bold"), width=20)
    entry_1.pack(pady=(0, 15))

    button_st = tk.Button(root4, text=">>> Начать раунд <<<", font=("Arial", 20), width=20, foreground="white",
                          background="red", command=r_p_s)
    button_st.pack(pady=(0, 20))

    label2 = tk.Label(root4, text="Итоги раунда: -----", font=("Arial", 15), anchor='w', justify="left")
    label2.pack(pady=(0, 20))

    label3 = tk.Label(root4, text="Выбор машины: -----", font=("Arial", 15), anchor='w', justify="left")
    label3.pack()


def generate_password_func(y):
    try:
        hh = int(y[2])
        if hh < 6:
            label4.config(text=f"Ответ машины: пароль должен быть больше 6 символов")
        elif hh > 32:
            label4.config(text=f"Ответ машины: пароль должен быть меньше 32 символов")
        else:
            password_chars = []
            for i in range(hh):
                password_chars.append(random.choice(lst_pass))
            answer = "".join(password_chars)
            label4.config(text=f"Ответ машины: {answer}")
    except Exception as e:
        label4.config(text=f"{e}")


def converter_func(y):
    try:
        amount = int(y[1])
        cur_start = y[2]
        cur_end = y[3]
        response = requests.get(
            f"https://min-api.cryptocompare.com/data/price?fsym={keys[cur_start]}&tsyms={keys[cur_end]}")
        result = response.json()
        rate = result[keys[cur_end]] * amount
        label4.config(text=f"Ответ машины: {rate:.2f} {cur_end}")
    except Exception as e:
        label4.config(text=f"{e}")


def guess_the_number_func(y):
    hit_dd = random.randint(1, 100)

    def number_gg():
        try:
            get_gg = int(entry11.get())
            scr_text.configure(state="normal")
            scr_text.insert(tk.END, f"{get_gg}\n")
            scr_text.configure(state="disabled")
            scr_text.see(tk.END)

            if get_gg > hit_dd:
                scr_text.configure(state="normal")
                scr_text.insert(tk.END, f"Меньше\n")
                scr_text.configure(state="disabled")
            elif get_gg < hit_dd:
                scr_text.configure(state="normal")
                scr_text.insert(tk.END, f"Больше\n")
                scr_text.configure(state="disabled")
            else:
                scr_text.configure(state="normal")
                scr_text.insert(tk.END, f"Победа!\n")
                scr_text.configure(state="disabled")
                entry11.configure(state="disabled")
                but_ton.configure(state="disabled")
                root5.after(3000, root5.destroy)

            scr_text.see(tk.END)
        except Exception as e:
            scr_text.configure(state="normal")
            scr_text.insert(tk.END, f"Ошибка: {e}\n")
            scr_text.configure(state="disabled")
            scr_text.see(tk.END)

    root5 = tk.Toplevel()
    root5.geometry("500x600")
    root5.resizable(False, False)
    root5.title("Guess The Number")

    label11 = tk.Label(root5, text="Guess The Number", font=("Arial", 20, "bold"))
    label11.pack(pady=(10, 5))

    scr_text = ScrolledText(root5, font=("Arial", 15), height=18, width=34, state="disabled")
    scr_text.pack(pady=(0, 10))

    entry11 = tk.Entry(root5, font=("Arial", 20, "bold"), width=22)
    entry11.pack(pady=(0, 15))

    but_ton = tk.Button(root5, text=">>> Угадать <<<", font=("Arial", 20), width=20, foreground="white",
                        background="red", command=number_gg)
    but_ton.pack(pady=(0, 15))


def analyze_func(y):
    try:
        h = 0
        for i in y[1:]:
            h += len(i)
        label4.config(text=f"Ответ машины: слова - {len(y[1:])}, символы - {h}")
    except Exception as e:
        label4.config(text=f"{e}")


def search_func(y):
    try:
        dd = " ".join(y[1:])
        search_url = f"https://www.google.com/search?q={dd}"
        webbrowser.open(search_url)
        label4.config(text=f"Ответ машины: запрос выполняется")
    except Exception as e:
        label4.config(text=f"{e}")


def translate_func(y):
    try:
        # Находим индекс "to" в команде
        to_index = y.index("to")
        text = " ".join(y[1:to_index])
        dast_1 = y[to_index + 1]

        trg = Translator().translate(text, dest=dast_1)

        def copy_text_2():
            pyperclip.copy(trg.text)
            bu_tton_1.config(text="Скопирован текст")

        root69 = tk.Toplevel()
        root69.geometry("600x600")
        root69.title("Translate")
        root69.resizable(False, False)

        label1 = tk.Label(root69, text="Translate", font=("Arial", 20, "bold"))
        label1.pack()

        scr_text = ScrolledText(root69, font=("Arial", 15), height=20, width=36, state="normal")
        scr_text.insert(tk.END, f"{trg.text}\n")
        scr_text.configure(state="disabled")
        scr_text.pack(pady=(0, 10))

        bu_tton_1 = tk.Button(root69, text="Скопировать", font=("Arial", 20), width=20,
                              foreground="white", background="red", command=copy_text_2)
        bu_tton_1.pack()

    except Exception as e:
        label4.config(text=f"{e}")


def screenshot_func(y):
    try:
        grgr = pyautogui.screenshot()
        grgr.save("screen_shot.png")
        label4.config(text="Ответ машины: скриншот создан")
    except Exception as e:
        label4.config(text=f"{e}")


def motivate_func(y):
    try:
        motivation = random.choice(motivations)
        label4.config(text=f"Ответ машины: {motivation}")
    except Exception as e:
        label4.config(text=f"{e}")


def button_start():
    entry_g = entry.get()
    y = entry_g.split()

    if not y:
        label4.config(text="Ответ машины: введите команду")
        return

    command = y[0]

    if command == "/help":
        help_func(y)
    elif command == "/about":
        about_func(y)
    elif command == "/ethernet":
        ethernet_func(y)
    elif command == "/calculate" and len(y) >= 2:
        calculate_func(y)
    elif command == "/rock" and len(y) >= 3 and y[1] == "paper" and y[2] == "scissors":
        rock_paper_scissors_func(y)
    elif command == "/generate" and len(y) >= 3 and y[1] == "password":
        generate_password_func(y)
    elif command == "/converter" and len(y) >= 4:
        converter_func(y)
    elif command == "/guess" and len(y) >= 3 and y[1] == "the" and y[2] == "number":
        guess_the_number_func(y)
    elif command == "/analyze" and len(y) >= 2:
        analyze_func(y)
    elif command == "/search" and len(y) >= 2:
        search_func(y)
    elif command == "/translate" and len(y) >= 4 and "to" in y:
        translate_func(y)
    elif command == "/screenshot":
        screenshot_func(y)
    elif command == "/motivate":
        motivate_func(y)
    else:
        label4.config(text="Ответ машины: команда не найдена")


root = tk.Tk()
root.geometry("800x350")
root.resizable(False, False)
root.title("Assistant")

heading = tk.Label(root, text="Assistant", font=("Arial", 20, "bold"))
heading.pack()

about = tk.Label(root, text="Для показа списка команд впишите - /help\n"
                            "Для показа информации о боте - /about", font=("Arial", 15))
about.pack(pady=(0, 15))

entry = tk.Entry(root, font=("Arial", 20, "bold"), width=40)
entry.pack(pady=(0, 15))

button_start = tk.Button(root, text=">>> Выполнить команду <<<", font=("Arial", 20), width=38,
                         foreground="white", background="red", command=button_start)
button_start.pack(pady=(0, 15))

label4 = tk.Label(root, text="Ответ машины: -----", font=("Arial", 20), anchor='w', justify="left")
label4.pack(pady=(0, 15))

bu_tton = tk.Button(root, text="Скопировать (0)", font=("Arial", 20), width=38,
                    foreground="white", background="red", command=copy_text_1)
bu_tton.pack()

root.mainloop()