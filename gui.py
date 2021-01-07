import tkinter as tk
from tkinter import *
import os
import data_manipulation as dm
import expense as exp
from subscription import subscription as sub
import calendar
import stats as st

def gui():
    root = tk.Tk()
    root.title("Subs App")
    canvas = tk.Canvas(root, height=700, width=700, bg="#FFFFF7")
    canvas.pack()

    frame = tk.Frame(root, bg="#99caff")
    frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
    label = tk.Label(frame, text="Kontroluj swoje subskrybcje", bg="#99caff")
    label.place(relx=0.25, rely=0.005, relwidth=0.5, relheight=0.05)


    # entry = tk.Entry(frame, bg="#FFFFFF")
    # entry.place(relx=0.05, rely=0.15, relwidth=0.4, relheight=0.05)


    # def adding():
    #   name = input("Wprowadź nazwę ")
    #  data = input("Wprowadź nazwę ")
    # amount = input("Wprowadź nazwę ")
    # ctive = input("Wprowadź nazwę ")
    # category = input("Wprowadź nazwę ")
    # nop = input("Wprowadź nazwę ")
    # ed = input("Wprowadź nazwę ")
    # return name, data, amount, platform, active, category, nop, ed


    def show_content_add_sub():
        def adding():
            x1 = ename.get()
            x2 = edate.get()
            x3 = eamount.get()
            x4 = eplatform.get()
            x5 = eactive.get()
            x6 = ecategory.get()
            x7 = enop.get()
            x8 = eed.get()

            add = tk.Button(root, text="Potwierdź", padx=10, pady=10, fg="black", bg="#FFFFF7",
                            command=lambda: dm.add_element('sub', sub(name=str(x1),
                                                                      date=str(x2),
                                                                      amount=str(x3),
                                                                      platform=str(x4),
                                                                      active=str(x5),
                                                                      category=str(x6),
                                                                      number_of_payments=str(x7),
                                                                      expiration_date=str(x8))), )
            add.place(relx=0.60, rely=0.75)

            def rem():
                add.place_forget()
                back_button1.place_forget()

            back_button1 = tk.Button(root, text="Wróć", padx=10, pady=10, fg="black", bg="#FFFFF7",
                                     command=rem)
            back_button1.place(relx=0.60, rely=0.85)

        lname = tk.Label(root, text="Nazwa:")
        lname.place(relx=0.45, rely=0.32)
        ename = Entry(root)
        ename.place(relx=0.40, rely=0.36)
        ldate = tk.Label(root, text="Data:")
        ldate.place(relx=0.45, rely=0.40)
        edate = Entry(root)
        edate.place(relx=0.40, rely=0.44)
        lamount = tk.Label(root, text="Ilość:")
        lamount.place(relx=0.45, rely=0.48)
        eamount = Entry(root)
        eamount.place(relx=0.40, rely=0.52)
        lplatform = tk.Label(root, text="Platforma:")
        lplatform.place(relx=0.45, rely=0.56)
        eplatform = Entry(root)
        eplatform.place(relx=0.40, rely=0.60)
        lactive = tk.Label(root, text="Czy aktywna?")
        lactive.place(relx=0.45, rely=0.64)
        eactive = Entry(root)
        eactive.place(relx=0.40, rely=0.68)
        lcategory = tk.Label(root, text="Kategoria:")
        lcategory.place(relx=0.45, rely=0.72)
        ecategory = Entry(root)
        ecategory.place(relx=0.40, rely=0.76)
        lnop = tk.Label(root, text="Liczba zapłat:")
        lnop.place(relx=0.45, rely=0.8)
        enop = Entry(root)
        enop.place(relx=0.40, rely=0.84)
        led = tk.Label(root, text="Data wygaśnięcia:")
        led.place(relx=0.45, rely=0.88)
        eed = Entry(root)
        eed.place(relx=0.40, rely=0.92)
        but = tk.Button(root, text="Gotowe", padx=10, pady=10, fg="black", bg="#FFFFF7", command=adding)
        but.place(relx=0.60, rely=0.75)

        def hide_content():
            lname.place_forget()
            ename.place_forget()
            ldate.place_forget()
            edate.place_forget()
            lamount.place_forget()
            eamount.place_forget()
            lplatform.place_forget()
            eplatform.place_forget()
            lactive.place_forget()
            eactive.place_forget()
            lcategory.place_forget()
            ecategory.place_forget()
            lnop.place_forget()
            enop.place_forget()
            led.place_forget()
            eed.place_forget()
            but.place_forget()
            back_button.place_forget()

        back_button = tk.Button(root, text="Wróć", padx=10, pady=10, fg="black", bg="#FFFFF7",
                                command=hide_content)
        back_button.place(relx=0.6, rely=0.85)


    add_sub = tk.Button(root, text="Dodaj Subskrybcję", padx=10, pady=10, fg="black", bg="#FFFFF7",
                        command=show_content_add_sub)
    # command=lambda: dm.add_element('sub', sub(name=input("Wprowadź nazwę"),
    #                                         date=input("Wprowadź datę"),
    #                                        amount=input("Wprowadź nazwę"),
    #                                       platform=input("Wprowadź platformę"),
    #                                      active=input("Wprowadź nazwę"),
    #                                     category=input("Wprowadź nazwę"),
    #                                    number_of_payments=input("Wprowadź nazwę"),
    #                                   expiration_date=input("Wprowadź nazwę"))))
    add_sub.place(relx=0.10, rely=0.25, relwidth=0.18, relheight=0.05)


    def show_content_rem_sub():
        def adding2():
            y1 = ename1.get()
            remove = tk.Button(root, text="Potwierdź", padx=10, pady=10, fg="black", bg="#FFFFF7",
                               command=lambda: dm.delete_element('sub', name=str(y1)))
            remove.place(relx=0.4, rely=0.42)

            def rem1():
                remove.place_forget()
                back_button2.place_forget()

            back_button2 = tk.Button(root, text="Wróć", padx=10, pady=10, fg="black", bg="#FFFFF7",
                                     command=rem1)
            back_button2.place(relx=0.5, rely=0.42)

        lname1 = tk.Label(root, text="Nazwa:")
        lname1.place(relx=0.45, rely=0.32)
        ename1 = Entry(root)
        ename1.place(relx=0.40, rely=0.36)
        but1 = tk.Button(root, text="Gotowe", padx=10, pady=10, fg="black", bg="#FFFFF7", command=adding2)
        but1.place(relx=0.4, rely=0.42)

        def hide_content1():
            lname1.place_forget()
            ename1.place_forget()
            but1.place_forget()
            back_button0.place_forget()

        back_button0 = tk.Button(root, text=" Wróć", padx=10, pady=10, fg="black", bg="#FFFFF7",
                                 command=hide_content1)
        back_button0.place(relx=0.5, rely=0.42)


    remove_sub = tk.Button(root, text="Usuń Subskrybcję", padx=10, pady=10, fg="black", bg="#FFFFF7",
                           command=show_content_rem_sub)
    #   command=lambda: dm.delete_element('sub', name=input("Wprowadź nazwę: ")))
    # command=lambda: dm.delete_element('sub', sub(name=input("Wprowadź nazwę"),
    #                                             date=input("Wprowadź datę"),
    #                                            amount=input("Wprowadź nazwę"),
    #                                           platform=input("Wprowadź platformę"),
    #                                          active=input("Wprowadź nazwę"),
    #                                         category=input("Wprowadź nazwę"),
    #                                        number_of_payments=input("Wprowadź nazwę"),
    #                                       expiration_date=input("Wprowadź nazwę"))))
    remove_sub.place(relx=0.30, rely=0.25, relwidth=0.18, relheight=0.05)

    get_all_subs = tk.Button(root, text="Wyświetl Subskrybcje", padx=10, pady=10, fg="black", bg="#FFFFF7",
                             command=lambda: print(dm.get_data_from_file('sub')))
    get_all_subs.place(relx=0.10, rely=0.35, relwidth=0.18, relheight=0.05)

    check_status = tk.Button(root, text="Sprawdź Status Subskrybcji", padx=10, pady=10, fg="black", bg="#FFFFF7",
                             command=st.plot_stats_subscriptions)
    check_status.place(relx=0.50, rely=0.25, relwidth=0.22, relheight=0.05)
    check_monthly_expanses = tk.Button(root, text="Sprawdź Miesięczne Wydatki", padx=10, pady=10, fg="black", bg="#FFFFF7",
                                       command=lambda: st.plot_period_stats_expenses(
                                           start=input("Wprowadź datę początkową (YYYY lub MM.YYYY) "), end=input("Wprowadź datę końcową (ten sam format co wyżej) ")))
    check_monthly_expanses.place(relx=0.10, rely=0.45, relwidth=0.24, relheight=0.05)
    check_stats = tk.Button(root, text="Sprawdź Statystyki Wydatków", padx=10, pady=10, fg="black", bg="#FFFFF7",
                            command=lambda: st.plot_stats_expenses(
                                start=input("Wprowadź datę początkową (YYYY, MM.YYYY lub DD.MM.YYYY) "), end=input("Wprowadź datę końcową (ten sam format co wyżej) ")))
    check_stats.place(relx=0.10, rely=0.55, relwidth=0.24, relheight=0.05)


    # search = tk.Button(root, text="Szukaj", fg="black", bg="#FFFFF7")
    # search.place(relx=0.455, rely=0.18, relwidth=0.18, relheight=0.05)


    def cal():
        y = e1.get()
        m = e2.get()
        cal_x = calendar.month(int(y), int(m), w=2, l=1)
        print(cal_x)
        cal_out = Label(root, text=cal_x, font=("courier", 12, "bold"), bg="#999999", justify=LEFT)
        cal_out.place(relx=0.65, rely=0.50)


    label1 = Label(root, text="Rok:")
    label1.place(relx=0.80, rely=0.30)

    e1 = Entry(root)
    e1.place(relx=0.75, rely=0.34)

    label2 = Label(root, text="Miesiąc:")
    label2.place(relx=0.8, rely=0.38)

    e2 = Entry(root)
    e2.place(relx=0.75, rely=0.42)

    button = Button(root, text="Wyświetl Kalendarz", command=cal)
    button.place(relx=0.75, rely=0.46)

    root.mainloop()
