import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Calculator")
        self.resizable(False, False)
        self.expression = ""
        self.display_var = tk.StringVar()
        self._create_widgets()

    def _create_widgets(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('TButton', font=('Arial', 16), padding=5)
        
        display = ttk.Entry(self, textvariable=self.display_var, justify='right', font=('Arial', 20))
        display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=(10, 20))

        buttons = [
            ('7', self._append), ('8', self._append), ('9', self._append), ('/', self._append),
            ('4', self._append), ('5', self._append), ('6', self._append), ('*', self._append),
            ('1', self._append), ('2', self._append), ('3', self._append), ('-', self._append),
            ('0', self._append), ('.', self._append), ('C', self._clear), ('+', self._append),
            ('=', self._calculate)
        ]

        row = 1
        col = 0
        for label, cmd in buttons:
            if label == '=':
                ttk.Button(self, text=label, command=cmd).grid(row=row, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)
            else:
                ttk.Button(self, text=label, command=lambda t=label: cmd(t)).grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
                col += 1
                if col > 3:
                    col = 0
                    row += 1

        for i in range(4):
            self.columnconfigure(i, weight=1)
        for i in range(row+1):
            self.rowconfigure(i, weight=1)

    def _append(self, char):
        self.expression += char
        self.display_var.set(self.expression)

    def _clear(self, _=None):
        self.expression = ""
        self.display_var.set("")

    def _calculate(self):
        try:
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

if __name__ == "__main__":
    Calculator().mainloop()
