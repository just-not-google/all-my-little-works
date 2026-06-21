import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import time
import webbrowser
import pyautogui
import pyperclip
import requests
import threading
from datetime import datetime
import os
import ctypes
import pywifi
from pywifi import const
import keyboard
from PIL import Image, ImageTk
import json
import string

# Расширенные данные
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?/~`'
extended_special = '¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'

# Расширенный список слов для паролей
common_words = [
    'password', 'admin', 'user', 'login', 'welcome', 'hello', 'secret', 'qwerty',
    '123456', 'letmein', 'master', 'access', 'monkey', 'shadow', 'sunshine', 'princess',
    'dragon', 'baseball', 'football', 'mustang', 'superman', 'batman', 'wolverine',
    'computer', 'internet', 'network', 'system', 'security', 'privacy', 'protection',
    'diamond', 'crystal', 'silver', 'gold', 'platinum', 'android', 'iphone', 'samsung',
    'microsoft', 'google', 'amazon', 'facebook', 'twitter', 'instagram', 'youtube',
    'gaming', 'player', 'hunter', 'runner', 'walker', 'jumper', 'killer', 'fighter',
    'legend', 'warrior', 'ninja', 'samurai', 'viking', 'knight', 'king', 'queen',
    'prince', 'princess', 'castle', 'palace', 'forest', 'mountain', 'river', 'ocean',
    'thunder', 'lightning', 'storm', 'rainbow', 'sunset', 'sunrise', 'universe',
    'galaxy', 'planet', 'star', 'moon', 'comet', 'meteor', 'asteroid', 'nebula',
    'quantum', 'atomic', 'nuclear', 'plasma', 'laser', 'photon', 'electron', 'proton',
    'matrix', 'cyber', 'digital', 'virtual', 'reality', 'future', 'past', 'present',
    'eternity', 'infinity', 'paradox', 'mystery', 'puzzle', 'riddle', 'enigma',
    'phoenix', 'dragon', 'tiger', 'lion', 'eagle', 'hawk', 'falcon', 'wolf', 'fox',
    'bear', 'shark', 'whale', 'dolphin', 'octopus', 'python', 'java', 'javascript',
    'html', 'css', 'python', 'ruby', 'swift', 'kotlin', 'rust', 'golang', 'sql',
    'database', 'server', 'client', 'router', 'modem', 'ethernet', 'wifi', 'bluetooth',
    'quantum', 'algorithm', 'function', 'variable', 'constant', 'parameter', 'argument'
]

# Расширенный список тем для генерации паролей
password_themes = {
    "Технологии": ["tech", "code", "byte", "data", "cyber", "net", "web", "cloud", "AI", "VR"],
    "Природа": ["forest", "ocean", "mountain", "river", "sky", "earth", "fire", "water"],
    "Животные": ["dragon", "tiger", "eagle", "wolf", "lion", "shark", "phoenix"],
    "Мифология": ["zeus", "odin", "thor", "athena", "apollo", "hercules", "medusa"],
    "Наука": ["quantum", "atom", "neutron", "proton", "electron", "photon", "laser"],
    "Космос": ["galaxy", "star", "planet", "comet", "nebula", "orbit", "cosmos"]
}

# Расширенный список URL для пранков
urls = [
    'https://google.com', 'https://youtube.com', 'https://github.com',
    'https://stackoverflow.com', 'https://reddit.com', 'https://twitter.com',
    'https://instagram.com', 'https://facebook.com', 'https://linkedin.com',
    'https://wikipedia.org', 'https://amazon.com', 'https://ebay.com',
    'https://netflix.com', 'https://spotify.com', 'https://twitch.tv',
    'https://discord.com', 'https://telegram.org', 'https://whatsapp.com',
    'https://microsoft.com', 'https://apple.com', 'https://ubuntu.com',
    'https://python.org', 'https://java.com', 'https://rust-lang.org',
    'https://quora.com', 'https://medium.com', 'https://github.com',
    'https://gitlab.com', 'https://bitbucket.org', 'https://docker.com',
    'https://kubernetes.io', 'https://terraform.io', 'https://ansible.com'
]

# Расширенный список социальных сетей для сканирования
social_networks = {
    "Facebook": {"url": "https://facebook.com/{}", "icon": "🔵"},
    "Instagram": {"url": "https://instagram.com/{}", "icon": "🌈"},
    "Twitter/X": {"url": "https://twitter.com/{}", "icon": "🐦"},
    "GitHub": {"url": "https://github.com/{}", "icon": "💻"},
    "Reddit": {"url": "https://reddit.com/user/{}", "icon": "👽"},
    "YouTube": {"url": "https://youtube.com/@{}", "icon": "📺"},
    "LinkedIn": {"url": "https://linkedin.com/in/{}", "icon": "💼"},
    "TikTok": {"url": "https://tiktok.com/@{}", "icon": "🎵"},
    "Pinterest": {"url": "https://pinterest.com/{}", "icon": "📌"},
    "Telegram": {"url": "https://t.me/{}", "icon": "✈️"},
    "VK": {"url": "https://vk.com/{}", "icon": "🔷"},
    "Snapchat": {"url": "https://snapchat.com/add/{}", "icon": "👻"},
    "Twitch": {"url": "https://twitch.tv/{}", "icon": "🎮"},
    "Discord": {"url": "https://discord.com/users/{}", "icon": "🎭"},
    "Spotify": {"url": "https://open.spotify.com/user/{}", "icon": "🎵"},
    "Steam": {"url": "https://steamcommunity.com/id/{}", "icon": "🎮"},
    "Medium": {"url": "https://medium.com/@{}", "icon": "📝"},
    "DeviantArt": {"url": "https://{}.deviantart.com", "icon": "🎨"},
    "Flickr": {"url": "https://flickr.com/people/{}", "icon": "📷"},
    "Goodreads": {"url": "https://goodreads.com/{}", "icon": "📚"},
    "ResearchGate": {"url": "https://researchgate.net/profile/{}", "icon": "🔬"},
    "Academia": {"url": "https://independent.academia.edu/{}", "icon": "🎓"},
    "Keybase": {"url": "https://keybase.io/{}", "icon": "🔑"},
    "GitLab": {"url": "https://gitlab.com/{}", "icon": "🦊"},
    "Bitbucket": {"url": "https://bitbucket.org/{}", "icon": "🪣"},
    "DockerHub": {"url": "https://hub.docker.com/u/{}", "icon": "🐳"},
    "NPM": {"url": "https://npmjs.com/~{}", "icon": "📦"},
    "PyPI": {"url": "https://pypi.org/user/{}", "icon": "🐍"}
}


class MultiToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛠️ Ultimate Security Multi-Tool Suite")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1e1e1e")

        # Стили
        self.setup_styles()

        # Создание вкладок
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Создание различных вкладок
        self.create_password_generator_tab()
        self.create_social_scanner_tab()
        self.create_spam_bot_tab()
        self.create_wifi_bruteforce_tab()
        self.create_prank_tab()

        # Статус бар
        self.status_var = tk.StringVar()
        self.status_var.set("🟢 Готов к работе")
        self.status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)

        # Инициализация переменных
        self.password_history = []
        self.scan_results = {}

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        # Настройка стилей
        style.configure('TFrame', background='#2d2d2d')
        style.configure('TLabel', background='#2d2d2d', foreground='white')
        style.configure('TButton', background='#404040', foreground='white')
        style.configure('TEntry', fieldbackground='#404040', foreground='white')
        style.configure('TScrollbar', background='#404040')
        style.configure('TLabelframe', background='#2d2d2d', foreground='white')
        style.configure('TLabelframe.Label', background='#2d2d2d', foreground='white')

    def update_status(self, message):
        self.status_var.set(message)
        self.root.update()

    # ===== РАСШИРЕННЫЙ ГЕНЕРАТОР ПАРОЛЕЙ =====
    def create_password_generator_tab(self):
        self.pass_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.pass_tab, text="🔐 Генератор паролей")

        # Основной фрейм
        main_frame = ttk.LabelFrame(self.pass_tab, text="Расширенные настройки генерации паролей", padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Верхняя панель настроек
        settings_frame = ttk.Frame(main_frame)
        settings_frame.pack(fill=tk.X, pady=10)

        # Левая колонка
        left_col = ttk.Frame(settings_frame)
        left_col.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Label(left_col, text="Количество паролей:").pack(anchor=tk.W, pady=2)
        self.pass_count = ttk.Entry(left_col, width=15)
        self.pass_count.insert(0, "20")
        self.pass_count.pack(fill=tk.X, pady=2)

        ttk.Label(left_col, text="Минимальная длина:").pack(anchor=tk.W, pady=2)
        self.min_length = ttk.Entry(left_col, width=15)
        self.min_length.insert(0, "8")
        self.min_length.pack(fill=tk.X, pady=2)

        ttk.Label(left_col, text="Максимальная длина:").pack(anchor=tk.W, pady=2)
        self.max_length = ttk.Entry(left_col, width=15)
        self.max_length.insert(0, "16")
        self.max_length.pack(fill=tk.X, pady=2)

        # Центральная колонка
        center_col = ttk.Frame(settings_frame)
        center_col.pack(side=tk.LEFT, fill=tk.Y, padx=20)

        self.use_digits = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)
        self.use_extended = tk.BooleanVar(value=False)

        ttk.Checkbutton(center_col, text="Цифры (0-9)", variable=self.use_digits).pack(anchor=tk.W, pady=2)
        ttk.Checkbutton(center_col, text="Строчные буквы", variable=self.use_lower).pack(anchor=tk.W, pady=2)
        ttk.Checkbutton(center_col, text="Заглавные буквы", variable=self.use_upper).pack(anchor=tk.W, pady=2)
        ttk.Checkbutton(center_col, text="Спецсимволы", variable=self.use_special).pack(anchor=tk.W, pady=2)
        ttk.Checkbutton(center_col, text="Расширенные символы", variable=self.use_extended).pack(anchor=tk.W, pady=2)

        # Правая колонка
        right_col = ttk.Frame(settings_frame)
        right_col.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Label(right_col, text="Тематика паролей:").pack(anchor=tk.W, pady=2)
        self.theme_var = tk.StringVar(value="Случайная")
        theme_combo = ttk.Combobox(right_col, textvariable=self.theme_var, width=15)
        theme_combo['values'] = ["Случайная"] + list(password_themes.keys())
        theme_combo.pack(fill=tk.X, pady=2)

        ttk.Label(right_col, text="Задержка (сек):").pack(anchor=tk.W, pady=2)
        self.pass_delay = ttk.Entry(right_col, width=15)
        self.pass_delay.insert(0, "0.05")
        self.pass_delay.pack(fill=tk.X, pady=2)

        # Кнопки генерации
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=10)

        self.gen_simple_btn = ttk.Button(btn_frame, text="🎲 Простые пароли",
                                         command=lambda: self.start_password_generation("simple"))
        self.gen_simple_btn.pack(side=tk.LEFT, padx=5)

        self.gen_human_btn = ttk.Button(btn_frame, text="👤 Человеческие пароли",
                                        command=lambda: self.start_password_generation("human"))
        self.gen_human_btn.pack(side=tk.LEFT, padx=5)

        self.gen_strong_btn = ttk.Button(btn_frame, text="🛡️ Сильные пароли",
                                         command=lambda: self.start_password_generation("strong"))
        self.gen_strong_btn.pack(side=tk.LEFT, padx=5)

        self.gen_themed_btn = ttk.Button(btn_frame, text="🎭 Тематические пароли",
                                         command=lambda: self.start_password_generation("themed"))
        self.gen_themed_btn.pack(side=tk.LEFT, padx=5)

        # Область вывода
        output_frame = ttk.Frame(main_frame)
        output_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Панель инструментов вывода
        tools_frame = ttk.Frame(output_frame)
        tools_frame.pack(fill=tk.X, pady=5)

        ttk.Label(tools_frame, text="Сгенерированные пароли:").pack(side=tk.LEFT)

        ttk.Button(tools_frame, text="📋 Копировать все",
                   command=self.copy_all_passwords).pack(side=tk.RIGHT, padx=5)
        ttk.Button(tools_frame, text="💾 Сохранить в файл",
                   command=self.save_passwords_to_file).pack(side=tk.RIGHT, padx=5)
        ttk.Button(tools_frame, text="🧹 Очистить",
                   command=self.clear_passwords).pack(side=tk.RIGHT, padx=5)

        self.pass_output = scrolledtext.ScrolledText(output_frame, height=20, width=80,
                                                     bg="#1e1e1e", fg="#00ff00",
                                                     font=("Consolas", 10))
        self.pass_output.pack(fill=tk.BOTH, expand=True)

    def get_character_set(self):
        chars = ""
        if self.use_digits.get():
            chars += digits
        if self.use_lower.get():
            chars += lowercase_letters
        if self.use_upper.get():
            chars += uppercase_letters
        if self.use_special.get():
            chars += special_characters
        if self.use_extended.get():
            chars += extended_special

        return chars if chars else digits + lowercase_letters  # fallback

    def generate_simple_password(self, length):
        chars = self.get_character_set()
        return ''.join(random.choice(chars) for _ in range(length))

    def generate_strong_password(self, length):
        # Гарантирует наличие разных типов символов
        parts = []
        if self.use_digits.get():
            parts.append(random.choice(digits))
        if self.use_lower.get():
            parts.append(random.choice(lowercase_letters))
        if self.use_upper.get():
            parts.append(random.choice(uppercase_letters))
        if self.use_special.get():
            parts.append(random.choice(special_characters))

        chars = self.get_character_set()
        while len(parts) < length:
            parts.append(random.choice(chars))

        random.shuffle(parts)
        return ''.join(parts[:length])

    def generate_themed_password(self, length):
        theme = self.theme_var.get()
        if theme == "Случайная":
            theme = random.choice(list(password_themes.keys()))

        theme_words = password_themes[theme]
        base_word = random.choice(theme_words)

        # Добавляем вариации
        variations = [
            base_word + str(random.randint(10, 999)),
            base_word.capitalize() + random.choice(special_characters),
            base_word + random.choice(special_characters) + str(random.randint(1, 99)),
            base_word.upper() + random.choice(special_characters) + random.choice(theme_words)
        ]

        password = random.choice(variations)

        # Добиваем до нужной длины если необходимо
        chars = self.get_character_set()
        while len(password) < length:
            password += random.choice(chars)

        return password[:length]

    def start_password_generation(self, mode):
        try:
            num = int(self.pass_count.get())
            min_len = int(self.min_length.get())
            max_len = int(self.max_length.get())
            delay = float(self.pass_delay.get())

            if min_len > max_len:
                messagebox.showerror("Ошибка", "Минимальная длина не может быть больше максимальной")
                return

            self.pass_output.delete(1.0, tk.END)
            self.update_status("🔄 Генерация паролей...")

            def generate():
                passwords = []
                for i in range(num):
                    length = random.randint(min_len, max_len)

                    if mode == "simple":
                        password = self.generate_simple_password(length)
                    elif mode == "strong":
                        password = self.generate_strong_password(length)
                    elif mode == "themed":
                        password = self.generate_themed_password(length)
                    else:  # human
                        password = random.choice([
                            self.human_password_1(), self.human_password_2(),
                            self.human_password_3(), self.human_password_4(),
                            self.human_password_5(), self.human_password_6()
                        ])

                    passwords.append(password)
                    time.sleep(delay)

                self.password_history.extend(passwords)
                self.root.after(0, lambda: self.display_passwords(passwords, mode))

            threading.Thread(target=generate, daemon=True).start()

        except ValueError as e:
            messagebox.showerror("Ошибка", f"Проверьте правильность введенных значений: {e}")

    def display_passwords(self, passwords, mode):
        self.pass_output.delete(1.0, tk.END)
        for i, pwd in enumerate(passwords, 1):
            strength = self.calculate_password_strength(pwd)
            strength_icon = "🟢" if strength > 70 else "🟡" if strength > 50 else "🔴"
            self.pass_output.insert(tk.END, f"{i:2d}. {pwd} {strength_icon} ({strength}%)\n")

        self.update_status(f"✅ Сгенерировано {len(passwords)} паролей ({mode})")

    def calculate_password_strength(self, password):
        score = 0
        if len(password) >= 8: score += 25
        if len(password) >= 12: score += 15
        if any(c.isdigit() for c in password): score += 20
        if any(c.islower() for c in password): score += 10
        if any(c.isupper() for c in password): score += 10
        if any(c in special_characters for c in password): score += 20
        if len(password) >= 16: score += 10
        return min(score, 100)

    def copy_all_passwords(self):
        passwords = self.pass_output.get(1.0, tk.END).strip()
        if passwords:
            pyperclip.copy(passwords)
            self.update_status("📋 Все пароли скопированы в буфер")

    def save_passwords_to_file(self):
        passwords = self.pass_output.get(1.0, tk.END).strip()
        if passwords:
            filename = f"passwords_{int(time.time())}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(passwords)
            self.update_status(f"💾 Пароли сохранены в {filename}")

    def clear_passwords(self):
        self.pass_output.delete(1.0, tk.END)
        self.update_status("🧹 Список паролей очищен")

    # Методы генерации человеческих паролей (из оригинального кода)
    def hh(self):
        try:
            return random.randint(1, 9999999)
        except Exception:
            return 0

    def special_hh(self):
        try:
            v = []
            for i in range(random.randint(1, 10)):
                i = random.choice(special_characters)
                v.append(i)
            return "".join(v)
        except Exception:
            return ""

    def text_upper_lower(self):
        try:
            f = random.choice(common_words)
            x_1 = []
            for i in f:
                if random.choice([True, False]):
                    h = i.lower() if i.isupper() else i.upper()
                else:
                    h = i
                x_1.append(h)
            return "".join(x_1)
        except Exception:
            return ""

    def human_password_1(self):
        return f"{random.choice(common_words)}_{self.hh()}"

    def human_password_2(self):
        return f"{self.text_upper_lower()}_{self.hh()}"

    def human_password_3(self):
        return f"{self.hh()}_{self.text_upper_lower()}"

    def human_password_4(self):
        return f"{self.hh()}_{random.choice(common_words)}"

    def human_password_5(self):
        return f"{self.hh()}_{random.choice(common_words)}_{self.hh()}"

    def human_password_6(self):
        return f"{self.hh()}_{self.text_upper_lower()}_{self.hh()}"

    # ===== РАСШИРЕННЫЙ СОЦИАЛЬНЫЙ СКАНЕР =====
    def create_social_scanner_tab(self):
        self.social_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.social_tab, text="🔍 Социальный сканер")

        main_frame = ttk.Frame(self.social_tab)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Панель поиска
        search_frame = ttk.LabelFrame(main_frame, text="Поиск профилей", padding=10)
        search_frame.pack(fill=tk.X, pady=10)

        ttk.Label(search_frame, text="Имя пользователя:").pack(anchor=tk.W)
        self.username_entry = ttk.Entry(search_frame, width=40, font=("Arial", 12))
        self.username_entry.pack(fill=tk.X, pady=5)

        # Кнопки поиска
        btn_frame = ttk.Frame(search_frame)
        btn_frame.pack(fill=tk.X, pady=10)

        self.scan_btn = ttk.Button(btn_frame, text="🔍 Начать поиск",
                                   command=self.start_social_scan)
        self.scan_btn.pack(side=tk.LEFT, padx=5)

        self.save_scan_btn = ttk.Button(btn_frame, text="💾 Сохранить результаты",
                                        command=self.save_scan_results)
        self.save_scan_btn.pack(side=tk.LEFT, padx=5)

        # Прогресс бар
        self.progress = ttk.Progressbar(search_frame, mode='determinate')
        self.progress.pack(fill=tk.X, pady=5)

        # Результаты
        results_frame = ttk.LabelFrame(main_frame, text="Результаты поиска", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Создание Treeview для результатов
        columns = ('platform', 'status', 'url')
        self.results_tree = ttk.Treeview(results_frame, columns=columns, show='headings', height=15)

        self.results_tree.heading('platform', text='Платформа')
        self.results_tree.heading('status', text='Статус')
        self.results_tree.heading('url', text='URL')

        self.results_tree.column('platform', width=150)
        self.results_tree.column('status', width=100)
        self.results_tree.column('url', width=300)

        # Scrollbar для Treeview
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.results_tree.yview)
        self.results_tree.configure(yscrollcommand=scrollbar.set)

        self.results_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Контекстное меню
        self.create_context_menu()

    def create_context_menu(self):
        self.context_menu = tk.Menu(self.results_tree, tearoff=0)
        self.context_menu.add_command(label="📋 Копировать URL", command=self.copy_selected_url)
        self.context_menu.add_command(label="🌐 Открыть в браузере", command=self.open_selected_url)

        self.results_tree.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self, event):
        item = self.results_tree.identify_row(event.y)
        if item:
            self.results_tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)

    def copy_selected_url(self):
        selected = self.results_tree.selection()
        if selected:
            url = self.results_tree.item(selected[0])['values'][2]
            pyperclip.copy(url)
            self.update_status("📋 URL скопирован в буфер")

    def open_selected_url(self):
        selected = self.results_tree.selection()
        if selected:
            url = self.results_tree.item(selected[0])['values'][2]
            webbrowser.open(url)
            self.update_status(f"🌐 Открываю {url}")

    def start_social_scan(self):
        username = self.username_entry.get().strip()
        if not username:
            messagebox.showwarning("Внимание", "Введите имя пользователя для поиска")
            return

        # Очистка предыдущих результатов
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)

        self.progress['maximum'] = len(social_networks)
        self.progress['value'] = 0
        self.update_status(f"🔍 Сканирование профилей для: {username}")

        def scan():
            results = []
            for i, (platform, data) in enumerate(social_networks.items()):
                if not self.scan_btn['state'] == 'normal':  # Проверка на остановку
                    break

                try:
                    url = data['url'].format(username)
                    icon = data['icon']

                    response = requests.get(url, timeout=10,
                                            headers={
                                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})

                    if response.status_code == 200:
                        status = "✅ Найден"
                        tags = ('found',)
                    elif response.status_code == 404:
                        status = "❌ Не найден"
                        tags = ('not_found',)
                    else:
                        status = "⚠️ Ошибка"
                        tags = ('error',)

                    results.append((f"{icon} {platform}", status, url))

                    # ИСПРАВЛЕННАЯ СТРОКА: использование отдельной функции для обновления прогресса
                    self.root.after(0, lambda idx=i: self.update_progress(idx))
                    self.root.after(0, lambda r=results[-1]: self.add_result_to_tree(r))

                except Exception as e:
                    results.append((f"🔵 {platform}", f"❌ Ошибка", url))
                    self.root.after(0, lambda r=results[-1]: self.add_result_to_tree(r))
                    self.root.after(0, lambda idx=i: self.update_progress(idx))

            self.root.after(0, lambda: self.update_status("✅ Сканирование завершено"))
            self.root.after(0, lambda: self.scan_btn.config(state='normal'))
            self.scan_results[username] = results

        self.scan_btn.config(state='disabled')
        threading.Thread(target=scan, daemon=True).start()

    def update_progress(self, idx):
        """Обновление прогресс бара"""
        self.progress['value'] = idx + 1

    def add_result_to_tree(self, result):
        platform, status, url = result
        tags = ()
        if "✅" in status:
            tags = ('found',)
        elif "❌" in status:
            tags = ('not_found',)
        else:
            tags = ('error',)

        self.results_tree.insert('', tk.END, values=(platform, status, url), tags=tags)

    def save_scan_results(self):
        if not self.results_tree.get_children():
            messagebox.showwarning("Внимание", "Нет результатов для сохранения")
            return

        filename = f"social_scan_{int(time.time())}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Результаты социального сканирования\n")
            f.write(f"Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Пользователь: {self.username_entry.get()}\n")
            f.write("=" * 50 + "\n\n")

            for item in self.results_tree.get_children():
                values = self.results_tree.item(item)['values']
                f.write(f"{values[0]} - {values[1]}\n")
                f.write(f"URL: {values[2]}\n\n")

        self.update_status(f"💾 Результаты сохранены в {filename}")

    # ===== СПАМ БОТ =====
    def create_spam_bot_tab(self):
        self.spam_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.spam_tab, text="🤖 Спам-бот")

        main_frame = ttk.LabelFrame(self.spam_tab, text="Настройки спам-рассылки", padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Поля ввода
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)

        # Левая колонка
        left_col = ttk.Frame(input_frame)
        left_col.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Label(left_col, text="Задержка перед запуском (сек):").pack(anchor=tk.W, pady=5)
        self.delay_entry = ttk.Entry(left_col, width=20)
        self.delay_entry.insert(0, "5")
        self.delay_entry.pack(fill=tk.X, pady=5)

        ttk.Label(left_col, text="Количество сообщений:").pack(anchor=tk.W, pady=5)
        self.msg_count_entry = ttk.Entry(left_col, width=20)
        self.msg_count_entry.insert(0, "10")
        self.msg_count_entry.pack(fill=tk.X, pady=5)

        # Правая колонка
        right_col = ttk.Frame(input_frame)
        right_col.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Label(right_col, text="Задержка между сообщениями (сек):").pack(anchor=tk.W, pady=5)
        self.msg_delay_entry = ttk.Entry(right_col, width=20)
        self.msg_delay_entry.insert(0, "0.5")
        self.msg_delay_entry.pack(fill=tk.X, pady=5)

        ttk.Label(right_col, text="Тип сообщения:").pack(anchor=tk.W, pady=5)
        self.msg_type_var = tk.StringVar(value="Случайное")
        msg_type_combo = ttk.Combobox(right_col, textvariable=self.msg_type_var, width=18)
        msg_type_combo['values'] = ["Случайное", "Приветствие", "Реклама", "Шутка", "Спам"]
        msg_type_combo.pack(fill=tk.X, pady=5)

        # Поле текста сообщения
        ttk.Label(main_frame, text="Текст сообщения:").pack(anchor=tk.W, pady=(10, 5))
        self.msg_text_entry = scrolledtext.ScrolledText(main_frame, height=4, width=80)
        self.msg_text_entry.pack(fill=tk.X, pady=5)
        self.msg_text_entry.insert('1.0', "Это тестовое сообщение от спам-бота! 🚀")

        # Кнопки управления
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=15)

        self.start_spam_btn = ttk.Button(btn_frame, text="🚀 Начать спам",
                                         command=self.start_spam)
        self.start_spam_btn.pack(side=tk.LEFT, padx=5)

        self.stop_spam_btn = ttk.Button(btn_frame, text="🛑 Остановить",
                                        command=self.stop_spam, state=tk.DISABLED)
        self.stop_spam_btn.pack(side=tk.LEFT, padx=5)

        # Лог выполнения
        ttk.Label(main_frame, text="Лог выполнения:").pack(anchor=tk.W, pady=(10, 5))
        self.spam_log = scrolledtext.ScrolledText(main_frame, height=12,
                                                  bg="#1e1e1e", fg="#00ff00")
        self.spam_log.pack(fill=tk.BOTH, expand=True)

        self.spam_running = False

    def get_message_text(self):
        message_type = self.msg_type_var.get()
        custom_text = self.msg_text_entry.get('1.0', tk.END).strip()

        if custom_text and message_type == "Случайное":
            return custom_text

        messages = {
            "Приветствие": ["Привет! 👋", "Добрый день! 😊", "Здравствуйте! 🎉", "Приветствую! 🌟"],
            "Реклама": ["Акция! Скидки 50%! 🏷️", "Уникальное предложение! 🔥", "Только сегодня! ⚡"],
            "Шутка": ["Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25! 😄",
                      "Какой язык программирования самый крутой? Python, конечно! 🐍"],
            "Спам": ["Срочное сообщение! 📢", "Важно! Не пропустите! 🔔", "Внимание! Новость! 📰"]
        }

        if message_type in messages:
            return random.choice(messages[message_type])
        else:
            return custom_text if custom_text else "Тестовое сообщение! 🚀"

    def start_spam(self):
        try:
            delay = int(self.delay_entry.get())
            count = int(self.msg_count_entry.get())
            msg_delay = float(self.msg_delay_entry.get())

            self.spam_log.delete(1.0, tk.END)
            self.spam_running = True
            self.start_spam_btn.config(state=tk.DISABLED)
            self.stop_spam_btn.config(state=tk.NORMAL)
            self.update_status("🔄 Подготовка к спаму...")

            def spam():
                # Обратный отсчет
                for i in range(delay, 0, -1):
                    if not self.spam_running:
                        break
                    self.root.after(0, lambda x=i: self.spam_log.insert(tk.END, f"⏳ {x} секунд до начала...\n"))
                    self.root.after(0, lambda: self.spam_log.see(tk.END))
                    time.sleep(1)

                if not self.spam_running:
                    return

                self.root.after(0, lambda: self.spam_log.insert(tk.END, "🎯 Начало спама!\n"))
                self.root.after(0, lambda: self.spam_log.see(tk.END))

                # Отправка сообщений
                for i in range(count):
                    if not self.spam_running:
                        break

                    message = self.get_message_text()
                    pyautogui.typewrite(message)
                    pyautogui.press('enter')

                    self.root.after(0, lambda x=i: self.spam_log.insert(tk.END,
                                                                        f"📤 Отправлено {x + 1}/{count}: {message}\n"))
                    self.root.after(0, lambda: self.spam_log.see(tk.END))

                    time.sleep(msg_delay)

                self.root.after(0, self.spam_finished)

            threading.Thread(target=spam, daemon=True).start()

        except ValueError:
            messagebox.showerror("Ошибка", "Проверьте правильность введенных значений")

    def stop_spam(self):
        self.spam_running = False
        self.start_spam_btn.config(state=tk.NORMAL)
        self.stop_spam_btn.config(state=tk.DISABLED)
        self.spam_log.insert(tk.END, "🛑 Спам остановлен пользователем\n")
        self.update_status("🛑 Спам остановлен")

    def spam_finished(self):
        self.spam_running = False
        self.start_spam_btn.config(state=tk.NORMAL)
        self.stop_spam_btn.config(state=tk.DISABLED)
        self.spam_log.insert(tk.END, "✅ Спам завершен!\n")
        self.update_status("✅ Спам завершен")

    # ===== WI-FI BRUTEFORCE =====
    def create_wifi_bruteforce_tab(self):
        self.wifi_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.wifi_tab, text="📶 Wi-Fi Bruteforce")

        main_frame = ttk.LabelFrame(self.wifi_tab, text="Подбор паролей Wi-Fi", padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Настройки
        settings_frame = ttk.Frame(main_frame)
        settings_frame.pack(fill=tk.X, pady=10)

        ttk.Label(settings_frame, text="SSID сети:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.ssid_entry = ttk.Entry(settings_frame, width=30)
        self.ssid_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        ttk.Label(settings_frame, text="Длина пароля:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.pass_len_entry = ttk.Entry(settings_frame, width=10)
        self.pass_len_entry.insert(0, "8")
        self.pass_len_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Кнопки управления
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=10)

        self.wifi_start_btn = ttk.Button(btn_frame, text="🎯 Начать подбор",
                                         command=self.start_wifi_bruteforce)
        self.wifi_start_btn.pack(side=tk.LEFT, padx=5)

        self.wifi_stop_btn = ttk.Button(btn_frame, text="🛑 Остановить",
                                        command=self.stop_wifi_bruteforce, state=tk.DISABLED)
        self.wifi_stop_btn.pack(side=tk.LEFT, padx=5)

        # Статистика
        stats_frame = ttk.Frame(main_frame)
        stats_frame.pack(fill=tk.X, pady=10)

        ttk.Label(stats_frame, text="Попыток:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.attempts_label = ttk.Label(stats_frame, text="0")
        self.attempts_label.grid(row=0, column=1, sticky=tk.W, pady=2)

        ttk.Label(stats_frame, text="Текущий пароль:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.current_pass_label = ttk.Label(stats_frame, text="")
        self.current_pass_label.grid(row=1, column=1, sticky=tk.W, pady=2)

        ttk.Label(stats_frame, text="Скорость:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.speed_label = ttk.Label(stats_frame, text="0/сек")
        self.speed_label.grid(row=2, column=1, sticky=tk.W, pady=2)

        # Лог
        ttk.Label(main_frame, text="Лог подбора:").pack(anchor=tk.W, pady=(10, 5))
        self.wifi_log = scrolledtext.ScrolledText(main_frame, height=15,
                                                  bg="#1e1e1e", fg="#00ff00")
        self.wifi_log.pack(fill=tk.BOTH, expand=True)

        self.wifi_running = False
        self.attempts = 0
        self.start_time = 0
        self.allowed_chars = list(digits + lowercase_letters + uppercase_letters + special_characters)

    def start_wifi_bruteforce(self):
        ssid = self.ssid_entry.get().strip()
        if not ssid:
            messagebox.showwarning("Внимание", "Введите SSID сети")
            return

        try:
            length = int(self.pass_len_entry.get())
            if length < 4 or length > 20:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Длина пароля должна быть от 4 до 20 символов")
            return

        self.wifi_running = True
        self.attempts = 0
        self.start_time = time.time()
        self.wifi_start_btn.config(state=tk.DISABLED)
        self.wifi_stop_btn.config(state=tk.NORMAL)
        self.wifi_log.delete(1.0, tk.END)
        self.wifi_log.insert(tk.END, f"🎯 Начало подбора пароля для сети: {ssid}\n")
        self.update_status("🔄 Подбор паролей Wi-Fi...")

        def bruteforce():
            while self.wifi_running and self.attempts < 1000:  # Лимит для демонстрации
                password = ''.join(random.choice(self.allowed_chars) for _ in range(length))
                self.attempts += 1

                # Обновление UI
                self.root.after(0, lambda: self.attempts_label.config(text=str(self.attempts)))
                self.root.after(0, lambda: self.current_pass_label.config(text=password))

                # Обновление скорости
                elapsed = time.time() - self.start_time
                speed = self.attempts / elapsed if elapsed > 0 else 0
                self.root.after(0, lambda: self.speed_label.config(text=f"{speed:.1f}/сек"))

                # Здесь должна быть реальная проверка подключения к Wi-Fi
                # Для демонстрации просто ждем
                time.sleep(0.01)

                # Имитация найденного пароля (для демонстрации)
                if self.attempts % 100 == 0 and random.random() < 0.05:  # Случайный "успех"
                    self.root.after(0, lambda: self.wifi_success(ssid, password))
                    break

            if self.wifi_running:
                self.root.after(0, lambda: self.wifi_log.insert(tk.END, "⚠️ Достигнут лимит попыток\n"))
                self.root.after(0, self.wifi_finished)

        threading.Thread(target=bruteforce, daemon=True).start()

    def stop_wifi_bruteforce(self):
        self.wifi_running = False
        self.wifi_start_btn.config(state=tk.NORMAL)
        self.wifi_stop_btn.config(state=tk.DISABLED)
        self.wifi_log.insert(tk.END, "🛑 Подбор остановлен\n")
        self.update_status("🛑 Подбор паролей остановлен")

    def wifi_success(self, ssid, password):
        self.wifi_running = False
        elapsed = time.time() - self.start_time
        speed = self.attempts / elapsed if elapsed > 0 else 0

        self.wifi_log.insert(tk.END, f"🎉 УСПЕХ! Пароль найден: {password}\n")
        self.wifi_log.insert(tk.END, f"📊 Статистика:\n")
        self.wifi_log.insert(tk.END, f"   Попыток: {self.attempts}\n")
        self.wifi_log.insert(tk.END, f"   Время: {elapsed:.1f} сек\n")
        self.wifi_log.insert(tk.END, f"   Скорость: {speed:.1f} попыток/сек\n")

        messagebox.showinfo("Успех", f"Пароль для сети {ssid}:\n{password}\n\nПопыток: {self.attempts}")
        self.wifi_finished()

    def wifi_finished(self):
        self.wifi_running = False
        self.wifi_start_btn.config(state=tk.NORMAL)
        self.wifi_stop_btn.config(state=tk.DISABLED)
        self.update_status("✅ Подбор паролей завершен")

    # ===== РАСШИРЕННЫЕ PRANK TOOLS =====
    def create_prank_tab(self):
        self.prank_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.prank_tab, text="🎭 Prank Tools")

        main_frame = ttk.LabelFrame(self.prank_tab, text="Расширенные инструменты для пранков", padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Сетка кнопок пранков
        prank_grid = ttk.Frame(main_frame)
        prank_grid.pack(fill=tk.X, pady=10)

        # Первый ряд
        row1 = ttk.Frame(prank_grid)
        row1.pack(fill=tk.X, pady=5)

        self.prank1_btn = ttk.Button(row1, text="🌐 Открыть случайные сайты",
                                     command=self.open_random_sites, width=25)
        self.prank1_btn.pack(side=tk.LEFT, padx=5)

        self.prank2_btn = ttk.Button(row1, text="📸 Сделать скриншоты",
                                     command=self.take_screenshots, width=25)
        self.prank2_btn.pack(side=tk.LEFT, padx=5)

        # Второй ряд
        row2 = ttk.Frame(prank_grid)
        row2.pack(fill=tk.X, pady=5)

        self.prank3_btn = ttk.Button(row2, text="🎮 Случайные действия",
                                     command=self.random_actions, width=25)
        self.prank3_btn.pack(side=tk.LEFT, padx=5)

        self.prank4_btn = ttk.Button(row2, text="💻 Имитация работы",
                                     command=self.fake_work, width=25)
        self.prank4_btn.pack(side=tk.LEFT, padx=5)

        # Третий ряд
        row3 = ttk.Frame(prank_grid)
        row3.pack(fill=tk.X, pady=5)

        self.prank5_btn = ttk.Button(row3, text="🔊 Громкие звуки",
                                     command=self.loud_sounds, width=25)
        self.prank5_btn.pack(side=tk.LEFT, padx=5)

        self.prank6_btn = ttk.Button(row3, text="🖥️ Смена обоев",
                                     command=self.change_wallpaper, width=25)
        self.prank6_btn.pack(side=tk.LEFT, padx=5)

        # Кнопка остановки
        self.stop_prank_btn = ttk.Button(prank_grid, text="🛑 Остановить все пранки",
                                         command=self.stop_pranks, state=tk.DISABLED)
        self.stop_prank_btn.pack(pady=10)

        # Лог пранков
        log_frame = ttk.LabelFrame(main_frame, text="Лог действий", padding=10)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.prank_log = scrolledtext.ScrolledText(log_frame, height=15,
                                                   bg="#1e1e1e", fg="#00ff00")
        self.prank_log.pack(fill=tk.BOTH, expand=True)

        self.prank_running = False

    def open_random_sites(self):
        self.start_prank_operation("Открытие случайных сайтов")

        def open_sites():
            count = random.randint(5, 15)
            self.root.after(0, lambda: self.prank_log.insert(tk.END, f"📡 Будет открыто {count} сайтов\n"))

            for i in range(count):
                if not self.prank_running:
                    break
                url = random.choice(urls)
                self.root.after(0, lambda u=url: self.prank_log.insert(tk.END, f"🌐 Открываю: {u}\n"))
                webbrowser.open(url, new=2)
                time.sleep(random.randint(1, 3))

            self.finish_prank_operation("Открытие сайтов завершено")

        threading.Thread(target=open_sites, daemon=True).start()

    def take_screenshots(self):
        self.start_prank_operation("Создание скриншотов")

        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        screenshot_dir = os.path.join(desktop, "Funny_Screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        self.root.after(0, lambda: self.prank_log.insert(tk.END, f"📁 Скриншоты сохраняются в: {screenshot_dir}\n"))

        def take_shots():
            count = random.randint(3, 8)
            for i in range(count):
                if not self.prank_running:
                    break
                try:
                    screenshot = pyautogui.screenshot()
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"prank_screenshot_{timestamp}_{i + 1}.png"
                    filepath = os.path.join(screenshot_dir, filename)
                    screenshot.save(filepath)
                    self.root.after(0, lambda f=filename: self.prank_log.insert(tk.END, f"📸 Скриншот сохранен: {f}\n"))
                    time.sleep(random.randint(1, 2))
                except Exception as e:
                    self.root.after(0, lambda: self.prank_log.insert(tk.END, f"❌ Ошибка: {e}\n"))

            self.finish_prank_operation("Создание скриншотов завершено")

        threading.Thread(target=take_shots, daemon=True).start()

    def random_actions(self):
        self.start_prank_operation("Случайные действия")

        def random_act():
            actions = random.randint(5, 12)
            action_types = [
                "набор текста", "нажатие клавиш", "перемещение мыши",
                "клики", "прокрутка", "активация окон"
            ]

            for i in range(actions):
                if not self.prank_running:
                    break

                action_type = random.choice(action_types)

                if action_type == "набор текста":
                    texts = ["Hello World!", "Test message", "Just pranking...", "Having fun!", "Python is awesome!"]
                    text = random.choice(texts)
                    pyautogui.typewrite(text)
                    self.root.after(0, lambda: self.prank_log.insert(tk.END, f"⌨️  Набран текст: '{text}'\n"))

                elif action_type == "нажатие клавиш":
                    key_combos = [['ctrl', 'c'], ['ctrl', 'v'], ['alt', 'tab'], ['win', 'd'], ['ctrl', 'shift', 'esc']]
                    keys = random.choice(key_combos)
                    pyautogui.hotkey(*keys)
                    self.root.after(0, lambda: self.prank_log.insert(tk.END, f"🔘 Нажаты клавиши: {keys}\n"))

                elif action_type == "перемещение мыши":
                    x, y = random.randint(100, 1000), random.randint(100, 700)
                    pyautogui.moveTo(x, y, duration=0.5)
                    self.root.after(0, lambda: self.prank_log.insert(tk.END, f"🖱️  Мышь перемещена в ({x}, {y})\n"))

                elif action_type == "клики":
                    pyautogui.click()
                    self.root.after(0, lambda: self.prank_log.insert(tk.END, f"👆 Выполнен клик\n"))

                elif action_type == "прокрутка":
                    scroll_amount = random.randint(-5, 5)
                    pyautogui.scroll(scroll_amount)
                    self.root.after(0, lambda: self.prank_log.insert(tk.END, f"📜 Прокрутка: {scroll_amount}\n"))

                time.sleep(random.randint(1, 3))

            self.finish_prank_operation("Случайные действия завершены")

        threading.Thread(target=random_act, daemon=True).start()

    def fake_work(self):
        self.start_prank_operation("Имитация работы")

        def fake_work_task():
            work_actions = [
                "Анализирую данные...",
                "Компилирую код...",
                "Запускаю тесты...",
                "Оптимизирую алгоритмы...",
                "Рефакторю код...",
                "Синхронизирую с репозиторием...",
                "Создаю документацию...",
                "Провожу code review...",
                "Дебажу приложение...",
                "Собираю проект..."
            ]

            for i in range(random.randint(8, 15)):
                if not self.prank_running:
                    break

                action = random.choice(work_actions)
                self.root.after(0, lambda a=action: self.prank_log.insert(tk.END, f"💼 {a}\n"))

                # Имитация набора кода
                if random.random() > 0.3:
                    code_snippets = ["def main():", "print('Hello')", "for i in range(10):", "if x > 0:", "return True"]
                    snippet = random.choice(code_snippets)
                    pyautogui.typewrite(snippet + "\n")

                time.sleep(random.randint(2, 5))

            self.finish_prank_operation("Имитация работы завершена")

        threading.Thread(target=fake_work_task, daemon=True).start()

    def loud_sounds(self):
        self.start_prank_operation("Громкие звуки")

        def sound_prank():
            # Максимальная громкость
            for _ in range(50):
                pyautogui.press('volumeup')

            self.root.after(0, lambda: self.prank_log.insert(tk.END, "🔊 Громкость установлена на максимум!\n"))

            # Имитация звуковых эффектов
            sounds = ["BEEP!", "BOOM!", "BANG!", "CLICK!", "POP!", "SNAP!"]
            for i in range(10):
                if not self.prank_running:
                    break
                sound = random.choice(sounds)
                self.root.after(0, lambda s=sound: self.prank_log.insert(tk.END, f"🔊 {s}\n"))
                time.sleep(1)

            self.finish_prank_operation("Звуковые эффекты завершены")

        threading.Thread(target=sound_prank, daemon=True).start()

    def change_wallpaper(self):
        try:
            self.start_prank_operation("Смена обоев")

            # Создаем простые обои программно
            colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
            color = random.choice(colors)

            # Создаем временное изображение для обоев
            from PIL import Image, ImageDraw

            img = Image.new('RGB', (1920, 1080), color=color)
            draw = ImageDraw.Draw(img)

            # Добавляем текст
            texts = ["PRANK!", "GOTCHA!", "HAHA!", "HELLO!", "SURPRISE!"]
            text = random.choice(texts)

            # Сохраняем и устанавливаем обои
            temp_path = os.path.join(os.getenv('TEMP'), 'prank_wallpaper.bmp')
            img.save(temp_path)

            ctypes.windll.user32.SystemParametersInfoW(20, 0, temp_path, 3)

            self.root.after(0, lambda: self.prank_log.insert(tk.END, f"🖼️  Обои изменены на: {text}\n"))
            self.finish_prank_operation("Смена обоев завершена")

        except Exception as e:
            self.root.after(0, lambda: self.prank_log.insert(tk.END, f"❌ Ошибка смены обоев: {e}\n"))
            self.finish_prank_operation("Ошибка смены обоев")

    def start_prank_operation(self, operation_name):
        self.prank_running = True
        self.stop_prank_btn.config(state=tk.NORMAL)
        self.prank_log.insert(tk.END, f"🚀 Запуск: {operation_name}\n")
        self.update_status(f"🎭 Выполняется: {operation_name}")

    def finish_prank_operation(self, message):
        self.prank_running = False
        self.stop_prank_btn.config(state=tk.DISABLED)
        self.prank_log.insert(tk.END, f"✅ {message}\n")
        self.update_status("🟢 Готов к работе")

    def stop_pranks(self):
        self.prank_running = False
        self.stop_prank_btn.config(state=tk.DISABLED)
        self.prank_log.insert(tk.END, "🛑 Все пранки остановлены пользователем\n")
        self.update_status("🛑 Пранки остановлены")


if __name__ == "__main__":
    root = tk.Tk()
    app = MultiToolApp(root)
    root.mainloop()
