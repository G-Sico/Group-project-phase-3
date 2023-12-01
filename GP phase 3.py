import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def check_login():
    entered_username = username_entry.get().lower()
    entered_password = password_entry.get().lower()
    if entered_username == "admin" and entered_password == "password":
        root.withdraw()
        ask_class_window = tk.Toplevel(root)
        ask_class_window.title("Class Information")

        def submit_class():
            user_class = class_entry.get()
            ask_class_window.destroy()
            open_class_window(user_class)

        class_label = tk.Label(ask_class_window, text="Enter the class you need help with:")
        class_label.pack()

        class_entry = tk.Entry(ask_class_window)
        class_entry.pack()

        submit_button = tk.Button(ask_class_window, text="Submit", command=submit_class)
        submit_button.pack()

        ask_class_window.geometry("300x150")
        ask_class_window.configure(bg="white")

    else:
        messagebox.showerror("Login failed", "Invalid username or password")

def open_class_window(user_class):
    class_window = tk.Toplevel(root)
    class_window.title(user_class + " Help")

    notebook = ttk.Notebook(class_window)
    notebook.pack(expand=True, fill='both', padx=5, pady=5)

    button_titles = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6"]

    for title in button_titles:
        page = ttk.Frame(notebook)
        notebook.add(page, text=title)

        label = tk.Label(page, text=f"Content for {title}")
        label.pack(padx=10, pady=10)

    class_window.geometry("400x300")
    class_window.configure(bg="#3498db")

root = tk.Tk()
root.title("login CSC110")
root.geometry("300x150")
root.configure(bg="white")

username_label = tk.Label(root, text="Username: ", bg="white", fg="black")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")

username_entry = tk.Entry(root, bg="light grey", fg="black")
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Password:", bg="white", fg="black")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="E")

password_entry = tk.Entry(root, show="*", bg="light grey", fg="black")
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(root, text="Login", command=check_login, bg="#2ecc71", fg="white")
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
