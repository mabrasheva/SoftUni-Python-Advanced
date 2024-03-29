from tkinter import Button, Label, Entry
from auth_services import register, login
from products_service import get_all_products
from PIL import ImageTk, Image


def clear_window(tk):
    for widget in tk.winfo_children():
        widget.destroy()


def render_main_screen(tk):
    Button(tk, text="Login", bg="green", command=lambda: render_login_screen(tk)).grid(row=0, column=0)
    Button(tk, text="Register", bg="yellow", command=lambda: render_register_screen(tk)).grid(row=0, column=1)


def render_register_screen(tk):
    clear_window(tk)

    Label(tk, text="Email").grid(row=0, column=0)
    email_entry = Entry(tk)
    email_entry.grid(row=0, column=1)

    Label(tk, text="Password").grid(row=1, column=0)
    password_entry = Entry(tk)
    password_entry.grid(row=1, column=1)

    Label(tk, text="Confirm password").grid(row=2, column=0)
    confirm_password_entry = Entry(tk)
    confirm_password_entry.grid(row=2, column=1)

    def on_register():
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if password != confirm_password:
            Label(tk, text="Password must match!", fg="red").grid(row=3, column=1)
            return

        result = register(email, password)
        if result:
            render_login_screen(tk)
        else:
            Label(tk, text="Email is already registered!", fg="red").grid(row=3, column=1)

    Button(tk, text="Register", command=lambda: on_register()).grid(row=4, column=1)


def render_login_screen(tk):
    clear_window(tk)

    Label(tk, text="Email").grid(row=0, column=0)
    email_entry = Entry(tk)
    email_entry.grid(row=0, column=1)

    Label(tk, text="Password").grid(row=1, column=0)
    password_entry = Entry(tk)
    password_entry.grid(row=1, column=1)

    def on_login():
        email = email_entry.get()
        password = password_entry.get()

        result = login(email, password)

        if result:
            render_products_list_screen(tk)
        else:
            Label(tk, text="Invalid credentials!", fg="red").grid(row=2, column=1)

    Button(tk, text="Login", command=lambda: on_login()).grid(row=3, column=1)


def render_products_list_screen(tk):
    clear_window(tk)

    products = get_all_products()
    row = 0
    column = 0
    for product in products:
        if column % 3 == 0:
            row += 4
            column = 0
        Label(tk, text=product["name"]).grid(row=row, column=column)

        photo_image = Image.open(f"./{product['imgPath']}")
        photo_image = photo_image.resize((100, 100))
        img = ImageTk.PhotoImage(photo_image)
        img_label = Label(tk, image=img)
        img_label.image = img
        img_label.grid(row=row + 1, column=column)

        Label(tk, text=product["count"]).grid(row=row + 2, column=column)
        Button(tk, text="Buy", command=lambda buy_product=product["id"]: print(buy_product)).grid(row=row + 3,
                                                                                                  column=column)
        column += 1
