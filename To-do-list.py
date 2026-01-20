import tkinter as tk
from tkinter import messagebox

FILE_NAME = "tasks.txt"

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def update_task():
    try:
        index = listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            listbox.delete(index)
            listbox.insert(index, new_task)
            task_entry.delete(0, tk.END)
            save_tasks()
        else:
            messagebox.showwarning("Warning", "Enter updated task!")
    except:
        messagebox.showwarning("Warning", "Select a task to update!")

def mark_completed():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        listbox.delete(index)
        listbox.insert(index, "✔ " + task)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

def save_tasks():
    with open(FILE_NAME, "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for task in file:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass


root = tk.Tk()
root.title("Advanced To-Do List App")
root.geometry("450x520")
root.resizable(False, False)


tk.Label(root, text="To-Do List Application", font=("Arial", 18, "bold")).pack(pady=10)


task_entry = tk.Entry(root, font=("Arial", 14), width=28)
task_entry.pack(pady=10)


btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=12, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=12, command=update_task).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete", width=12, command=delete_task).grid(row=1, column=0, pady=5)
tk.Button(btn_frame, text="Complete", width=12, command=mark_completed).grid(row=1, column=1, pady=5)


listbox = tk.Listbox(root, font=("Arial", 12), width=45, height=12)
listbox.pack(pady=15)


load_tasks()


root.mainloop()
