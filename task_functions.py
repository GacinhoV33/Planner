#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
# import timeit
import sqlite3
""" 
This module contains functions that generate tasks report in pdf 
It also contains function that scrapping through database and automatically update time of tasks 
"""
#TODO 1: Check time of operation -> It may be big due to 3/4 loops
#     2: Implement execptions to avoid situation of empty db etc.
#     3: GenerateReport and DeleteOldDatabases needs to be implemented 

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
    # print(goals_data)
    c_goals.close()

    hours_data = list()
    """ STEP 2 """
    for file_name in os.listdir('database/'):
        if file_name != "goals.db":
            # print(file_name)
            conn_hours = sqlite3.connect(f'database/{file_name}')
            c_hours = conn_hours.cursor()
            c_hours.execute(""" SELECT * FROM weekplanner""")
            hours_data.append(c_hours.fetchall())
            c_hours.close()
            # print(hours_data)
            # c.commit()


    """ Getting names of all tasks """
    goal_names = [goal[0] for goal in goals_data]
    for goal_name in goal_names:
        for day in hours_data:
            for hour in day:
                if goal_name in hour:
                    print("I've found that")


# print(timeit.timeit(UpdateTasksTime()))
UpdateTasksTime()