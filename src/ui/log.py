from tkinter import scrolledtext
import tkinter as tk


class Log:
    def __init__(self, root):
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.text_area.grid(row=100, columnspan=3, pady=10, padx=10)
        self.text_area.tag_configure("red", foreground="red")
        self._disableWrtieText()

    def added_log(self, text, color=None):
        self._enableWriteText()
        self.text_area.insert(tk.END, text + "\n", color)
        self._disableWrtieText()

    def _enableWriteText(self):
        self.text_area.config(state=tk.NORMAL)

    def _disableWrtieText(self):
        self.text_area.config(state=tk.DISABLED)

    def added_error(self, text):
        self.added_log(text=text, color="red")
