from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 6)
    nr_symbols = random.randint(1, 3)
    nr_numbers = random.randint(1, 3)

    new_characters = [random.choice(letters) for i in range(nr_letters)]
    new_symbols = [random.choice(symbols) for j in range(nr_symbols)]
    new_numbers = [random.choice(numbers) for k in range(nr_numbers)]

    password_list = new_characters + new_symbols + new_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)
    password_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered: \nEmail: {email}\n"
                                                                   f"Password: {password}\nDo you wanna save?")

        if is_ok:
            with open("data.txt", mode='a') as data:
                data.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "example_mail@mymail.com")

password_input = Entry(width=27)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate", font=("Ariel", 8), width=5, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", font=("Ariel", 8), width=37, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
