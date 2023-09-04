import tkinter as tk


def create_label(root, text):
    label = tk.Label(root, text=text)
    return label


def create_entry(root):
    entry = tk.Entry(root)
    return entry


def create_checkbox(root, text):
    checkbox_var = tk.BooleanVar()
    checkbox = tk.Checkbutton(root, text=text, variable=checkbox_var)
    return checkbox_var, checkbox


def create_row(root, row, text, checkbox_text=None):
    label = create_label(root, text=text)
    label_entry = create_entry(root)
    label.grid(row=row, column=0, padx=10, pady=5)
    label_entry.grid(row=row, column=1, padx=10, pady=5)

    if not checkbox_text:
        return label_entry
    checkbox_var, checkbox = create_checkbox(root, text=checkbox_text)
    checkbox.grid(row=row, column=2, padx=10, pady=5)

    return label_entry, checkbox_var, checkbox
