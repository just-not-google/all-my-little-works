import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from translate import Translator
from gtts import gTTS
import pyperclip
from pydub import AudioSegment
from pydub.playback import play
import io
import os


# Функция озвучки текста
def speak(text, lang='ru'):
    try:
        tts = gTTS(text=text, lang=lang)
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        sound = AudioSegment.from_file(audio_data, format="mp3")
        play(sound)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось воспроизвести текст: {str(e)}")


# Функции копирования текста
def copy_source_text():
    text = txt.get("1.0", tk.END).strip()
    if text:
        pyperclip.copy(text)
        messagebox.showinfo("Успех", "Исходный текст скопирован!")


def copy_translated_text():
    text = txt1.get("1.0", tk.END).strip()
    if text:
        pyperclip.copy(text)
        messagebox.showinfo("Успех", "Переведенный текст скопирован!")


# Функции очистки текста
def delete_source_text():
    txt.delete('1.0', tk.END)


def delete_translated_text():
    txt1.delete('1.0', tk.END)


# Функция перевода
def translate_text():
    src_lang = combo.get()
    dest_lang = combo1.get()
    text_to_translate = txt.get("1.0", tk.END).strip()

    if not text_to_translate:
        messagebox.showwarning("Предупреждение", "Введите текст для перевода")
        return

    lang_codes = {
        "Русский": "ru",
        "Китайский": "zh"
    }

    try:
        translator = Translator(from_lang=lang_codes[src_lang], to_lang=lang_codes[dest_lang])
        translation = translator.translate(text_to_translate)
        txt1.delete("1.0", tk.END)
        txt1.insert(tk.END, translation)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка перевода: {str(e)}")


# Функции озвучки
def speak_source_text():
    text = txt.get("1.0", tk.END).strip()
    if text:
        lang = 'ru' if combo.get() == "Русский" else 'zh'
        speak(text, lang)


def speak_translated_text():
    text = txt1.get("1.0", tk.END).strip()
    if text:
        lang = 'ru' if combo1.get() == "Русский" else 'zh'
        speak(text, lang)


# Создание главного окна
root = tk.Tk()
root.geometry("640x740")
root.resizable(False, False)
root.title("ТекстоСеть (Версия 2.0)")

# Заголовки
heading = tk.Label(root, text="ТекстоСеть (Версия 2.0)", font=("Arial", 20, "bold"))
heading.pack(pady=10)
heading2 = tk.Label(root, text="Цифровой переводчик RUS-CHN", font=("Arial", 16))
heading2.pack()

# Настройка стилей Combobox
style = ttk.Style()
style.configure('TCombobox', font=('Arial', 14))

# Верхний блок (исходный текст)
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

# Combobox для выбора исходного языка
combo = ttk.Combobox(frame_top, values=["Русский", "Китайский"], width=20)
combo.set("Русский")
combo.grid(row=0, column=0, padx=5)

# Кнопки для исходного текста
copy_btn = tk.Button(frame_top, text="⎘", font=('Arial', 14), width=5, command=copy_source_text)
copy_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(frame_top, text="✕", font=('Arial', 14), width=5, command=delete_source_text)
delete_btn.grid(row=0, column=2, padx=5)

voice_btn = tk.Button(frame_top, text="🔊", font=('Arial', 14), width=5, command=speak_source_text)
voice_btn.grid(row=0, column=3, padx=5)

# Поле исходного текста
txt = scrolledtext.ScrolledText(root, font=('Arial', 14), width=40, height=8, wrap=tk.WORD)
txt.pack(pady=10)

# Кнопка перевода
translate_btn = tk.Button(root, text="Перевести", font=('Arial', 16), bg="#4CAF50", fg="white",
                          width=30, command=translate_text)
translate_btn.pack(pady=20)

# Нижний блок (переведенный текст)
frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

# Combobox для выбора языка перевода
combo1 = ttk.Combobox(frame_bottom, values=["Русский", "Китайский"], width=20)
combo1.set("Китайский")
combo1.grid(row=0, column=0, padx=5)

# Кнопки для переведенного текста
copy1_btn = tk.Button(frame_bottom, text="⎘", font=('Arial', 14), width=5, command=copy_translated_text)
copy1_btn.grid(row=0, column=1, padx=5)

delete1_btn = tk.Button(frame_bottom, text="✕", font=('Arial', 14), width=5, command=delete_translated_text)
delete1_btn.grid(row=0, column=2, padx=5)

voice1_btn = tk.Button(frame_bottom, text="🔊", font=('Arial', 14), width=5, command=speak_translated_text)
voice1_btn.grid(row=0, column=3, padx=5)

# Поле переведенного текста
txt1 = scrolledtext.ScrolledText(root, font=('Arial', 14), width=40, height=8, wrap=tk.WORD)
txt1.pack(pady=10)

# Запуск приложения
root.mainloop()