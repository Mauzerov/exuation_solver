import tkinter as tk
from decimal import Decimal


class Equation(tk.PanedWindow):
    def __init__(this, master):
        super().__init__(master)

        this.value = tk.Entry(this)
        this.a = tk.Entry(this)
        this.b = tk.Entry(this)
        this.c = tk.Entry(this)

        this.label_eq = tk.Label(this, text=" = (")
        this.label_a = tk.Label(this, text=") + (")
        this.label_b = tk.Label(this, text=") + (")
        this.label_c = tk.Label(this, text=")")

        this.value.pack(side=tk.LEFT)
        this.label_eq.pack(side=tk.LEFT)
        this.a.pack(side=tk.LEFT)
        this.label_a.pack(side=tk.LEFT)
        this.b.pack(side=tk.LEFT)
        this.label_b.pack(side=tk.LEFT)
        this.c.pack(side=tk.LEFT)
        this.label_c.pack(side=tk.LEFT)

    @property
    def values(self):
        value = self.value.get()
        a = Decimal(int(self.a.get()))
        b = Decimal(int(self.b.get()))
        c = Decimal(int(self.c.get()))
        assert a * a + b * b + c * c > 0, "At Least One Of Values Has To Be Set"
        return Eq({
            'v': value, 'a': a, 'b': b, 'c': c
        })


class Eq:
    a: int
    b: int
    c: int
    v: int

    def __init__(self, d: dict):
        for key, val in d.items():
            self.__setattr__(key, int(val))
