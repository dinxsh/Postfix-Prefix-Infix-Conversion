import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("400x500")
root.title("Postfix Infix Prefix Conversion")



exp=tk.StringVar()

explabel = Label(root, text="Expression", font=('Cambria', 11))
explabel.place(x=50, y=100)
expinput = tk.Entry(root, width="30")
expinput.place(x=50, y=125)

root.mainloop()
