import tkinter as tk
from tkinter import messagebox

def calculate_result():
    try:
        a = float(num1_entry.get())
        b = float(num2_entry.get())
        op = operator_var.get()

        if op == "Add (+)":
            ans = a + b
        elif op == "Subtract (-)":
            ans = a - b
        elif op == "Multiply (*)":
            ans = a * b
        elif op == "Divide (/)":
            if b == 0:
                messagebox.showerror("Error", "Division by zero not allowed!")
                return
            ans = a / b
        else:
            messagebox.showwarning("Warning", "Please select an operation")
            return

        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, ans)
        result_entry.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def clear_all():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.config(state="readonly")
    operator_var.set("Select Operation")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("420x460")
root.resizable(False, False)


tk.Label(root, text="Calculator", font=("Arial", 18, "bold")).pack(pady=15)


tk.Label(root, text="First Number").pack()
num1_entry = tk.Entry(root, font=("Arial", 14), width=25)
num1_entry.pack(pady=5)


tk.Label(root, text="Second Number").pack()
num2_entry = tk.Entry(root, font=("Arial", 14), width=25)
num2_entry.pack(pady=5)


operator_var = tk.StringVar(value="Select Operation")
operations = ["Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)"]
tk.OptionMenu(root, operator_var, *operations).pack(pady=12)


tk.Button(root, text="Calculate", width=18, font=("Arial", 13),
          command=calculate_result).pack(pady=10)

tk.Button(root, text="Clear", width=18, font=("Arial", 13),
          command=clear_all).pack(pady=5)


tk.Label(root, text="Result", font=("Arial", 14, "bold")).pack(pady=10)
result_entry = tk.Entry(root, font=("Arial", 14), width=25, state="readonly")
result_entry.pack(pady=5)


root.mainloop()

