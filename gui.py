import customtkinter
from tkinter import *
from tkinter import messagebox
from datetime import date

app = customtkinter.CTk()
app.title("Restaurant App")
app.geometry("1000x400")
app.config(bg="#25283b")
app.resizable(False, False)

font1 = ('Arial', 25, 'bold')
font2 = ('Arial', 15, 'bold')
font3 = ('Arial', 12, 'bold')
price_list = [50, 30, 25]
total_price = 0

bill_frame = customtkinter.CTkFrame(app, width=300, height=400, fg_color='#545457')
bill_frame.place(x=700, y=0)

menu_label = customtkinter.CTkLabel(app,
                                    text="Prime Restaurant",
                                    text_color='#ffffff',
                                    bg_color='#25283b'
                                    )

menu_label.place(x=230, y=5)

img_label1 = customtkinter.CTkLabel(app,
                                    text="Seafood Pasta\n Price: $50",
                                    text_color='#ffffff',
                                    fg_color='#090b17',
                                    width=200,
                                    height=200,
                                    corner_radius=20,
                                    compound=TOP,
                                    anchor=N)
img_label1.place(x=30, y=70)

img_label2 = customtkinter.CTkLabel(app,
                                    text="Rice and Chicken\n Price: $40",
                                    text_color='#ffffff',
                                    fg_color='#090b17',
                                    width=200,
                                    height=200,
                                    corner_radius=20,
                                    compound=TOP,
                                    anchor=N)
img_label2.place(x=250, y=70)

img_label3 = customtkinter.CTkLabel(app,
                                    text="Mushroom Pasta\n Price: $50",
                                    text_color='#ffffff',
                                    fg_color='#090b17',
                                    width=100,
                                    height=200,
                                    corner_radius=20,
                                    compound=TOP,
                                    anchor=N)
img_label3.place(x=470, y=70)


def add_to_order(item, price):
    global total_price
    total_price += price
    messagebox.showinfo("Added to Order", f"{item} added to your order!")
    update_total()


def update_total():
    global total_price
    total_label.configure(text=f"Total Price: ${total_price}")


def clear_order():
    global total_price
    total_price = 0
    update_total()
    messagebox.showinfo("Order Cleared", "Your order has been cleared.")


order_button1 = customtkinter.CTkButton(app, text="Order Seafood Pasta",
                                        command=lambda: add_to_order("Seafood Pasta", 50), height=30)
order_button1.place(x=70, y=290)

order_button2 = customtkinter.CTkButton(app, text="Order Rice and Chicken",
                                        command=lambda: add_to_order("Rice and Chicken", 40), height=30)
order_button2.place(x=290, y=290)

order_button3 = customtkinter.CTkButton(app, text="Order Mushroom Pasta",
                                        command=lambda: add_to_order("Mushroom Pasta", 35), height=30)
order_button3.place(x=510, y=290)

total_label = customtkinter.CTkLabel(app, text="Total Price: $0", text_color='#ffffff', bg_color='#25283b', font=font3)
total_label.place(x=700, y=300)

clear_button = customtkinter.CTkButton(app, text="Clear Order", command=clear_order)
clear_button.place(x=800, y=350)
