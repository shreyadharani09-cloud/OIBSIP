import tkinter as tk
from tkinter import messagebox
import secrets
import string
import random
import pyperclip

window = tk.Tk()
window.title("Random Password Generator")
window.geometry("600x500")
window.resizable(False, False)

password_history = []

frame = tk.Frame(window, padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

heading_label = tk.Label(
    frame,
    text="Random Password Generator",
    font=("Arial",20,"bold")
)
heading_label.grid(row=0,column=0,columnspan=2,pady=20)

length_label = tk.Label(
    frame,
    text="Password Length",
    font=("Arial",12)
)
length_label.grid(row=1,column=0,padx=10,pady=10,sticky="w")

length_entry = tk.Entry(
    frame,
    font=("Arial",12),
    width=20
)
length_entry.grid(row=1,column=1,padx=10,pady=10)

uppercase_var = tk.BooleanVar()
tk.Checkbutton(
    frame,
    text="Uppercase (A-Z)",
    variable=uppercase_var,
    font=("Arial",11)
).grid(row=2,column=0,sticky="w")

lowercase_var = tk.BooleanVar()
tk.Checkbutton(
    frame,
    text="Lowercase (a-z)",
    variable=lowercase_var,
    font=("Arial",11)
).grid(row=2,column=1,sticky="w")

numbers_var = tk.BooleanVar()
tk.Checkbutton(
    frame,
    text="Numbers (0-9)",
    variable=numbers_var,
    font=("Arial",11)
).grid(row=3,column=0,sticky="w")

symbols_var = tk.BooleanVar()
tk.Checkbutton(
    frame,
    text="Symbols (!@#$)",
    variable=symbols_var,
    font=("Arial",11)
).grid(row=3,column=1,sticky="w")

ambiguous_var = tk.BooleanVar()
tk.Checkbutton(
    frame,
    text="Exclude Ambiguous Characters",
    variable=ambiguous_var,
    font=("Arial",11)
).grid(row=4,column=0,columnspan=2,sticky="w",pady=5)

password_label = tk.Label(
    frame,
    text="Your password will appear here",
    font=("Arial",12,"bold"),
    fg="blue",
    wraplength=350
)
password_label.grid(row=5,column=0,columnspan=2,pady=15)

strength_label = tk.Label(
    frame,
    text="Strength:",
    font=("Arial",12,"bold")
)
strength_label.grid(row=6,column=0,columnspan=2,pady=10)

def generate_password():

    try:
        length = int(length_entry.get())

        if length < 8:
            messagebox.showerror(
                "Error",
                "Password length must be at least 8."
            )
            return

        selected_count = (
            uppercase_var.get() +
            lowercase_var.get() +
            numbers_var.get() +
            symbols_var.get()
        )

        if selected_count < 2:
            messagebox.showerror(
                "Selection Error",
                "Please select at least 2 character types."
            )
            return

        characters = ""
        password_list = []

        if uppercase_var.get():
            upper = string.ascii_uppercase
            if ambiguous_var.get():
                upper = upper.replace("O", "")
            characters += upper
            password_list.append(secrets.choice(upper))

        if lowercase_var.get():
            lower = string.ascii_lowercase
            if ambiguous_var.get():
                lower = lower.replace("l", "")
            characters += lower
            password_list.append(secrets.choice(lower))

        if numbers_var.get():
            nums = string.digits
            if ambiguous_var.get():
                nums = nums.replace("0", "").replace("1", "")
            characters += nums
            password_list.append(secrets.choice(nums))

        if symbols_var.get():
            symbols = string.punctuation
            characters += symbols
            password_list.append(secrets.choice(symbols))

        while len(password_list) < length:
            password_list.append(secrets.choice(characters))

        random.shuffle(password_list)

        password = "".join(password_list)

        password_label.config(text=f"Password: {password}")

        password_history.append(password)

        if len(password_history) > 5:
            password_history.pop(0)

        if length < 12:
            strength = "Medium"
            color = "orange"

        elif length < 16:
            strength = "Strong"
            color = "green"

        else:
            strength = "Very Strong"
            color = "dark green"

        strength_label.config(
            text=f"Strength: {strength}",
            fg=color
        )

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter a valid password length."
        )


def copy_password():

    password = password_label.cget("text")

    if password == "Your password will appear here":
        messagebox.showwarning(
            "Warning",
            "Generate a password first."
        )
        return

    password = password.replace("Password: ", "")
    pyperclip.copy(password)

    messagebox.showinfo(
        "Success",
        "Password copied to clipboard!"
    )


def view_history():

    history_window = tk.Toplevel(window)
    history_window.title("Password History")
    history_window.geometry("350x300")

    heading = tk.Label(
        history_window,
        text="Last 5 Generated Passwords",
        font=("Arial",14,"bold")
    )

    heading.pack(pady=10)

    if len(password_history) == 0:

        tk.Label(
            history_window,
            text="No passwords generated yet.",
            font=("Arial",11)
        ).pack()

    else:

        for i, pwd in enumerate(reversed(password_history), start=1):

            tk.Label(
                history_window,
                text=f"{i}. {pwd}",
                font=("Consolas",11)
            ).pack(anchor="w", padx=20)


generate_button = tk.Button(
    frame,
    text="Generate Password",
    font=("Arial",12,"bold"),
    width=20,
    command=generate_password
)

generate_button.grid(
    row=7,
    column=0,
    columnspan=2,
    pady=15
)

copy_button = tk.Button(
    frame,
    text="Copy Password",
    font=("Arial",11,"bold"),
    width=15,
    command=copy_password
)

copy_button.grid(
    row=8,
    column=0,
    pady=10
)

history_button = tk.Button(
    frame,
    text="View History",
    font=("Arial",11,"bold"),
    width=15,
    command=view_history
)

history_button.grid(
    row=8,
    column=1,
    pady=10
)

window.mainloop()