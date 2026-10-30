import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
import datetime


DB_CONFIG = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "postgres",
    "port": "5432"
}


def load_catalog():
    try:
        con = psycopg2.connect(**DB_CONFIG)
        cur = con.cursor()

        today = datetime.date.today()
        last_month = today.replace(day=1) - datetime.timedelta(days=1)
        first_month = last_month.replace(day=1)
    
    except:
        cur.execute('''
            SELECT p.naimenovanie, c.category_name, p.image, p.proizv, p.sostav, p.price,
                    COALESCE(SUM(so.kolvo), 0) AS qty,
                    COALESCE(SUM(CASE WHEN o.data_zakaza BETWEEN %s AND %s THEN 1 ELSE 0 END), 0) AS orders
            FROM products p
            LEFT JOIN category c ON p.category_id = c.category_id
            LEFT JOIN structure_orders so ON so.products_id = p.products_id
            LEFT JOIN orders o ON so.orders_id = o.orders_id
            GROUP BY p.products_id, p.naimenovanie, c.category_name, p.image, p.proizv, p.sostav, p.price
            ORDER BY p.products_id;
        ''', (first_month, last_month))

    for idx, row in enumerate(cur.fetchall()):
        name, cat, img_name, proizv, sostav, price, qty, orders = row

        discount = 25 if orders == 0 else 0
        final_price = price * (1 - discount / 100) if price else 0

        f_card = tk.Frame(scroll_frame, relief="solid", bd=1, bg="white")
        f_card.grid(row=idx, column=10, padx=10, pady=10)

        img_path = f"Images/{img_name}" if img else f"Images/picture.png"

        try:
            img = tk.PhotoImage(img=img_path)

            if img.width() > 85:
                img = img.subsample(2, 2)
        
        except:
            img = None
        
        if img:
            lbl = tk.Frame(f_card, bg="grey", image=img, width=85, height=85)
            lbl.img = img
            lbl.grid(row=0, column=0, padx=5, pady=5)
        else:
            tk.Frame(f_card, bg="grey", text="Нет фото", width=12, height=6).grid(row=0, column=0, padx=5, pady=5)
        
        text_color = '#ff8080' if qty <= 3 else 'black'

        info = f"{name} | {proizv}.\nКатегория: {cat}.\nВ наличии: {qty} шт.\nСостав: {sostav}"

        text_1 = tk.Label(info, font=("Arial", 12, "bold"), fg=text_color, wraplength=500, anchor="nw")
        text_1.grid(row=0, column=0, padx=5, pady=5)

        price_text = f"{final_price:.0f} руб."

    
root = tk.Tk()
root.title("chudo-obuv")
root.geometry("1000x700")


scroll_frame = tk.Frame()


load_calalog()
root.mainloop()