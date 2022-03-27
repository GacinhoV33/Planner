#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sqlite3

""" 
This module contains functions that generate tasks report in pdf 
It also contains function that scrapping through database and automatically update time of tasks 
"""
#TODO 1: Check time of operation -> It may be big due to 3/4 loops
#     2: Implement execptions to avoid situation of empty db etc.
#     3: GenerateReport and DeleteOldDatabases needs to be implemented
#     4: Implement mechanism that run UpdateTasksTime each night, and not repeat days in counting

def GenerateReport():
    pass

def DeleteOldDatabases():
    pass


def UpdateTasksTime():
    """
    Function steps:
    1) Connect to taks Database
    2) Connect to hour Database
    3) Get data from databases
    4) Search for hours with names of tasks
    5) Update time according to findings
    6) Commit both Databases
    7) Close databases
    """
    """ STEP 1 """
    conn = sqlite3.connect('database/goals.db')
    c_goals = conn.cursor()
    c_goals.execute("""SELECT * FROM main_goals""")
    goals_data = c_goals.fetchall()

    hours_data = list()
    """ STEP 2 """
    for file_name in os.listdir('database/'):
        database / {TIME['MONTH']} - {TIME['WEEK']} - {day}.db
        if file_name != "goals.db":
            conn_hours = sqlite3.connect(f'database/{file_name}')
            c_hours = conn_hours.cursor()
            c_hours.execute(""" SELECT * FROM weekplanner""")
            hours_data.append(c_hours.fetchall())
            c_hours.close()

    TaskDictUpdate = dict()
    """ Getting names of all tasks """
    goal_names = [goal[0] for goal in goals_data]
    """ STEP 4 """
    for goal_name in goal_names:
        for day in hours_data:
            for hour in day:
                if goal_name in hour:
                    if '/' in hour:
                        try:
                            TaskDictUpdate[goal_name] += 0.5 # if hour is splitted
                        except:
                            TaskDictUpdate[goal_name] = 0.5
                    else:
                        try:
                            TaskDictUpdate[goal_name] += 1 # if there's one hour for task
                        except:
                            TaskDictUpdate[goal_name] = 1
    """ Updating DataBase """
    """ STEP 5 """
    for key, value in TaskDictUpdate.items():
       c_goals.execute("""UPDATE main_goals SET curr_time = ? + curr_time
                    WHERE name = ?""",
        (float(value), key))
    """ STEP 6 """
    conn.commit() # commiting changes in hours
    """ STEP 7 """
    c_goals.close()


if __name__ == "__main__":
    UpdateTasksTime()