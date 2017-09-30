from presenters.BasePresenter import BasePresenter


class CalculatorPresenter(BasePresenter):

    symbols = ["/", "*", "-", "+", "=", "."]

    def on_create(self):
        self.view.set_number(0)
        self._current_number = 0
        self._expression = ""
        self.decimal = 1

    def on_click_calculator_btn(self, key):
        if key in self.symbols:
            self.process_symbol(key)
        else:
            self.process_number(int(key))

    def process_symbol(self, symbol: str):
        if symbol == "=":
            self._expression += str(self._current_number) + " "

            self._current_number = self.get_result()
            self.display()

            self._expression = ""
            self.decimal = 1

        elif symbol == ".":
            self.display(self.decimal == 1)
            if self.decimal == 1:
                self.decimal *= 0.1
        else:
            self._expression += str(self._current_number) + " " + symbol + " "

            self._current_number = 0
            self.decimal = 1

    def process_number(self, number: int):

        if self.decimal < 1:
            self._current_number += number * self.decimal
            self.decimal *= 0.1
        else:
            self._current_number *= 10
            self._current_number += number

        self.display()

    def get_result(self) -> int:
        return int(eval(self._expression))

    def display(self, decimal=False):
        display = '{0:g}'.format(self._current_number)

        if decimal:
            display += "."

        self.view.set_number(display)