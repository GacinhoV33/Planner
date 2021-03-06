#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
from tkinter import messagebox


class Goal:
    def __init__(self, name: str, category: str, significance: int, start_date: str, end_date: str, time: float, curr_time:float=0.0,
                 status: str="WIP"):
        self.name = name
        self.category = category
        self.significance = significance
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.time = time
        self.curr_time = curr_time

    def delete_goal(self):
        pass

    def increase_time(self, amount:float=None):
        if amount:
            self.curr_time += amount
        else:
            self.curr_time += 1.0

    def change_status(self, status: str="DONE"):
        self.status = status

    def add_to_database(self):
        conn = sqlite3.connect("database/goals.db")

        # if value > 10:
        #     value = 10 f'{TIME["DAY"]}-{TIME["MONTH"]}-{TIME["YEAR"]}'
        # elif value < 0:
        #     value = 0
        c = conn.cursor()
        c.execute("""INSERT INTO main_goals VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (self.name,
                                                                         self.category, self.significance,
                                                                         self.start_date, self.end_date, self.time, self.curr_time, self.status
                                                                         )
                  )
        conn.commit()
        conn.close()
        messagebox.showinfo("Goals", "Record successfully added to database")