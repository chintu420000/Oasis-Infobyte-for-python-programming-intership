import tkinter as tk
import random
import string
import pyperclip
class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Password Generator")
        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_var = tk.IntVar(value=12)
        self.length_entry = tk.Entry(master, textvariable=self.length_var, width=5)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        tk.Checkbutton(master, text="Include Uppercase", variable=self.include_uppercase).grid(row=1, column=0, sticky='w', padx=10)
        tk.Checkbutton(master, text="Include Lowercase", variable=self.include_lowercase).grid(row=2, column=0, sticky='w', padx=10)
        tk.Checkbutton(master, text="Include Numbers", variable=self.include_numbers).grid(row=3, column=0, sticky='w', padx=10)
        tk.Checkbutton(master, text="Include Symbols", variable=self.include_symbols).grid(row=4, column=0, sticky='w', padx=10)
        self.exclude_label = tk.Label(master, text="Exclude Characters:")
        self.exclude_label.grid(row=5, column=0, padx=10, pady=10)
        self.exclude_entry = tk.Entry(master, width=20)
        self.exclude_entry.grid(row=5, column=1, padx=10, pady=10)
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.result_label = tk.Label(master, text="Generated Password:")
        self.result_label.grid(row=7, column=0, padx=10, pady=10)
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(master, textvariable=self.result_var, width=30)
        self.result_entry.grid(row=7, column=1, padx=10, pady=10)
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=8, column=0, columnspan=2, pady=10)
    def generate_password(self):
        length = self.length_var.get()
        character_set = ""
        if self.include_uppercase.get():
            character_set += string.ascii_uppercase
        if self.include_lowercase.get():
            character_set += string.ascii_lowercase
        if self.include_numbers.get():
            character_set += string.digits
        if self.include_symbols.get():
            character_set += string.punctuation

        exclude_chars = self.exclude_entry.get()
        character_set = ''.join(c for c in character_set if c not in exclude_chars)

        # Generate password efficiently
        if character_set:
            password = ''.join(random.choices(character_set, k=length))
            self.result_var.set(password)
    def copy_to_clipboard(self):
        password = self.result_var.get()
        if password:
            pyperclip.copy(password)
if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()
