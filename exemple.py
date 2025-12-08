# 1. Импортируем абсолютную пустоту (0 байт)
import space

# 2. Наполняем пустоту смыслом прямо в рантайме
space.author          = "shirinst"
space.purpose         = "Доказать, что всё начинается с нуля"
space.year            = 2025
space.meaning         = 42
space.create_universe = lambda: "Вселенная успешно развёрнута из 0 байт"
space.zen             = """
    Пустота — не отсутствие.
    Пустота — бесконечная возможность.
"""

# 3. Сохраняем наполненную пустоту как новый, живой модуль
import marshal

with open("universe.py", "wb") as f:
    # Сохраняем скомпилированный код модуля (пустой) + все атрибуты
    marshal.dump(space.__dict__, f)

print("Вселенная сохранена в universe.py")
