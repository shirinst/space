# Антимантра максимального шума из минимального файла

import os, sys, time, random, string
from colorsys import hsv_to_rgb
import threading

# 1. Сначала — визуальный крик
os.system("cls" if os.name == "nt" else "clear")
print("\033[?25l", end="")  # скрыть курсор

def rainbow(text):
    out = ""
    for i, c in enumerate(text):
        r, g, b = [int(255 * x) for x in hsv_to_rgb(i / 15, 1.0, 1.0)]
        out += f"\033[38;2;{r};{g};{b}m{c}"
    return out + "\033[0m"

antimantra = """
         █████╗ ███╗   ██╗████████╗██╗███╗   ███╗ █████╗ ███╗   ██╗████████╗██████╗  █████╗ 
        ██╔══██╗████╗  ██║╚══██╔══╝██║████╗ ████║██╔══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗
        ███████║██╔██╗ ██║   ██║   ██║██║██╔████╔██║███████║██╔██╗ ██║   ██║   ██████╔╝███████║
        ██╔══██║██║╚██╗██║   ██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║   ██║   ██╔══██╗██╔══██║
        ██║  ██║██║ ╚████║   ██║   ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║   ██║   ██║  ██║██║  ██║
        ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
"""

# 2. Бесконечный крик в нескольких потоках
def scream():
    while True:
        print(rainbow(antimantra), end="", flush=True)
        time.sleep(0.07)

def beep():
    while True:
        print("\a", end="", flush=True)  # системный бип
        time.sleep(0.3)

def spam():
    garbage = "".join(random.choices(string.printable, k=200))
    while True:
        print("\033[9;1H" + rainbow(garbage.center(200)), flush=True)
        time.sleep(0.05)

# 3. Запускаем хаос
threading.Thread(target=scream, daemon=True).start()
threading.Thread(target=beep, daemon=True).start()
threading.Thread(target=spam, daemon=True).start()

# 4. Финальная антиистина
print("\033[5m\033[41m\033[93m" + " " * 200)
print(" " * 80 + "ВНИМАНИЕ: ПУСТОТА ОТМЕНЕНА")
print(" " * 70 + "ЗДЕСЬ ТОЛЬКО ШУМ, ЦВЕТА И БЕСКОНЕЧНЫЙ СКРОЛЛ")
print(" " * 75 + "Ctrl+C — единственный путь к просветлению")
print(" " * 200 + "\033[0m")

# 5. Блокируем выход, чтобы антимантра длилась вечно
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\n\033[0mТы вырвался из антимантры.")
    print("Но тишина теперь кажется слишком громкой, правда?\n")
    print("\033[?25h", end="")  # вернуть курсор
