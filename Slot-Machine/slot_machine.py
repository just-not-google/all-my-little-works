import tkinter as tk
from tkinter import messagebox, ttk
import random
import time
import math
import os


class AnimatedSlot:
    def __init__(self, parent, font=("Arial", 60), width=3, height=1):
        self.parent = parent
        self.font = font
        self.label = tk.Label(parent, text="★", font=font, width=width, height=height,
                              bg="black", fg="white", relief="raised", bd=3)
        self.is_spinning = False
        self.spin_duration = 0
        self.start_time = 0

    def grid(self, **kwargs):
        self.label.grid(**kwargs)

    def spin(self, duration=2.0, final_symbol=None):
        self.is_spinning = True
        self.spin_duration = duration
        self.start_time = time.time()
        self.final_symbol = final_symbol
        self.animate_spin()

    def animate_spin(self):
        if not self.is_spinning:
            return

        elapsed = time.time() - self.start_time
        progress = min(elapsed / self.spin_duration, 1.0)

        # Ускоряемся в начале и замедляемся в конце
        ease_progress = self.ease_out_cubic(progress)

        # Меняем символ во время вращения
        symbols = ["♦", "♠", "♣", "♥", "★", "♫", "♻", "⚑", "⚡", "♖", "♔", "♕"]
        if progress < 1.0:
            # Быстрая смена символов во время вращения
            symbol_index = int(time.time() * 20) % len(symbols)
            self.label.config(text=symbols[symbol_index])
            delay = max(10, int(50 * (1 - ease_progress)))  # Замедляемся к концу
            self.label.after(delay, self.animate_spin)
        else:
            # Устанавливаем финальный символ
            self.is_spinning = False
            if self.final_symbol:
                self.label.config(text=self.final_symbol)

    def ease_out_cubic(self, x):
        return 1 - pow(1 - x, 3)


class CasinoGame:
    def __init__(self):
        self.money = 1000000
        self.bet_amount = 100
        self.total_spins = 0
        self.wins = 0
        self.losses = 0
        self.player_name = "Player"
        self.theme_index = 0
        self.themes = [
            {"bg": "#1a1a2e", "fg": "white", "accent": "#16213e", "slot_bg": "#0f3460", "button_bg": "#e94560"},
            {"bg": "#1b4332", "fg": "white", "accent": "#2d6a4f", "slot_bg": "#40916c", "button_bg": "#f48c06"},
            {"bg": "#3d348b", "fg": "white", "accent": "#7678ed", "slot_bg": "#f7b801", "button_bg": "#f18701"},
            {"bg": "#22223b", "fg": "white", "accent": "#4a4e69", "slot_bg": "#9a8c98", "button_bg": "#c9ada7"}
        ]

        # Символы с разной редкостью
        self.symbols = [
            {"symbol": "♦", "name": "Diamond", "multiplier": 3, "rarity": 1.0},
            {"symbol": "♠", "name": "Spade", "multiplier": 3, "rarity": 1.0},
            {"symbol": "♣", "name": "Club", "multiplier": 3, "rarity": 1.0},
            {"symbol": "♥", "name": "Heart", "multiplier": 3, "rarity": 1.0},
            {"symbol": "★", "name": "Star", "multiplier": 5, "rarity": 0.7},
            {"symbol": "♫", "name": "Music", "multiplier": 5, "rarity": 0.7},
            {"symbol": "♻", "name": "Recycle", "multiplier": 5, "rarity": 0.7},
            {"symbol": "⚑", "name": "Flag", "multiplier": 8, "rarity": 0.5},
            {"symbol": "⚡", "name": "Zap", "multiplier": 10, "rarity": 0.3},
            {"symbol": "♖", "name": "Rook", "multiplier": 15, "rarity": 0.2},
            {"symbol": "♔", "name": "King", "multiplier": 20, "rarity": 0.1},
            {"symbol": "♕", "name": "Queen", "multiplier": 25, "rarity": 0.05}
        ]

        self.root = None
        self.slots = []
        self.win_label = None
        self.money_label = None
        self.stats_label = None
        self.spin_button = None
        self.bet_scale = None
        self.jackpot_amount = 10000
        self.jackpot_label = None
        self.progress_bar = None
        self.history_text = None
        self.volume_var = None
        self.animation_speed = 1.0
        self.bet_label = None

    def get_weighted_symbol(self):
        weights = [symbol["rarity"] for symbol in self.symbols]
        return random.choices(self.symbols, weights=weights)[0]

    def calculate_win(self, slot_results):
        symbols = [result["symbol"] for result in slot_results]
        win_amount = 0
        win_type = "No Win"

        # Проверяем комбинации
        if symbols[0] == symbols[1] == symbols[2]:
            # Джекпот - три редких символа
            if slot_results[0]["multiplier"] >= 15:
                win_amount = self.jackpot_amount
                self.jackpot_amount = 10000  # Сбрасываем джекпот
                win_type = "JACKPOT!"
            else:
                win_amount = self.bet_amount * slot_results[0]["multiplier"]
                win_type = "Three of a Kind!"
        elif symbols[0] == symbols[1] or symbols[1] == symbols[2] or symbols[0] == symbols[2]:
            win_amount = self.bet_amount * 2
            win_type = "Two of a Kind!"

        # Увеличиваем джекпот с каждой игрой
        self.jackpot_amount += int(self.bet_amount * 0.1)

        return win_amount, win_type

    def spin_slots(self):
        if self.money < self.bet_amount:
            messagebox.showerror("Insufficient Funds", "You don't have enough money to place this bet!")
            return

        if any(slot.is_spinning for slot in self.slots):
            return

        self.money -= self.bet_amount
        self.total_spins += 1
        self.update_display()

        # Генерируем результаты
        results = [self.get_weighted_symbol() for _ in range(3)]

        # Запускаем анимацию слотов
        spin_duration = 1.5 / self.animation_speed
        for i, slot in enumerate(self.slots):
            delay = i * 300  # Задержка между запуском каждого слота
            self.root.after(delay,
                            lambda s=slot, d=spin_duration, f=results[i]["symbol"]: s.spin(duration=d, final_symbol=f))

        # После завершения анимации вычисляем выигрыш
        self.root.after(int((spin_duration + 0.5) * 1000), lambda: self.finish_spin(results))

    def finish_spin(self, results):
        win_amount, win_type = self.calculate_win(results)

        if win_amount > 0:
            self.money += win_amount
            self.wins += 1
            self.win_label.config(text=f"{win_type} You won ${win_amount}!",
                                  fg="#4CAF50", font=("Arial", 16, "bold"))

            # Добавляем в историю
            self.history_text.insert(tk.END, f"Spin {self.total_spins}: WON ${win_amount} ({win_type})\n")

            # Специальные эффекты для больших выигрышей
            if win_type == "JACKPOT!":
                self.celebrate_win()
        else:
            self.losses += 1
            self.win_label.config(text="No win this time. Try again!",
                                  fg="#F44336", font=("Arial", 14))
            self.history_text.insert(tk.END, f"Spin {self.total_spins}: Lost ${self.bet_amount}\n")

        self.history_text.see(tk.END)
        self.update_display()

        # Проверяем условие окончания игры
        if self.money <= 0:
            self.end_game()

    def celebrate_win(self):
        # Создаем эффект празднования для джекпота
        celebration_window = tk.Toplevel(self.root)
        celebration_window.title("JACKPOT!")
        celebration_window.geometry("400x300")
        celebration_window.configure(bg="gold")
        celebration_window.attributes("-topmost", True)

        tk.Label(celebration_window, text="🎉 JACKPOT! 🎉",
                 font=("Arial", 24, "bold"), bg="gold", fg="red").pack(expand=True)
        tk.Label(celebration_window, text=f"You won ${self.jackpot_amount}!",
                 font=("Arial", 18), bg="gold").pack()

        # Автоматически закрываем окно через 3 секунды
        celebration_window.after(3000, celebration_window.destroy)

    def update_display(self):
        self.money_label.config(text=f"Money: ${self.money:,}")
        self.stats_label.config(text=f"Spins: {self.total_spins} | Wins: {self.wins} | Losses: {self.losses}")
        self.jackpot_label.config(text=f"Jackpot: ${self.jackpot_amount:,}")

        # Обновляем прогресс
        win_rate = (self.wins / self.total_spins * 100) if self.total_spins > 0 else 0
        self.progress_bar["value"] = win_rate

    def change_bet(self, value):
        self.bet_amount = int(float(value))
        self.update_bet_display()

    def update_bet_display(self):
        if self.bet_label:
            self.bet_label.config(text=f"Current Bet: ${self.bet_amount}")

    def change_theme(self):
        self.theme_index = (self.theme_index + 1) % len(self.themes)
        self.apply_theme()

    def apply_theme(self):
        # Применяем тему только после создания всех виджетов
        if not hasattr(self, 'theme_applied'):
            return

        theme = self.themes[self.theme_index]
        self.root.configure(bg=theme["bg"])

        # Обновляем цвета всех виджетов
        widgets = [self.win_label, self.money_label, self.stats_label, self.jackpot_label]
        for widget in widgets:
            if widget:  # Проверяем, что виджет существует
                widget.config(bg=theme["bg"], fg=theme["fg"])

        if self.spin_button:
            self.spin_button.config(bg=theme["button_bg"], fg="white")
        if self.bet_scale:
            self.bet_scale.config(bg=theme["accent"])
        if self.bet_label:
            self.bet_label.config(bg=theme["bg"], fg=theme["fg"])

    def change_animation_speed(self, value):
        self.animation_speed = float(value)

    def save_game(self):
        try:
            with open("casino_save.txt", "w") as f:
                f.write(f"{self.money}\n{self.total_spins}\n{self.wins}\n{self.losses}\n{self.jackpot_amount}")
            messagebox.showinfo("Game Saved", "Your game progress has been saved!")
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save game: {e}")

    def load_game(self):
        try:
            if os.path.exists("casino_save.txt"):
                with open("casino_save.txt", "r") as f:
                    lines = f.readlines()
                    self.money = int(lines[0].strip())
                    self.total_spins = int(lines[1].strip())
                    self.wins = int(lines[2].strip())
                    self.losses = int(lines[3].strip())
                    self.jackpot_amount = int(lines[4].strip())
                self.update_display()
                messagebox.showinfo("Game Loaded", "Your game progress has been loaded!")
        except Exception as e:
            messagebox.showerror("Load Error", f"Could not load game: {e}")

    def end_game(self):
        if self.spin_button:
            self.spin_button.config(state=tk.DISABLED)
        messagebox.showinfo("Game Over",
                            f"Game Over!\n\n"
                            f"Final Stats:\n"
                            f"Total Spins: {self.total_spins}\n"
                            f"Wins: {self.wins}\n"
                            f"Losses: {self.losses}\n"
                            f"Win Rate: {(self.wins / self.total_spins * 100):.1f}%")

    def show_help(self):
        help_text = """
        TRIPLE THREAT CASINO - HELP

        HOW TO PLAY:
        - Set your bet amount using the slider
        - Click SPIN to spin the slots
        - Match symbols to win!

        WINNING COMBINATIONS:
        - Three of a Kind: Bet × Symbol Multiplier
        - Two of a Kind: Bet × 2
        - JACKPOT: Three rare symbols!

        SYMBOLS:
        Common (♦♠♣♥): ×3 Multiplier
        Uncommon (★♫♻): ×5 Multiplier  
        Rare (⚑): ×8 Multiplier
        Very Rare (⚡): ×10 Multiplier
        Epic (♖): ×15 Multiplier
        Legendary (♔♕): ×20-25 Multiplier

        TIPS:
        - Higher bets = Higher potential wins
        - Watch the jackpot grow!
        - Save your progress regularly
        """
        messagebox.showinfo("Game Help", help_text)

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Triple Threat Casino - Ultimate Edition")
        self.root.geometry("900x800")
        self.root.resizable(True, True)

        # Сначала создаем все виджеты
        self.create_widgets()

        # Затем применяем тему
        self.theme_applied = True
        self.apply_theme()

        self.update_display()

    def create_widgets(self):
        # Заголовок
        title_frame = tk.Frame(self.root, bg=self.themes[self.theme_index]["accent"])
        title_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(title_frame, text="🎰 TRIPLE THREAT CASINO 🎰",
                 font=("Arial", 24, "bold"),
                 bg=self.themes[self.theme_index]["accent"],
                 fg="white").pack(pady=10)

        # Информационная панель
        info_frame = tk.Frame(self.root, bg=self.themes[self.theme_index]["bg"])
        info_frame.pack(fill=tk.X, padx=20, pady=10)

        self.money_label = tk.Label(info_frame, text=f"Money: ${self.money:,}",
                                    font=("Arial", 16, "bold"),
                                    bg=self.themes[self.theme_index]["bg"],
                                    fg="white")
        self.money_label.pack(side=tk.LEFT, padx=10)

        self.jackpot_label = tk.Label(info_frame, text=f"Jackpot: ${self.jackpot_amount:,}",
                                      font=("Arial", 16, "bold"),
                                      bg=self.themes[self.theme_index]["bg"],
                                      fg="gold")
        self.jackpot_label.pack(side=tk.RIGHT, padx=10)

        # Статистика
        self.stats_label = tk.Label(self.root,
                                    text=f"Spins: {self.total_spins} | Wins: {self.wins} | Losses: {self.losses}",
                                    font=("Arial", 12),
                                    bg=self.themes[self.theme_index]["bg"],
                                    fg="white")
        self.stats_label.pack(pady=5)

        # Прогресс-бар win rate
        progress_frame = tk.Frame(self.root, bg=self.themes[self.theme_index]["bg"])
        progress_frame.pack(fill=tk.X, padx=20, pady=5)

        tk.Label(progress_frame, text="Win Rate:",
                 font=("Arial", 10),
                 bg=self.themes[self.theme_index]["bg"],
                 fg="white").pack(side=tk.LEFT)

        self.progress_bar = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL,
                                            length=200, mode='determinate')
        self.progress_bar.pack(side=tk.LEFT, padx=5)

        # Слоты
        slots_frame = tk.Frame(self.root, bg="black", relief="raised", bd=5)
        slots_frame.pack(pady=20)

        # Создаем анимированные слоты
        self.slots = []
        for i in range(3):
            slot = AnimatedSlot(slots_frame, font=("Arial", 70), width=3, height=1)
            slot.grid(row=0, column=i, padx=15, pady=15)
            self.slots.append(slot)

        # Метка выигрыша
        self.win_label = tk.Label(self.root, text="Place your bet and spin!",
                                  font=("Arial", 14),
                                  bg=self.themes[self.theme_index]["bg"],
                                  fg="white")
        self.win_label.pack(pady=10)

        # Панель управления
        control_frame = tk.Frame(self.root, bg=self.themes[self.theme_index]["bg"])
        control_frame.pack(pady=20)

        # Регулировка ставки
        bet_frame = tk.Frame(control_frame, bg=self.themes[self.theme_index]["bg"])
        bet_frame.pack(pady=10)

        tk.Label(bet_frame, text="Bet Amount:",
                 font=("Arial", 12),
                 bg=self.themes[self.theme_index]["bg"],
                 fg="white").pack()

        self.bet_scale = tk.Scale(bet_frame, from_=10, to=1000, orient=tk.HORIZONTAL,
                                  length=300, resolution=10,
                                  bg=self.themes[self.theme_index]["accent"],
                                  fg="white", highlightbackground=self.themes[self.theme_index]["bg"],
                                  command=self.change_bet)
        self.bet_scale.set(self.bet_amount)
        self.bet_scale.pack(pady=5)

        self.bet_label = tk.Label(bet_frame, text=f"Current Bet: ${self.bet_amount}",
                                  font=("Arial", 11),
                                  bg=self.themes[self.theme_index]["bg"],
                                  fg="white")
        self.bet_label.pack()

        # Кнопка вращения
        self.spin_button = tk.Button(control_frame, text="🎰 SPIN 🎰",
                                     font=("Arial", 18, "bold"),
                                     bg=self.themes[self.theme_index]["button_bg"],
                                     fg="white",
                                     command=self.spin_slots,
                                     width=15, height=2)
        self.spin_button.pack(pady=10)

        # Дополнительные настройки
        settings_frame = tk.Frame(control_frame, bg=self.themes[self.theme_index]["bg"])
        settings_frame.pack(pady=10)

        # Скорость анимации
        tk.Label(settings_frame, text="Animation Speed:",
                 font=("Arial", 10),
                 bg=self.themes[self.theme_index]["bg"],
                 fg="white").grid(row=0, column=0, padx=5)

        speed_scale = tk.Scale(settings_frame, from_=0.5, to=3.0, orient=tk.HORIZONTAL,
                               length=150, resolution=0.1,
                               bg=self.themes[self.theme_index]["accent"],
                               fg="white", highlightbackground=self.themes[self.theme_index]["bg"],
                               command=self.change_animation_speed)
        speed_scale.set(self.animation_speed)
        speed_scale.grid(row=0, column=1, padx=5)

        # Кнопки управления
        button_frame = tk.Frame(control_frame, bg=self.themes[self.theme_index]["bg"])
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Change Theme",
                  command=self.change_theme,
                  bg=self.themes[self.theme_index]["accent"],
                  fg="white").grid(row=0, column=0, padx=5)

        tk.Button(button_frame, text="Save Game",
                  command=self.save_game,
                  bg=self.themes[self.theme_index]["accent"],
                  fg="white").grid(row=0, column=1, padx=5)

        tk.Button(button_frame, text="Load Game",
                  command=self.load_game,
                  bg=self.themes[self.theme_index]["accent"],
                  fg="white").grid(row=0, column=2, padx=5)

        tk.Button(button_frame, text="Help",
                  command=self.show_help,
                  bg=self.themes[self.theme_index]["accent"],
                  fg="white").grid(row=0, column=3, padx=5)

        # История игр
        history_frame = tk.Frame(self.root, bg=self.themes[self.theme_index]["bg"])
        history_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        tk.Label(history_frame, text="Game History:",
                 font=("Arial", 12, "bold"),
                 bg=self.themes[self.theme_index]["bg"],
                 fg="white").pack(anchor=tk.W)

        self.history_text = tk.Text(history_frame, height=8, width=80,
                                    bg="#2c2c2c", fg="white",
                                    font=("Arial", 9))
        scrollbar = tk.Scrollbar(history_frame, command=self.history_text.yview)
        self.history_text.config(yscrollcommand=scrollbar.set)

        self.history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Статус бар
        status_bar = tk.Label(self.root, text="Ready to play! Place your bet and spin the slots!",
                              relief=tk.SUNKEN, anchor=tk.W,
                              bg=self.themes[self.theme_index]["accent"],
                              fg="white")
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def run(self):
        self.create_gui()
        self.root.mainloop()


if __name__ == "__main__":
    # Создаем экземпляр игры и запускаем
    casino_game = CasinoGame()
    casino_game.run()
