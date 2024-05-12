import tkinter as tk


class RestaurantMenuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurant Menu App")

        self.menu_items = {
            "Burger": 10,
            "Pizza": 12,
            "Pasta": 8,
            "Salad": 6,
            "Steak": 15
        }

        self.create_widgets()

    def create_widgets(self):
        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack(padx=20, pady=20)

        for item, price in self.menu_items.items():
            item_label = tk.Label(self.menu_frame, text=f"{item}: ${price}")
            item_label.pack(anchor="w")

        self.total_label = tk.Label(self.master, text="Total: $0")
        self.total_label.pack(pady=10)

        self.order_button = tk.Button(self.master, text="Place Order", command=self.place_order)
        self.order_button.pack()

    def place_order(self):
        total_price = sum(self.menu_items.values())
        self.total_label.config(text=f"Total: ${total_price}")


def main():
    root = tk.Tk()
    app = RestaurantMenuApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
