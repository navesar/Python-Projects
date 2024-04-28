from tkinter import Tk, Entry, PhotoImage, Canvas, Label, Button, END, messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    symbols = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
        '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^',
        '_', '`', '{', '|', '}', '~'
    ]
    numbers = list("1234567890")
    num_of_letters = random.randint(8, 10)
    num_of_symbols = random.randint(2, 4)
    num_of_numbers = random.randint(2, 4)
    generated_password = [random.choice(letters) for _ in range(num_of_letters)]
    [generated_password.insert(random.randint(a=0, b=len(generated_password)), random.choice(symbols))
     for _ in range(num_of_symbols)]
    [generated_password.insert(random.randint(a=0, b=len(generated_password)), random.choice(numbers))
     for _ in range(num_of_numbers)]
    generated_password = "".join(generated_password)
    password_input.delete(0, END)
    password_input.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()

    if website == "" or email_username == "" or password == "":
        messagebox.showerror(title="Error", message="Please fill all the fields")
        return

    data = f"{website} | {email_username} | {password}"
    if messagebox.askokcancel(title="Confirm Data", message=f"Do you want to save this data?\n{data}"):
        with open("data.txt", "a") as data_file:
            data_file.write(f"{data}\n")
        website_input.delete(0, END)
        password_input.delete(0, END)
        messagebox.showinfo(title="Data Saved", message="Data saved successfully to data.txt")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas()
logo_img = PhotoImage(file="logo.png")
canvas.create_image(200, 120, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=80)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_input = Entry(width=80)
email_username_input.insert(0, "example@gmail.com")
email_username_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=80)
password_input.grid(row=3, column=1, columnspan=2)

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=68, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
