from tkinter import *
from tkinter import messagebox
import random
import pyperclip
from random import choice, shuffle

FONT_NAME = "Courier"
bg_color = "dodger blue"

# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def convert_tuple(tup):
    strip = ''.join(tup)
    return strip


def genetrate_pass():
    nr_letters = random.randint(1, 10)
    nr_symbols = random.randint(1, 10)
    nr_numbers = random.randint(1, 10)

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    passweod_number = [choice(numbers) for _ in range(nr_numbers)]

    password_lists = password_letters + passweod_number + password_symbols
    shuffle(password_lists)

    password = convert_tuple(password_lists)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_name.get()
    email = username_email.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        if len(website) != 0:
            messagebox.showinfo(title="oops", message="your password is blank")
        else:
            messagebox.showinfo(title="oops", message="your website name is blank")
    else:
        is_ok = messagebox.askokcancel(title=f"Your credentials for {website} ", message=f"\n Email: {email} "
                                                                                         f"\n Password: {password}")

        if is_ok:
            with open("data.text", "a") as datafile:
                datafile.write(f"{website} / {email} / {password} \n")
                website_name.delete(0, END)
                username_email.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("PASSWORD")
window.config(bg=bg_color, padx=100, pady=10)


canvas = Canvas(height=320, width=320, bg="yellow", highlightthickness=0)
logo = PhotoImage(file="Screenshot 2022-07-29 171459.png")
canvas.create_image(165, 160, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website name", font=(FONT_NAME, 12, "bold"), bg=bg_color)
website_label.grid(row=2, column=0, padx=10, pady=10)
website_name = Entry(width=39)
website_name.focus()
website_name.grid(row=2, column=1, columnspan=2, pady=10)

username_email = Label(text="username/ email", font=(FONT_NAME, 12, "bold"), bg=bg_color)
username_email.grid(row=3, column=0, pady=10)
username_email = Entry(width=39)
username_email.grid(row=3, column=1, columnspan=2, pady=10)
username_email.insert(0, "203001170011@gmail.com")

password_gen = Label(text="password", font=(FONT_NAME, 12, "bold"), bg=bg_color)
password_gen.grid(row=4, column=0, padx=10, pady=10)
password_entry = Entry(width=18)
password_entry.grid(row=4, column=1, pady=10)


generate_but = Button(text="generate password", activebackground="green", command=genetrate_pass)

generate_but.grid(row=4, column=2)


add_but = Button(text="Add to vault", width=36, activebackground="green", command=save)
add_but .grid(row=5, column=0, columnspan=3, pady=20)

window.mainloop()