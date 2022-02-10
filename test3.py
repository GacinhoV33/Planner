#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

from datetime import datetime, date
today = date.today().strftime("%d/%m/%Y %H:%M:%S")

D_name = str(datetime.now())
print(today)
# ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('500x500')
# ws['bg'] = '#AC99F2'
#
# game_frame = Frame(ws)
# game_frame.pack()
#
# # scrollbar
# game_scroll = Scrollbar(game_frame)
# game_scroll.pack(side=RIGHT, fill=Y)
#
# game_scroll2 = Scrollbar(game_frame, orient='horizontal')
# game_scroll2.pack(side=BOTTOM, fill=X)
#
# my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)
#
# my_game.pack()
#
# game_scroll.config(command=my_game.yview)
# game_scroll.config(command=my_game.xview)
#
# # define our column
#
# my_game['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')
#
# # format our column
# my_game.column("#0", width=0, stretch=NO)
# my_game.column("player_id", anchor=CENTER, width=80)
# my_game.column("player_name", anchor=CENTER, width=80)
# my_game.column("player_Rank", anchor=CENTER, width=80)
# my_game.column("player_states", anchor=CENTER, width=80)
# my_game.column("player_city", anchor=CENTER, width=80)
#
# # Create Headings
# my_game.heading("#0", text="", anchor=CENTER)
# my_game.heading("player_id", text="Id", anchor=CENTER)
# my_game.heading("player_name", text="Name", anchor=CENTER)
# my_game.heading("player_Rank", text="Rank", anchor=CENTER)
# my_game.heading("player_states", text="States", anchor=CENTER)
# my_game.heading("player_city", text="States", anchor=CENTER)
#
# # add data
# my_game.insert(parent='', index='end', iid=0, text='',
#                values=('1', 'Ninja', '101', 'Oklahoma', 'Moore'))
# my_game.insert(parent='', index='end', iid=1, text='',
#                values=('2', 'Ranger', '102', 'Wisconsin', 'Green Bay'))
# my_game.insert(parent='', index='end', iid=2, text='',
#                values=('3', 'Deamon', '103', 'California', 'Placentia'))
# my_game.insert(parent='', index='end', iid=3, text='',
#                values=('4', 'Dragon', '104', 'New York', 'White Plains'))
# my_game.insert(parent='', index='end', iid=4, text='',
#                values=('5', 'CrissCross', '105', 'California', 'San Diego'))
# my_game.insert(parent='', index='end', iid=5, text='',
#                values=('6', 'ZaqueriBlack', '106', 'Wisconsin', 'TONY'))
# my_game.insert(parent='', index='end', iid=6, text='',
#                values=('7', 'RayRizzo', '107', 'Colorado', 'Denver'))
# my_game.insert(parent='', index='end', iid=7, text='',
#                values=('8', 'Byun', '108', 'Pennsylvania', 'ORVISTON'))
# my_game.insert(parent='', index='end', iid=8, text='',
#                values=('9', 'Trink', '109', 'Ohio', 'Cleveland'))
# my_game.insert(parent='', index='end', iid=9, text='',
#                values=('10', 'Twitch', '110', 'Georgia', 'Duluth'))
# my_game.insert(parent='', index='end', iid=10, text='',
#                values=('11', 'Animus', '111', 'Connecticut', 'Hartford'))
# my_game.insert(parent='', index='end', iid=11, text='',
#                values=('12', 'Trink', '112', 'Ohio', 'Cleveland'))
# my_game.insert(parent='', index='end', iid=12, text='',
#                values=('13', 'Twitch', '113', 'Georgia', 'Duluth'))
# my_game.insert(parent='', index='end', iid=113, text='',
#                values=('14', 'Animus', '114', 'Connecticut', 'Hartford'))
# my_game.pack()
#
# ws.mainloop()

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
# from tkcalendar import Calendar
# from tkinter import *
#
# root = Tk()
#
# root.geometry("800x800")
#
# cal = Calendar(root, selectmode='day', year=2020, month=5, day=22)
# cal.pack(pady=20)
# print(cal.get_date().split('/'))
# root.mainloop()