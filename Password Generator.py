import tkinter as tk
from tkinter import messagebox
import string
import secrets

def generate_password(length, complexity):
    """
    Generate a strong and random password.

    Args:
        length (int): The length of the password.
        complexity (str): The complexity of the password. Can be 'simple', 'medium', or 'complex'.

    Returns:
        str: The generated password.
    """
    if complexity == 'simple':
        characters = string.ascii_letters
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_password_callback():
    try:
        length = int(length_entry.get())
        if length < 8:
            messagebox.showerror("Error", "Password length should be at least 8 characters.")
            return
    except ValueError:
        messagebox.showerror("Error", "Password length should be an integer.")
        return

    complexity = complexity_var.get()
    password = generate_password(length, complexity)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#2b2b2b")

length_label = tk.Label(root, text="Password Length:", bg="white")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(root, bg="white")
length_entry.grid(row=0, column=1, padx=5, pady=5)

complexity_label = tk.Label(root, text="Password Complexity:", bg="white")
complexity_label.grid(row=1, column=0, padx=5, pady=5)

complexity_var = tk.StringVar(root)
complexity_var.set('simple')
complexity_option = tk.OptionMenu(root, complexity_var, 'simple', 'medium', 'complex')
complexity_option.config(bg="white")
complexity_option.grid(row=1, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_callback, bg="white")
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

password_label = tk.Label(root, text="Generated Password:", bg="white")
password_label.grid(row=3, column=0, padx=5, pady=5)

password_entry = tk.Entry(root, width=50, bg="white")
password_entry.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
