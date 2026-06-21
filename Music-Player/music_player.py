import random
import os
import playsound
from typing import List, Union


def open_files_folder(folder: str) -> Union[List[str], bool]:
    try:
        if not os.path.exists(folder):
            return False

        all_files = os.listdir(folder)
        music_list = []

        for file in all_files:
            if file.lower().endswith(".mp3"):
                full_path = os.path.join(folder, file)
                if os.path.isfile(full_path):
                    music_list.append(full_path)

        return music_list if music_list else False
    except Exception:
        return False


def play_music(music: str) -> bool:
    try:
        if not os.path.exists(music):
            return False

        playsound.playsound(music)
        return True
    except Exception:
        return False


def random_play_music() -> None:
    try:
        music_lst = open_files_folder("data")
        if not music_lst:
            print("Нет доступных музыкальных файлов")
            return

        while music_lst:
            music_index = random.randint(0, len(music_lst) - 1)
            selected_music = music_lst.pop(music_index)
            print(f"Сейчас играет: {os.path.basename(selected_music)}")
            print(f"Оставшиеся песни: {len(music_lst)}")
            play_music(selected_music)
    except Exception:
        return


def default_play_music() -> None:
    try:
        music_lst = open_files_folder("data")
        if not music_lst:
            print("Нет доступных музыкальных файлов")
            return

        total_files = len(music_lst)

        for index, music_file in enumerate(music_lst, 1):
            print(f"Сейчас играет: {os.path.basename(music_file)}")
            print(f"Оставшиеся песни: {total_files - index}")
            play_music(music_file)
    except Exception:
        return


def main(text_input: str) -> None:
    try:
        while True:
            if text_input.lower() == "yes":
                random_play_music()
            else:
                default_play_music()
    except Exception:
        return


if __name__ == "__main__":
    user_input = input("Хотите включить рандомное воспроизведение: ")
    main(user_input)