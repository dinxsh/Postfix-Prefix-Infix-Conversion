from tkinter import ttk
from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("280x500")
root.title("Postfix Infix Prefix Conversion")

type1Var = tk.StringVar()
type2Var = tk.StringVar()

type1label = Label(root, text="Convert from", font=('Cambria', 11))
type1label.place(x=50, y=200)
type1 = ttk.Combobox(root, width = 27, textvariable = type1Var)  
type1['values'] = (' Postfix',' Prefix',' Infix')

type1.place(x=50, y=225)

type2label = Label(root, text="Convert to", font=('Cambria', 11))
type2label.place(x=50, y=265)
type2 = ttk.Combobox(root, width = 27, textvariable = type2Var)  
type2['values'] = (' Postfix',' Prefix',' Infix')

type2.place(x=50, y=285)

type1.current(1)
type2.current(2)

exp=tk.StringVar()

explabel = Label(root, text="Expression", font=('Cambria', 11))
explabel.place(x=50, y=100)
expinput = tk.Entry(root, width="30")
expinput.place(x=50, y=125)

root.mainloop()
