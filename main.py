from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser
# user-defined modules below
import prefix
import postfix
import infix

root = Tk()
root.resizable(0,0)
root.geometry("280x500")
root.title("Postfix Infix Prefix Conversion") 

menubar = Menu(root)
  
Github = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Github', menu = Github)
Github.add_command(label ='View Repo', command = lambda:webbrowser.open("https://github.com/blaze-pvt/Postfix-Prefix-Infix-Conversion"))
Github.add_command(label ='Contribute', command = lambda:webbrowser.open("https://github.com/blaze-pvt/Postfix-Prefix-Infix-Conversion"))
Github.add_command(label ='Open PR', command = lambda:webbrowser.open("https://github.com/blaze-pvt/Postfix-Prefix-Infix-Conversion/pulls"))

info = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Info', menu = info)
info.add_command(label ='Help', command = lambda:messagebox.showinfo("Help", "to report any complains kindly email me at blaze.mehh@gmail.com"))
info.add_command(label ='About Developer', command = lambda:messagebox.showinfo("About Developer", "Hi, I'm Blaze\nA 13 y/o web developer and tech enthusiast\nmail me at blaze.mehh@gmail.com"))
info.add_command(label ='About Project', command = lambda:messagebox.showinfo("About Project", "Posfix Prefix Infix Converter"))
  
AppLabel = Label(root, text="Postfix Infix Prefix Converter", font=('Cambria', 12))
AppLabel.place(x=40, y=15)

AppSeparator = ttk.Separator(root, orient='vertical')
AppSeparator.place(x=40, y=30) 

type1Var = tk.StringVar()
type2Var = tk.StringVar()

type1label = Label(root, text="Convert from", font=('Cambria', 11))
type1label.place(x=50, y=200)
type1 = ttk.Combobox(root, width = 27, textvariable = type1Var)  
type1['values'] = ('Postfix',' Prefix',' Infix')

type1.place(x=50, y=225)

type2label = Label(root, text="Convert to", font=('Cambria', 11))
type2label.place(x=50, y=265)
type2 = ttk.Combobox(root, width = 27, textvariable = type2Var)  
type2['values'] = ('Postfix',' Prefix',' Infix')

type2.place(x=50, y=285)

type1.current(1)
type2.current(2)

exp=tk.StringVar()

explabel = Label(root, text="Expression", font=('Cambria', 11))
explabel.place(x=50, y=100)
expinput = tk.Entry(root, width="30")
expinput.place(x=50, y=125)

def Convert():
    if (type1Var.get()==type2Var.get()):
        print("Both converting values can't be same!")
    if (str(type1Var.get())=="Postfix"):
        if (str(type2Var.get())=="Prefix"):
            print("Postfix to Prefix")
        if (type2Var.get()=="Infix"):
            print("Postfix to Infix")

    elif (type1Var.get()=="Prefix"):
        if (type2Var.get()=="Postfix"):
            print("Prefix To Postfix")
        if (type2Var.get()=="Infix"):
            print("Prefix To Infix")

    elif (type1Var.get()=="Postfix"):
        if (type2Var.get()=="Prefix"):
            print("Postfix to Prefix")
        if (type2Var.get()=="Infix"):
            print("Postfix to Infix")


submitbutton = ttk.Button(root, command=Convert, text="Convert")
submitbutton.place(x=50, y=340)

root.config(menu = menubar)
root.mainloop()
