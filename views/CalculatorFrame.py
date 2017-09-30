import tkinter as tk

from presenters.CalculatorPresenter import CalculatorPresenter


class CalculatorFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.presenter = CalculatorPresenter(self)
        self.initialize_components()

    def initialize_components(self):
        self.number_text = tk.StringVar()
        self.number = tk.Label(self, textvariable=self.number_text, bg="white", font=("Courier", 30), anchor="e")\
            .grid(row=0, columnspan=4, ipadx=10, ipady=5, sticky=tk.W + tk.E)

        self.calculator_btns = {
            0: self.create_button("0", 4, 1),
            1: self.create_button("1", 3, 0),
            2: self.create_button("2", 3, 1),
            3: self.create_button("3", 3, 2),
            4: self.create_button("4", 2, 0),
            5: self.create_button("5", 2, 1),
            6: self.create_button("6", 2, 2),
            7: self.create_button("7", 1, 0),
            8: self.create_button("8", 1, 1),
            9: self.create_button("9", 1, 2),
            "/": self.create_button("/", 1, 3),
            "*": self.create_button("*", 2, 3),
            "-": self.create_button("-", 3, 3),
            "+": self.create_button("+", 4, 3),
            "=": self.create_button("=", 4, 2),
            ".": self.create_button(".", 4, 0),
        }

        for key, btn in self.calculator_btns.items():
            def _click(n):
                return lambda e: self.presenter.on_click_calculator_btn(n)
            btn.bind("<Button-1>", _click(key))

        self.presenter.on_create()

    def create_button(self, text, row, column):
        button = tk.Button(self, text=text, width=3, height=2, font=("Courier", 20))
        button.grid(row=row, column=column)
        return button

    def set_number(self, formatted_number):
        self.number_text.set(str(formatted_number))
