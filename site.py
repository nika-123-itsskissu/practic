#13
import tkinter as tk
from tkinter import ttk

window = tk.Tk() # создаем главное окно приложения
window.title("Мой сайт") # заголовок окна
window.geometry("1500x1000") # размер окна

# шапка
header = tk.Frame(window, bg="#2c3e50", height=60) # Tk.Frame - контейнер, внутри которого размещаются элементы
# bg - цвет, height - высота
header.pack(fill="x") # растянуть по горизонтали на всю ширину окна

tk.Label(header, text="Мой Сайт", bg="#2c3e50", fg="white",
         font=("Arial", 18, "bold")).pack(side="left", padx=20)
# tk.Label - текстовая надпись, header - родитель, то есть метка лежит внутри шапки
# bg - фон, fg - цвет текста, .pack(side="left", padx=20) - прижать к левому краю шапки, отступ 20п


tk.Button(header, text="Войти", bg="#3498db", fg="white").pack(side="right", padx=20, pady=15)
# tk.Button - кнопка, bg - фон, fg - цвет текста


# основной контент
main = tk.Frame(window, bg="#ecf0f1")
main.pack(fill="both")
# bg - фон, fill="both" растянуть по горизонтали и вертикали

tk.Label(main, text="Каталог товаров", bg="#56c1dc",
         font=("Arial", 24)).pack(pady=40)

# Создаем карточки товаров
cards_area = tk.Frame(window, bg="#ecf0f1")
cards_area.pack(fill="both", expand=True, padx=40, pady=40)
# размести этот контейнер в окне и растяни его, при этом мы ставим padx=40, pady=40, чтобы карточки не прилипли по бокам фрейма

card = tk.Frame(cards_area, bg="white", width=300, height=420,
                highlightbackground="#bdc3c7", highlightthickness=1)
card.pack(side="left", padx=15)       # прижать влево, отступ между карточками
# highlightbackground="#bdc3c7" - цвет рамки, highlightthickness=1 - толщина обводки рамки

# 1. «Картинка» — цветной блок
image_block = tk.Frame(card, bg="#3498db", height=180)
image_block.pack(fill="x")
image_block.pack_propagate(False)   # фиксируем высоту 180

tk.Label(image_block, text="Фото", bg="#3498db", fg="white",
         font=("Arial", 14, "bold")).pack(expand=True)
# pack(expand=True) - занимает все пустое место внутри родителя
# 2. Название
tk.Label(card, text="Кружка «Кот-программист»", bg="white",
         fg="#2c3e50", font=("Arial", 13, "bold"),
         wraplength=260, justify="left").pack(anchor="w", padx=15, pady=(12, 4))

# 3. Описание
tk.Label(card, text="Керамика 350 мл. Держит тепло до 40 минут, не выцветает.",
         bg="white", fg="#7f8c8d", font=("Arial", 10),
         wraplength=260, justify="left").pack(anchor="w", padx=15)

# 4. Цена
tk.Label(card, text="890 ₽", bg="white", fg="#e74c3c",
         font=("Arial", 16, "bold")).pack(anchor="w", padx=15, pady=(10, 0))

# подвал
footer = tk.Frame(window, bg="#34495e", height=40)
footer.pack(fill="x", side="bottom")
# side="bottom" - прижать к низу окна

tk.Label(footer, text="Сайт", bg="#34495e",
         fg="white", font=("Arial", 9)).pack(pady=10)

window.mainloop()