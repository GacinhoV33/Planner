#!/usr/bin/python
# -*- coding: utf-8 -*-
# from tkinter import *
#
#
#
# root = Tk()
# mymenu1 = MyOptionMenu(root, 'Select status', 'a','b','c')
# mymenu2 = MyOptionMenu(root, 'Select another status', 'd','e','f')
# mymenu1.pack()
# mymenu2.pack()
# root.mainloop()
# master = Tk()
#
# variable = StringVar(master)
# variable.set("one") # default value
#
# w = OptionMenu(master, variable, "one", "two", "three")
# w.pack()
#
# mainloop()
from tkcalendar import Calendar
from tkinter import *

root = Tk()

root.geometry("800x800")

cal = Calendar(root, selectmode='day', year=2020, month=5, day=22)
cal.pack(pady=20)
print(cal.get_date().split('/'))
root.mainloop()