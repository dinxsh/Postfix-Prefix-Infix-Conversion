from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Postfix Infix Prefix Conversion")

explabel = Label(root, text="Expression")
explabel.place(x=50, y=300)
expinput = Text(root)
explabel.place(x=50, y=320)

root.mainloop()
