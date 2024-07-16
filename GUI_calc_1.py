import tkinter as tk
from tkinter import *
tj = tk.Tk()
tj.title("calculator")
tj.geometry("480x640")
ac = ad = ""

Grid.rowconfigure(tj, 1, weight=4)
Grid.rowconfigure(tj, 2, weight=1)
Grid.rowconfigure(tj, 3, weight=1)
Grid.rowconfigure(tj, 4, weight=1)
Grid.rowconfigure(tj, 5, weight=1)

Grid.columnconfigure(tj, 1, weight=1)
Grid.columnconfigure(tj, 2, weight=1)
Grid.columnconfigure(tj, 3, weight=1)
Grid.columnconfigure(tj, 4, weight=1)

w = tk.Label(tj, text="", bg="cyan", font=("Arial", 30,))
w.grid(row=1, column=1, columnspan=4, sticky="nsew")


def bt1(x):
    global ac, ad
    d = {"x": "*", "^": "**"}
    if x == "=":
        w.config(text=eval(ac))
        ac = ad = str(eval(ac))
    elif x=="e":
        ad=ac=ad[:-1]
        w.config(text=ad)
    elif x in d:
        ad += x
        ac += d[x]
        w.config(text=ad)
    else:
        ac += x
        ad += x
        w.config(text=ad)


b1 = tk.Button(tj, text="1", font=("Arial", 20,),
               command=lambda: bt1("1"), padx=10, pady=10)
b1.grid(row=2, column=1, sticky="nsew")

b2 = tk.Button(tj, text="2", font=("Arial", 20,),
               command=lambda: bt1("2"), padx=10, pady=10)
b2.grid(row=2, column=2, sticky="nsew")

b3 = tk.Button(tj, text="3", font=("Arial", 20,),
               command=lambda: bt1("3"), padx=10, pady=10)
b3.grid(row=2, column=3, sticky="nsew")

b4 = tk.Button(tj, text="4", font=("Arial", 20,),
               command=lambda: bt1("4"), padx=10, pady=10)
b4.grid(row=3, column=1, sticky="nsew")

b5 = tk.Button(tj, text="5", font=("Arial", 20,),
               command=lambda: bt1("5"), padx=10, pady=10)
b5.grid(row=3, column=2, sticky="nsew")

b6 = tk.Button(tj, text="6", font=("Arial", 20,),
               command=lambda: bt1("6"), padx=10, pady=10)
b6.grid(row=3, column=3, sticky="nsew")

b7 = tk.Button(tj, text="7", font=("Arial", 20,),
               command=lambda: bt1("7"), padx=10, pady=10)
b7.grid(row=4, column=1, sticky="nsew")

b8 = tk.Button(tj, text="8", font=("Arial", 20,),
               command=lambda: bt1("8"), padx=10, pady=10)
b8.grid(row=4, column=2, sticky="nsew")

b9 = tk.Button(tj, text="9", font=("Arial", 20,),
               command=lambda: bt1("9"), padx=10, pady=10)
b9.grid(row=4, column=3, sticky="nsew")

b0 = tk.Button(tj, text="0", font=("Arial", 20,),
               command=lambda: bt1("0"), padx=10, pady=10)
b0.grid(row=5, column=1, sticky="nsew")

bp = tk.Button(tj, text="+", font=("Arial", 20,),
               command=lambda: bt1("+"), padx=5, pady=5)
bp.grid(row=2, column=4, sticky="nsew")

bm = tk.Button(tj, text="-", font=("Arial", 20,),
               command=lambda: bt1("-"), padx=5, pady=5)
bm.grid(row=3, column=4, sticky="nsew")

bx = tk.Button(tj, text="x", font=("Arial", 20,),
               command=lambda: bt1("x"), padx=5, pady=5)
bx.grid(row=4, column=4, sticky="nsew")

bd = tk.Button(tj, text="/", font=("Arial", 20,),
               command=lambda: bt1("/"), padx=5, pady=5)
bd.grid(row=5, column=4, sticky="nsew")

bex = tk.Button(tj, text="^", font=("Arial", 20,),
                command=lambda: bt1("^"), padx=10, pady=5)
bex.grid(row=5, column=3, sticky="nsew")

be = tk.Button(tj, text="=", font=("Arial", 20,),
               command=lambda: bt1("="), padx=10, pady=10)
be.grid(row=5, column=2, sticky="nsew")

bz = tk.Button(tj, text="erase", font=("Arial", 20,),
               command=lambda: bt1("e"), padx=5, pady=5)
bz.grid(row=1, column=4, sticky="ne")

tj.mainloop()
