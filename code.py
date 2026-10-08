import tkinter as tk

# Импортируем ttk(улучшенные компоненты, например таблицы)
# и messegebox(для вслывабщих окон с ошибками)
from tkinter import ttk, messagebox

# Импортируем библиотеку для работы с бд
import psycopg2

# Настройки подключения к бд
DB_HOST = "localhost"
DB_NAME = "database_1"
DB_USER = "postgres"
DB_PASS = "236945"
DB_PORT = "5432"

# Объявляем функцию, котаря будет забирать данные из бд и отобрать их в таблице интерфейса
def fetch_users():
    try:
        # Открываем соединение с бд, используя ранее заданные константы
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )

        # Создаем курсор - это инструмент для выполнения запросов и получения результатов
        cur = conn.cursor()

        # Делаем запрос. Используется LEFT JOIN для объединения таблицы пользователей
        # и ролей, чтобы вместо числового role_id вывести понятное название роли(role_name)
        cur.execute("""
            SELECT u.users_id, u.users_name, u.familia, u.otchestvo, u.login, r.rols_name
            FROM users u
            LEFT JOIN rols r ON u.rols_id = r.rols_id;
        """)

        # Извлекаем все строки, которые вернул запрос, в переменную rows (список кортежей)
        rows = cur.fetchall()

        # Очищаем таблицу в интерфейсе перед выводом новых данных, чтобы строки не дублировались при обновлении
        for item in tree.get_children():
            tree.delete(item)

        # Циклом обходим каждую строку из бд и добавляем её в конец таблицы TreeView
        for row in rows:
            tree.insert('', 'end', values=row)


        # Закрываем курсор и соединение с БД, чтобы освободить ресурсы сервера
        cur.close()
        conn.close()

    # Если на каком-то этапе произошла ошибка, выводим всплывающее окно с её текстом 
    except Exception as e:
        messagebox.showerror("Ошибка БД", str(e))

    # Интерфейс

    # Создаем главное окно приложения
window = tk.Tk()

window.title("Пользователи")
window.geometry("800x400")

# Создаем текстовую надпись-заголовок внутри окна, задаем крупный шрифт и размещаем с отступом сверху/снизу 10px
tk.Label(window, text="Список пользователей", font=("Arial", 14, "bold")).pack(pady=10)

# Определяем внутренние id колонок для таблицы Treeview
columns = ("users_id", "users_name", "familia", "otchestvo", "login", "rols_id")

# Создаем саму таблицу TreeView привязываем колонки. show="headings" - прячет пустой начальный столбец-дерево
tree = ttk.Treeview(window, columns=columns, show="headings")

# Задаем видимые заголовки для каждой колонки таблицы, которые увидят пользователь
tree.heading("users_id", text="ID")
tree.heading("users_name", text="Имя")
tree.heading("familia", text="Фамилия")
tree.heading("otchestvo", text="Отчество")
tree.heading("login", text="Логин")
tree.heading("rols_id", text="Роль")

# Настраиваем ширину колонок и выравнивание текста (например, ID ставим по центру, для остальных - по умолчанию влево)
tree.column("users_id", width=60, anchor="center")
tree.column("users_name", width=120)
tree.column("familia", width=120)
tree.column("otchestvo", width=120)
tree.column("login", width=130)
tree.column("rols_id", width=130)

# Размещаем таблицу в окне. fill="both" и expand=True заставляют её растягиваться при изменении размеров окна
tree.pack(fill="both", expand=True, padx=10, pady=5)

# Создаем кнопку обновить. Параметр command=fetch_users, связывает её с функцией загрузки данных из БД
tk.Button(window, text="Обновить", command=fetch_users, font=("Arial", 14)).pack(pady=5)

# Первичный вызов функции, чтобы таблица заполнилась данными сразу при запуске программы, а не только по кнопке
fetch_users()

# Запускаем бесконечный главный цикл Tkinter, который удерживает окно открытым и обрабатывает клики/события
window.mainloop()