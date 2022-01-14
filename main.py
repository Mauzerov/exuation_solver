import tkinter as tk
from tkinter.messagebox import showinfo
from Equation import Equation


class App(tk.Tk):
    def __init__(this, title=""):
        super().__init__()
        this.title = title
        this.calc = tk.Button(this, command=this.calculate, text="Click Me!")

        this.first = Equation(this)
        this.first.pack()

        this.second = Equation(this)
        this.second.pack()

        this.third = Equation(this)
        this.third.pack()

        this.calc.pack()

        this.answer = tk.StringVar()
        this.answer_label = tk.Label(textvariable=this.answer)
        this.answer_label.pack()


    def run(this):
        this.mainloop()

    def calculate(this):
        x1, x2, x3 = this.first.values, this.second.values, this.third.values
        assert x1 and x2 and x3, "Unable To Parse With Zeros"
        # nfl - kgn + ogj - old - pfj + pkg
        # ---------------------------------
        # rfl - kgr + gmo - lho - fmp + khp
        c =\
            (
                (x3.v * x1.a * x2.b) - (x2.a * x1.b * x3.v) + (x1.b * x2.v * x3.a) -
                (x3.a * x2.b * x1.v) - (x3.b * x1.a * x2.v) + (x3.b * x2.a * x1.v)
            ) /\
            (
                (x3.c * x1.a * x2.b) - (x2.a * x1.b * x3.c) + (x1.b * x2.c * x3.a) -
                (x3.a * x1.c * x2.b) - (x3.b * x1.a * x2.c) + (x3.b * x2.a * x1.c)
            )
        # fj - kd + c * (kh - fm)
        # -----------------------
        # fl - kg
        b =\
            (
                (x1.a * x2.v - x2.a * x1.v) + (c * (x2.a * x1.c - x1.a * x2.c))
            ) /\
            (
                x1.a * x2.b - x2.a * x1.b
            )
        # d - g*b - h*c
        # -------------
        # f
        a =\
            (
               x1.v - x1.b * b - x1.c * c
            ) / x1.a

        this.answer.set(f"{a=}, {b=}, {c=}")


if __name__ == '__main__':
    App("Calculate Equations").run()
