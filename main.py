from tkinter import *
import csv

master = Tk()

import csv


def var_states():
    with open('MCD database.csv', newline="") as f:
        reader = csv.reader(f)
        d = list(reader)

        if var9.get() == 1:
            if var1.get() == 1 and var3.get() == 1:
                print("The best combo is ", d[4][0], 'and', d[3][2])
                print("It will cost Rs.", int(d[4][1]) + int(d[3][3]))
                print()
                print("The cheapest combo is ", d[3][0], 'and', d[7][2])
                print("It will cost Rs.", int(d[3][1]) + int(d[7][3]))
                print()
                print("The Costliest combo is ", d[2][0], 'and', d[3][2])
                print("It will cost Rs.", int(d[2][1]) + int(d[3][3]))

            elif var3.get() == 1 and var7.get() == 1:
                print("The best combo is ", d[5][2], 'and', d[7][4])
                print("It will cost Rs.", int(d[5][3]) + int(d[7][5]))
                print()
                print("The cheapest combo is ", d[7][2], 'and', d[1][4])
                print("It will cost Rs.", int(d[7][3]) + int(d[1][5]))
                print()
                print("The Costliest combo is ", d[3][2], 'and', d[6][4])
                print("It will cost Rs.", int(d[3][3]) + int(d[6][5]))

            elif var5.get() == 1 and var7.get() == 1:
                print("The best combo is ", d[4][6], 'and', d[5][4])
                print("It will cost Rs.", int(d[4][7]) + int(d[5][5]))
                print()
                print("The cheapest combo is ", d[3][0], 'and', d[1][4])
                print("It will cost Rs.", int(d[3][1]) + int(d[1][5]))
                print()
                print("The Costliest combo is ", d[2][6], 'and', d[6][4])
                print("It will cost Rs.", int(d[2][7]) + int(d[6][5]))

            elif var5.get() == 1 and var3.get() == 1:
                print("The best combo is ", d[1][6], 'and', d[6][2])
                print("It will cost Rs.", int(d[1][7]) + int(d[6][3]))
                print()
                print("The cheapest combo is ", d[3][6], 'and', d[7][2])
                print("It will cost Rs.", int(d[3][7]) + int(d[7][3]))
                print()
                print("The Costliest combo is ", d[2][6], 'and', d[3][2])
                print("It will cost Rs.", int(d[2][7]) + int(d[3][3]))


        elif var10.get() == 1:
            if var1.get() == 1 and var3.get() == 1:
                print("The best combo is ", d[7][0], 'and', d[1][2])
                print("It will cost Rs.", int(d[7][1]) + int(d[1][3]))
                print()
                print("The cheapest combo is ", d[6][0], 'and', d[7][2])
                print("It will cost Rs.", int(d[6][1]) + int(d[7][3]))
                print()
                print("The Costliest combo is ", d[5][0], 'and', d[2][2])
                print("It will cost Rs.", int(d[5][1]) + int(d[2][3]))

            elif var3.get() == 1 and var7.get() == 1:
                print("The best combo is ", d[1][2], 'and', d[2][4])
                print("It will cost Rs.", int(d[1][3]) + int(d[2][5]))
                print()
                print("The cheapest combo is ", d[7][2], 'and', d[1][4])
                print("It will cost Rs.", int(d[7][3]) + int(d[1][5]))
                print()
                print("The Costliest combo is ", d[2][2], 'and', d[6][4])
                print("It will cost Rs.", int(d[2][3]) + int(d[6][5]))


            elif var5.get() == 1 and var7.get() == 1:
                print("The best combo is ", d[7][6], 'and', d[3][4])
                print("It will cost Rs.", int(d[7][7]) + int(d[3][5]))
                print()
                print("The cheapest combo is ", d[6][6], 'and', d[1][4])
                print("It will cost Rs.", int(d[6][7]) + int(d[1][5]))
                print()
                print("The Costliest combo is ", d[5][6], 'and', d[6][4])
                print("It will cost Rs.", int(d[5][7]) + int(d[6][5]))

            elif var5.get() == 1 and var3.get() == 1:
                print("The best combo is ", d[7][6], 'and', d[4][2])
                print("It will cost Rs.", int(d[7][7]) + int(d[4][3]))
                print()
                print("The cheapest combo is ", d[6][6], 'and', d[7][2])
                print("It will cost Rs.", int(d[6][7]) + int(d[7][3]))
                print()
                print("The Costliest combo is ", d[5][6], 'and', d[2][2])
                print("It will cost Rs.", int(d[5][7]) + int(d[2][3]))


master.geometry("300x300")

Label(master, text="LunchLauncher").grid(row=0, sticky=S)

Label(master, text="Do you want Veg or Non-Veg ?").grid(row=2, sticky=W)
var9 = IntVar()
Checkbutton(master, text="Veg", variable=var9).grid(row=3, column=0, sticky=W)
var10 = IntVar()
Checkbutton(master, text="Non Veg", variable=var10).grid(row=3, column=1, sticky=W)

Label(master, text="Do you want a meal ?").grid(row=4, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Yes", variable=var1).grid(row=5, column=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text="No", variable=var2).grid(row=5, column=1, sticky=W)

Label(master, text="Do you want Sides ? ").grid(row=6, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Yes", variable=var3).grid(row=7, column=0, sticky=W)
var4 = IntVar()
Checkbutton(master, text="No", variable=var4).grid(row=7, column=1, sticky=W)

Label(master, text="Do you want a burger ? ").grid(row=8, sticky=W)
var5 = IntVar()
Checkbutton(master, text="Yes", variable=var5).grid(row=9, column=0, sticky=W)
var6 = IntVar()
Checkbutton(master, text="No", variable=var6).grid(row=9, column=1, sticky=W)

Label(master, text="Do you want a Drink ? ").grid(row=10, sticky=W)
var7 = IntVar()
Checkbutton(master, text="Yes", variable=var7).grid(row=11, column=0, sticky=W)
var8 = IntVar()
Checkbutton(master, text="No", variable=var8).grid(row=11, column=1, sticky=W)

Button(master, text='Quit', command=master.quit).grid(row=14, column=3, sticky=W, pady=4)
Button(master, text='Find the best Combos ? ', command=var_states).grid(row=14, column=0, sticky=W, pady=4)
mainloop()




