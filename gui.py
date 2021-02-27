from tkinter import *
import csv
master = Tk()


def var_states():  # ADD YOUR COMBO CODE HERE DONT FORGET, THE CSV FILE ALSO IS IN THIS COLAB, THE PROGRAM DOESNT RUN HERE, USE PYCHARM
    
    filename = "MCD database.csv"
    # opening the file using "with"
    # statement
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            print(line)

master.geometry("300x300")

Label(master, text="Lunch Launcher").grid(row=0, sticky=S)

Label(master, text="Do you want a meal ?").grid(row=2, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Yes", variable=var1).grid(row=3, column=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text="No", variable=var2).grid(row=3, column=1, sticky=W)

Label(master, text="Do you want Sides ? ").grid(row=5, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Yes", variable=var3).grid(row=6, column=0, sticky=W)
var4 = IntVar()
Checkbutton(master, text="No", variable=var4).grid(row=6, column=1, sticky=W)

Label(master, text="Do you want a burger ? ").grid(row=7, sticky=W)
var5 = IntVar()
Checkbutton(master, text="Yes", variable=var5).grid(row=8, column=0, sticky=W)
var6 = IntVar()
Checkbutton(master, text="No", variable=var6).grid(row=8, column=1, sticky=W)

Label(master, text="Do you want a Drink ? ").grid(row=9, sticky=W)
var7 = IntVar()
Checkbutton(master, text="Yes", variable=var7).grid(row=10, column=0, sticky=W)
var8 = IntVar()
Checkbutton(master, text="No", variable=var8).grid(row=10, column=1, sticky=W)

Button(master, text='Quit', command=master.quit).grid(row=13, column=3, sticky=W, pady=4)
Button(master, text='Find the best Combos ? ', command=var_states).grid(row=13, column=0, sticky=W, pady=4)
mainloop()

