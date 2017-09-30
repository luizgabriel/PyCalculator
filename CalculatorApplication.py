from tkinter import Tk

from views.CalculatorFrame import CalculatorFrame


class CalculatorApplication:

    def __init__(self):
        self.root = Tk()
        self.root.title("PyCalculator")
        self.main_frame = CalculatorFrame(self.root)

    def run(self):
        self.root.resizable(0, 0)
        self.main_frame.pack(expand=True)
        self.root.mainloop()
