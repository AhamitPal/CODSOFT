import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")


root = tk.Tk()
root.title("To-Do List")


listbox = tk.Listbox(root, width=50,bg='lightblue')
listbox.pack(pady=10)


task_entry = tk.Entry(root, width=50,bg='lightgrey')
task_entry.pack()


add_button = tk.Button(root, text="Add Task", command=add_task,bg='green')
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg= 'red')
delete_button.pack(pady=5)


root.mainloop()
