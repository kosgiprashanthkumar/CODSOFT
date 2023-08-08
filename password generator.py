import tkinter as tk
import random
import string

def generate_password():
    password_length = int(password_length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    generated_password_entry.delete(0, tk.END)
    generated_password_entry.insert(0, generated_password)

def reset_fields():
    username_entry.delete(0, tk.END)
    password_length_entry.delete(0, tk.END)
    generated_password_entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")
root.configure(bg='silver')

# Heading
heading_label = tk.Label(root, text="Password Generator", font=("arial", 16, "bold"), fg="blue",)
heading_label.grid(row=0, column=0, columnspan=2, pady=10)

# Username Label and Entry
username_label = tk.Label(root, text="Enter Username:")
username_label.grid(row=1, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=5, pady=5)

# Password Length Label and Entry
password_length_label = tk.Label(root, text="Enter Password Length:")
password_length_label.grid(row=2, column=0, padx=5, pady=5)
password_length_entry = tk.Entry(root)
password_length_entry.grid(row=2, column=1, padx=5, pady=5)

# Generated Password Label and Entry
generated_password_label = tk.Label(root, text="Generated Password:")
generated_password_label.grid(row=3, column=0, padx=5, pady=5)
generated_password_entry = tk.Entry(root)
generated_password_entry.grid(row=3, column=1, padx=5, pady=5)

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white")
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Accept and Reset Buttons
accept_button = tk.Button(root, text="Accept", command=root.quit, bg="green", fg="white")
reset_button = tk.Button(root, text="Reset", command=reset_fields, bg="red", fg="white")
accept_button.grid(row=5, column=0,columnspan=2, padx=5, pady=5)
reset_button.grid(row=6, column=0, columnspan=2,padx=5, pady=5)

root.mainloop()
