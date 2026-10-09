#1
name = input("Как вас зовут")

profession = input("кем вы работаете или учитесь?")

city = input("из какого вы города?")

hobbi = input("какой у вас хобби?")

  
  

print("\n ---моя визитка---")

print(f"имя:{name}")

print(f"...")

print(f"...")

print("...")

print(f"...")

  

#2

odsh_summ = int(input("Общая сумма счета"))

cha = int(input("какой процент чаевых они хотят оставитьь"))

chel = int(input("нас колько человек нужно разделить счет"))

  

sum = (odsh_summ * cha) /100

it_sum = (odsh_summ + cha)

skoka = (it_sum / chel)

  

print(f"Сумма самих чаевых:{sum}")

print(f"итоговая сумма к оплатае:{it_sum}")

print(f"сколько человек должен каждый:{skoka}")


#3
sp = input("введите пароль")

v = int(input("возраст"))

  

if sp == 'python':

    if v <= 18:

        print("добро пожаловать в клуб")

    elif sp == 'python' and v > 18:

        print("пароль верный но вам рано еще в клуб")

else:

    print("доступ запрещен парроль не верный")



#4
import random

  

conteiner = 'abcdifghielomoldjil123456789'

letter = random.choice(conteiner)

letter2 = random.choice(conteiner)

letter3 = random.choice(conteiner)

letter4 = random.choice(conteiner)

letter5 = random.choice(conteiner)

print(letter + letter2 + letter3 + letter4 + letter5)



#5
shopping_list = []

a = input("введите:")

b = input("введите:")

c = input("введите:")

  

shopping_list.append(a)

shopping_list.append(b)

shopping_list.append(c)

  

d = input("не предумал ли на счет продукта?:")

  

if d == 'да':

    f = input('введит то что хотете удалить')

    shopping_list.remove(f)

print(shopping_list)

#7
phone_book = {

    "Алиса": "89005674321",

    "Алина": "89255674321",

    "Анна": "89345674321"

}

  

a = input("чей номер?")

  

if a  in phone_book:

    print(f"номер: {phone_book[a]}")

else:

    print("номер не найден")
    
    
    
#10 
import tkinter as tk

  
  

window = tk.Tk()

window.title("моя визитка")

window.geometry("350x250")

  

label = tk.Label(window, text="Жасмина", font=("Bold", 20))

label.pack(pady=20)

label = tk.Label(window, text="Студент", font=("Bold", 20))

label.pack(pady=20)

label = tk.Label(window, text="Москва", font=("Bold", 20))

label.pack(pady=20)

  

window.mainloop()

#11
import tkinter as tk

  

count = 0

  

def click():

    global count

    count += 1

    label.config(text = count)

  

def reset():

    global count

    count = 0

    label.config(text = count)

  
  

window = tk.Tk()

window.title("Счетчик кликов")

window.geometry("300x250")

  
  

label = tk.Label(window, text=count, font=("Arial", 12))

label.pack(pady=20)

  

button = tk.Button(

    window,

    text="Клик",

    command=click,

    font=("Arial", 12)

)

button.pack()

  

button = tk.Button(

    window,

    text="Сброс",

    command=reset,

    font=("Arial", 12)

)

button.pack()

  

window.mainloop()

#12
import tkinter as tk



window = tk.Tk()
window.title("Калькулятор")
window.geometry("300x250")

frame = tk.Frame(window)
frame.pack(pady=20, padx=20)


tk.Label(frame, text="Поле ввода 1 числа:")


button = tk.Button(
    window,
    text="Сложить",
    command=click,
    font=("Arial", 12)
)
button.pack()


window.mainloop()
