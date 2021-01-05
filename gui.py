import tkinter as tk
from tkinter import *
import os
import data_manipulation as dm
import expense as exp
from subscription import subscription as sub
import calendar


root = tk.Tk()
root.title("Subs App")
canvas = tk.Canvas(root, height = 700, width =700, bg = "#FFFFF7" )
canvas.pack()

frame = tk.Frame(root, bg = "#99caff")
frame.place(relx = 0.05, rely =0.05, relwidth = 0.9, relheight = 0.9)
label = tk.Label(frame, text = "Kontroluj swoje subskrybcje", bg ="#99caff")
label.place(relx = 0.25, rely = 0.005, relwidth = 0.5, relheight =0.05)
entry = tk.Entry(frame, bg = "#FFFFFF")
entry.place(relx = 0.05, rely = 0.15, relwidth = 0.4, relheight = 0.05)

name1 = ""
data1 = ""
amount1 = 0
platform1 = ""
active1 = ""
category1 = ""
nop1 = 0
ed1 = 0

add_sub = tk.Button(root, text = "Dodaj Subskrybcję", padx = 10, pady= 10, fg = "black", bg = "#FFFFF7",
                    command = lambda:dm.add_element('sub', sub(name = input(name1),
                                                        date = input(data1),
                                                        amount = input(amount1),
                                                        platform = input(platform1),
                                                        active = input(active1),
                                                        category = input(category1),
                                                        number_of_payments = input(nop1),
                                                        expiration_date = input(ed1))))
#add_sub = tk.Button(root, text = "Czytaj z pliku", padx = 10, pady= 10, fg = "black", bg = "#FFFFF7",
#                   command = dm.get_data_from_file('sub'))
add_sub.place(relx = 0.10, rely = 0.25, relwidth = 0.18, relheight = 0.05)
remove_sub = tk.Button(root, text = "Usuń Subskrybcję", padx = 10, pady= 10, fg = "black", bg = "#FFFFF7")
remove_sub.place(relx = 0.30, rely = 0.25, relwidth = 0.18, relheight = 0.05)
check_expense = tk.Button(root, text = "Sprawdź Wydatki", padx = 10, pady= 10, fg = "black", bg = "#FFFFF7")
check_expense.place(relx = 0.50, rely = 0.25, relwidth = 0.18, relheight = 0.05)
search = tk.Button(root, text = "Szukaj",  fg = "black", bg = "#FFFFF7")
search.place(relx = 0.455, rely = 0.18, relwidth = 0.18, relheight = 0.05)

def cal():
  y = e1.get()
  m = e2.get()
  cal_x = calendar.month(int(y),int(m),w = 2, l = 1)
  print (cal_x)
  cal_out = Label(root, text=cal_x, font=("courier", 12, "bold"), bg="#999999" , justify=LEFT)
  cal_out.place(relx = 0.65, rely= 0.50)



label1 = Label(root, text="Rok:")
label1.place(relx = 0.80, rely = 0.30)

e1 = Entry(root)
e1.place(relx = 0.75, rely = 0.34)

label2 = Label(root, text="Miesiąc:")
label2.place(relx = 0.8, rely = 0.38)

e2 = Entry(root)
e2.place(relx = 0.75, rely = 0.42)

button = Button(root, text="Wyświetl Kalendarz",command=cal)
button.place(relx = 0.75, rely = 0.46)



root.mainloop()