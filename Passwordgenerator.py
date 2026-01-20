import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showwarning("Warning", "Enter valid length!")
            return

        chars = ""

        if letters_var.get():
            chars += string.ascii_letters
        if numbers_var.get():
            chars += string.digits
        if symbols_var.get():
            chars += string.punctuation

        if chars == "":
            messagebox.showwarning("Warning", "Select at least one option!")
            return

        password = "".join(random.choice(chars) for _ in range(length))

        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
        result_entry.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Length must be a number!")

def clear_all():
    length_entry.delete(0, tk.END)
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.config(state="readonly")
    letters_var.set(0)
    numbers_var.set(0)
    symbols_var.set(0)


root = tk.Tk()
root.title("Password Generator")
root.geometry("450x500")
root.resizable(False, False)


tk.Label(root, text="Password Generator", font=("Arial", 18, "bold")).pack(pady=15)


tk.Label(root, text="Password Length", font=("Arial", 12)).pack()
length_entry = tk.Entry(root, font=("Arial", 14), width=25)
length_entry.pack(pady=8)


options_frame = tk.Frame(root)
options_frame.pack(pady=10)

letters_var = tk.IntVar()
numbers_var = tk.IntVar()
symbols_var = tk.IntVar()

tk.Checkbutton(options_frame, text="Include Letters", variable=letters_var).pack(anchor="w")
tk.Checkbutton(options_frame, text="Include Numbers", variable=numbers_var).pack(anchor="w")
tk.Checkbutton(options_frame, text="Include Symbols", variable=symbols_var).pack(anchor="w")


tk.Button(root, text="Generate Password", width=20, font=("Arial", 13),
          command=generate_password).pack(pady=15)

tk.Button(root, text="Clear", width=20, font=("Arial", 13),
          command=clear_all).pack(pady=5)


tk.Label(root, text="Generated Password", font=("Arial", 14, "bold")).pack(pady=10)
result_entry = tk.Entry(root, font=("Arial", 14), width=30, state="readonly")
result_entry.pack(pady=5)


root.mainloop()
