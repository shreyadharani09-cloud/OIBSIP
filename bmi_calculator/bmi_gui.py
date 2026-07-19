import tkinter as tk
import csv
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

window = tk.Tk()

window.title("BMI Calculator")
window.geometry("700x500")
window.resizable(False, False)

frame = tk.Frame(window, padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

heading_label = tk.Label(frame,text="BMI Calculator",font=("Arial", 20, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

name_label = tk.Label(frame, text="Name", font=("Arial", 12))
name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

name_entry = tk.Entry(frame, font=("Arial", 12), width=25)
name_entry.grid(row=1, column=1, padx=10, pady=10)

weight_label = tk.Label(frame, text="Weight", font=("Arial", 12))
weight_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

weight_entry = tk.Entry(frame, font=("Arial", 12), width=25)
weight_entry.grid(row=2, column=1, padx=10, pady=10)

height_label = tk.Label(frame, text="Height", font=("Arial", 12))
height_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

height_entry = tk.Entry(frame, font=("Arial", 12), width=25)
height_entry.grid(row=3, column=1, padx=10, pady=10)

def calculate_bmi():
 try:
    name = name_entry.get()
    if name == "":
        messagebox.showwarning("Name Error", "Please enter your name.")
        return
    weight = float(weight_entry.get())
    if weight <= 0:
        messagebox.showwarning("Weight Error", "Weight must be greater than 0.")
        return
    height = float(height_entry.get())
    if height <= 0:
        messagebox.showwarning("Height Error", "Height must be greater than 0.")
        return

    height = height * 0.3048

    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Underweight"
        color = "blue"

    elif bmi < 25:
        category = "Normal"
        color = "green"

    elif bmi < 30:
        category = "Overweight"
        color = "brown"

    else:
        category = "Obese"
        color = "red"

    result_label.config(text=f"Name: {name}\nBMI: {bmi:.2f}\nCategory: {category}",fg=color)
    with open("bmi_records.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, weight, height, round(bmi, 2), category])

 except ValueError:
     messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")

calculate_button = tk.Button(frame,text="Calculate BMI",font=("Arial", 12, "bold"),width=15 , command=calculate_bmi)
calculate_button.grid(row=5, column=0, padx=10, pady=10)


result_label = tk.Label(frame,text="Enter your details and click Calculate BMI",font=("Arial", 12),fg="gray")
result_label.grid(row=4, column=0, columnspan=2, pady=20)


def view_history():

    history_window = tk.Toplevel(window)

    history_window.title("BMI History")
    history_window.geometry("500x300")

    text_box = tk.Text(history_window, width=60, height=15)
    text_box.pack()

    with open("bmi_records.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
         text_box.insert(tk.END, " | ".join(row) + "\n")

history_button = tk.Button(frame, text="View History",font=("Arial", 12, "bold"),width=15,command=view_history)
history_button.grid(row=5, column=1, padx=10, pady=10)



def clear_fields():

    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    result_label.config(text="")


clear_button = tk.Button(frame,text="Clear",font=("Arial", 12, "bold"),width=15,command=clear_fields)
clear_button.grid(row=6, column=0, columnspan=2, pady=10)

def show_graph():

    names = []
    bmi_values = []

    with open("bmi_records.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            names.append(row[0])
            bmi_values.append(float(row[3]))

    plt.plot(names, bmi_values)

    plt.title("BMI Graph")
    plt.xlabel("Name")
    plt.ylabel("BMI")

    plt.show()

graph_button = tk.Button(frame,text="Show Graph",font=("Arial", 12, "bold"),width=15,command=show_graph)
graph_button.grid(row=7, column=0, columnspan=2, pady=10)

window.mainloop()