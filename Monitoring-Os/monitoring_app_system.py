import tkinter as tk
from tkinter import scrolledtext, ttk
import platform
import GPUtil
import cpuinfo
import wmi
import threading
import psutil


def get_system_info():
    result = ""

    result += "=== СИСТЕМА ===\n"
    result += f"Операционная система: {platform.system()} {platform.release()} ({platform.version()})\n"
    result += f"Рабочая станция: {platform.node()} ({platform.machine()})\n"
    result += f"Архитектура: {platform.architecture()[0]}\n"
    result += f"Версия Python: {platform.python_version()}\n\n"

    try:
        info = cpuinfo.get_cpu_info()
        result += "=== ПРОЦЕССОР ===\n"
        result += f"Производитель: {info.get('vendor_id_raw', 'Неизвестно')}\n"
        result += f"Модель: {info.get('brand_raw', 'Неизвестно')}\n"
        result += f"Текущая частота: {info.get('hz_actual', ['Неизвестно'])[0]}\n"
        result += f"Заявленная частота: {info.get('hz_advertised', ['Неизвестно'])[0]}\n"
        result += f"Физические ядра: {psutil.cpu_count(logical=False)}\n"
        result += f"Логические ядра: {info.get('count', 'Неизвестно')}\n"
        result += f"Загрузка CPU: {psutil.cpu_percent()}%\n\n"
    except Exception as e:
        result += f"Ошибка получения информации о процессоре: {e}\n\n"

    try:
        mem = psutil.virtual_memory()
        result += "=== ОПЕРАТИВНАЯ ПАМЯТЬ ===\n"
        result += f"Всего: {round(mem.total / (1024 ** 3), 1)} GB\n"
        result += f"Доступно: {round(mem.available / (1024 ** 3), 1)} GB\n"
        result += f"Использовано: {round(mem.used / (1024 ** 3), 1)} GB\n"
        result += f"Загрузка RAM: {mem.percent}%\n\n"
    except Exception as e:
        result += f"Ошибка получения информации о памяти: {e}\n\n"

    try:
        gpus = GPUtil.getGPUs()
        result += "=== ВИДЕОКАРТА ===\n"
        for i, gpu in enumerate(gpus, 1):
            used_memory_mb = gpu.memoryTotal - gpu.memoryFree
            free_memory_gb = round(gpu.memoryFree / 1024, 1)
            used_memory_gb = round(used_memory_mb / 1024, 1)
            total_memory_gb = round(gpu.memoryTotal / 1024, 1)
            fahrenheit_temperature = round((gpu.temperature * 1.8) + 32)

            if i > 1:
                result += "─" * 50 + "\n"

            result += (f"Видеокарта #{i}: {gpu.name}\n"
                       f"Загрузка: {gpu.load * 100:.1f}%\n"
                       f"Общая память: {total_memory_gb} GB\n"
                       f"Свободно: {free_memory_gb} GB\n"
                       f"Использовано: {used_memory_gb} GB\n"
                       f"Температура: {gpu.temperature}°C ({fahrenheit_temperature}°F)\n")
        result += "\n"
    except Exception as e:
        result += f"Ошибка получения информации о видеокарте: {e}\n\n"

    try:
        c = wmi.WMI()
        result += "=== НАКОПИТЕЛИ ===\n"
        for i, disk in enumerate(c.Win32_DiskDrive(), 1):
            disk_size_gb = round(int(disk.Size) / 1073741824, 1)

            if i > 1:
                result += "─" * 50 + "\n"

            result += (f"Диск #{i}: {disk.Model.strip()}\n"
                       f"Размер: {disk_size_gb} GB\n"
                       f"Интерфейс: {disk.InterfaceType}\n"
                       f"Тип носителя: {disk.MediaType}\n")
        result += "\n"
    except Exception as e:
        result += f"Ошибка получения информации о дисках: {e}\n\n"

    return result


def update_info():
    loading_label.config(text="🔄 Загрузка данных...", fg="blue")
    text_area.delete(1.0, tk.END)
    root.update()

    def get_info_thread():
        info = get_system_info()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, info)
        loading_label.config(text="✅ Данные успешно загружены", fg="green")

    threading.Thread(target=get_info_thread, daemon=True).start()


def show_section(section):
    info = get_system_info()
    lines = info.split('\n')
    result = ""
    in_section = False

    for line in lines:
        if line.startswith(f"=== {section.upper()} ==="):
            in_section = True
            result += line + "\n"
        elif line.startswith("===") and in_section:
            break
        elif in_section:
            result += line + "\n"

    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, result or f"Раздел '{section}' не найден")


root = tk.Tk()
root.title("Системный монитор")
root.geometry("1000x700")
root.resizable(False, False)
root.configure(bg="#2c3e50")

style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=10)
style.configure('Section.TButton', font=('Arial', 11), padding=5)

main_frame = tk.Frame(root, bg="#2c3e50")
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

title_label = tk.Label(main_frame, text="🔍 СИСТЕМНЫЙ МОНИТОР",
                       font=("Arial", 20, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=(0, 15))

section_frame = tk.Frame(main_frame, bg="#2c3e50")
section_frame.pack(fill=tk.X, pady=(0, 10))

sections = ["СИСТЕМА", "ПРОЦЕССОР", "ОПЕРАТИВНАЯ ПАМЯТЬ", "ВИДЕОКАРТА", "НАКОПИТЕЛИ", "ВСЕ"]

for i, section in enumerate(sections):
    btn = ttk.Button(section_frame, text=section, command=lambda s=section: show_section(s) if s != "ВСЕ" else update_info(), style='Section.TButton')
    btn.pack(side=tk.LEFT, padx=2)

control_frame = tk.Frame(main_frame, bg="#2c3e50")
control_frame.pack(fill=tk.X, pady=10)

update_button = ttk.Button(control_frame, text="ОБНОВИТЬ ВСЕ", command=update_info)
update_button.pack(side=tk.LEFT, padx=5)

loading_label = tk.Label(control_frame, text="Нажмите 'ОБНОВИТЬ ВСЕ' для загрузки данных", font=("Arial", 12), bg="#2c3e50", fg="#ecf0f1")
loading_label.pack(side=tk.LEFT, padx=20)

exit_button = ttk.Button(control_frame, text="ВЫХОД", command=root.quit)
exit_button.pack(side=tk.RIGHT, padx=5)

text_frame = tk.Frame(main_frame, bg="#34495e")
text_frame.pack(fill=tk.BOTH, expand=True)

text_area = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, width=100, height=30, font=("Consolas", 12), bg="#ecf0f1", fg="#2c3e50", relief=tk.FLAT, bd=2)
text_area.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)

status_bar = tk.Label(root, text="Готов к работе", relief=tk.SUNKEN, anchor=tk.W, font=("Arial", 10), bg="#34495e", fg="white")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()