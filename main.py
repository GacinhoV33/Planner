#!/usr/bin/python
# -*- coding: utf-8 -*-


#TODO DATABASE for input
#TODO AUTOMATIC TASKS ALOCATION
#TODO
import os
from tkinter import *
from settings import X_size, Y_size, monitor_width, monitor_height
from PIL import Image, ImageTk
import sqlite3
from datetime import datetime
from datetime import date
from tkinter_custom_button import TkinterCustomButton
from tkinter import messagebox, ttk
from source import get_key
from tkcalendar import Calendar
from Goal import Goal
from CustomedOptionMenu import CustomedOptionMenu

goals_data_db = None
selection_of_key_sort = 2
V = datetime.now().strftime("%V")
today = date.today().strftime("%d/%m/%Y %H:%M:%S")

D = today[:2]
M = today[3:5]
Y = today[6:10]
H = today[11:19]
D_name = str(datetime.now().strftime("%A"))

"""Dictionary which contains data and time. It is taken and updated when program starts"""
TIME = {"HOUR" : H,
        "DAY" : D_name,
        "YEAR" : Y,
        "WEEK" : V,
        "MONTH" : M,
        "DAY_NUMB": D
        }

DAY_DICT = {"0" : "Monday",
            "1" : "Tuesday",
            "2" : "Wednesday",
            "3" : "Thursday",
            "4" : "Friday",
            "5" : "Saturday",
            "6" : "Sunday"}

DAY_DICT_INV = {v: k for k, v in DAY_DICT.items()} # Inverted Dict of Days

"""Lists needed to dropwdown menus"""
lst_of_categories = ['Sport', 'Cooking', 'Learning', 'Studies', 'Work', 'Fun', 'Workout']
lst_of_statuses = ['Work in Progress', 'Done', 'Blocked', 'TODO', 'Retaken']

""" SETTINGS """
table_pos_x = 200
table_pos_y = 100
table_width = 160
table_height = 30
tp_butt_width = 40
button_pos_y = 35
table_width_day = 891
st_x = X_size//2
st_y = Y_size//1.1
save_x = X_size//1.2
save_y = Y_size//1.1
goals_x = X_size//2.5
goals_y = Y_size//1.1
goals_x_size = 1000
goals_y_size = 700
short_tasks_x_size = 720
short_tasks_y_size = 480
screen_pos_x = monitor_width//2 - X_size //2
screen_pos_y = monitor_height//2 - Y_size//2
screen_pos_x_goals = monitor_width//2 - goals_x_size
screen_pos_y_goals = monitor_height//2 - goals_y_size
"""
FLAG RESPONSIBLE FOR DISPLAY
1 -> All days
2 -> Specific day
3 -> Weekend
4 -> Week
"""
table_look_flag = 1

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

"""TOP BUTTONS COLORS """
bg_color = ("#68D0BC", "#EBAEAC", "#51638E", "#E26AFF", "#FFA500", "#3CB371", "Pink")
fg_color = ("#002732", "#FFFFD6", "#FFE700", "#EEEEEE", "#3C3C3C", "#FFFFFF", "White")

""" END SETTINGS """


class Table:

    def __init__(self, root, data_from_db):
        self.all_entries = [[None for _ in range(18)] for _ in range(7)]
        self.data_from_db = data_from_db # get data from parameters and update
        self.data_dict = {}
        """
        Code responsible for creating table 7x18
        if you reach to [i][-1][j]  -1 means that you want to take the last commit
        If everything will be implemented good, that will mean that you take data from last weak
        """

        for i in range(7):
            self.label = Label(root, text=f'{days[i]}', font=('Arial', 16))
            self.label.place(x=table_pos_x + table_width//3.52 + i*(table_width+5) - len(days[i])*2, y=table_pos_y-table_height)
            for j in range(18):
                self.all_entries[i][j] = Entry(root, fg=fg_color[i], bg=bg_color[i], font=('Helvetica', 16))
                self.all_entries[i][j].place(x=table_pos_x + i*(table_width+5), y=table_pos_y+j*(table_height+5), width=table_width, height=table_height)
                self.all_entries[i][j].insert(END, self.data_from_db[i][-1][j]) # here might be problems with bigger commits

    def get_data(self):
        """
        THIS FUNCTION TAKES ALL DATA FROM ENTRIES AND STORE IT IN DICTIONARY
        i -> day
        j -> hour   (j = 0 <===> hour = 6;00-7;00)
        """
        for i in range(7):
            for j in range(18):
                self.data_dict[f'{i}{j}'] = self.all_entries[i][j]

    def write_data_from_db_into_entries(self): #NOT USED IN PROGRAMM - think about deleting it
        try:
                conn = sqlite3.connect(f"database/{TIME['MONTH']}-{TIME['WEEK']}")
                c = conn.cursor()
                pon_data = [self.data_from_db[f'0{i}'] for i in range(18)]
                c.executemany("INSERT INTO weekplanner VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", pon_data)
                #TODO make it more transparent and cleaner
                conn.commit()
                conn.close()

        except Exception as e:
                messagebox.showerror(title="Error", message=f"Error: {e}.\n Planner couldn't take data from database!!!")

    #TODO end rest of dayss/ change it into iterable form

    def write_data_from_entries_into_db(self, autosave_flag=False):
        try:
            self.get_data()
            for n, day in enumerate(days):
                #TODO
                day_entry = tuple([str(hour.get()) for hour in self.all_entries[n]])

                conn = sqlite3.connect(f"database/{TIME['MONTH']}-{TIME['WEEK']}-{day}.db")
                c = conn.cursor()

                c.execute("""INSERT INTO weekplanner VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", day_entry)
                conn.commit()
                conn.close()
            if not autosave_flag:
                messagebox.showinfo(title="Save", message="Database succesfully updated")
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Error: {e}.\nDatabase update failed!!!")

    def get_info_about_time(self,):
        """
        This function takes information about how much time you spend on specific task
        User don't need to make it, it automatically runs when application starts, and update database
        1. Take name of every goal in database and put it one list
        2. Take current data, and data of creating goal
        3. For every week from step 2:
            - Get whole data from every hour
            - If name of goal is mention in specific hour increment curr_time
            - If / found in name incerement by 0.5
            -
        4. Update database
        :return:
        """
        #TODO
        pass

class TableDay:

    def __init__(self, root, day_open, data_from_db):
        self.data_from_db = data_from_db
        self.day_open = day_open
        self.all_entries = [0 for _ in range(18)]
        self.day_n = int(get_key(DAY_DICT, day_open))
        self.data_dict = {}
        print(self.data_from_db)
        for i in range(18):
            self.all_entries[i] = Entry(root, fg=fg_color[self.day_n], bg=bg_color[self.day_n],
                           font=('Arial', 16, 'bold'))
            self.all_entries[i].place(x=table_pos_x, y=table_pos_y + i * (table_height + 5),
                         width=table_width_day, height=table_height)
            self.all_entries[i].insert(END, self.data_from_db[i])

    def get_data(self):
        for i in range(18):
            self.data_dict[f'{i}'] = self.all_entries[i]

    def write_data_from_entries_into_db(self):
        try:
            self.get_data()
            day_entry = tuple([str(hour.get()) for hour in self.all_entries])

            conn = sqlite3.connect(f"database/{TIME['MONTH']}-{TIME['WEEK']}-{self.day_open}.db")
            c = conn.cursor()

            c.execute("""INSERT INTO weekplanner VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", day_entry)
            conn.commit()
            conn.close()
            messagebox.showinfo(title="Save", message="Database succesfully updated")
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Error: {e}.\nDatabase update failed!!!")

    def write_data_from_db_into_entries(self): #NOT USED IN PROGRAMM - think about deleting it or reformating
        conn = sqlite3.connect(f"database/{TIME['MONTH']}-{TIME['WEEK']}-{self.day_open}")
        c = conn.cursor()
        for entry in self.all_entries:
            # entry.insert
            pass
            #TODO GET SHIT FROM DB FROM ONE DAY (Y) (Y) (Y) 


class TableWeekend:
    def __init__(self, root, data_from_db_week):
        self.data_from_db_week = data_from_db_week
        self.all_entries = [[None for _ in range(18)] for _ in range(2)]
        self.data_dict = {}
        print(len(data_from_db_week))
        for i in range(2):
            for j in range(18):
                self.all_entries[i][j] = Entry(root, fg=fg_color[5+i], bg=bg_color[5+i], font=('Helvetica', 16))
                self.all_entries[i][j].place(x=table_pos_x + i*(table_width_day//2+20), y=table_pos_y + j*(table_height+5), width=table_width_day//2, height=table_height)
                self.all_entries[i][j].insert(END, self.data_from_db_week[i][-1][j])
                """ UWAGA - W liście siedzi krotka, dlatego trzeba użyć 0/1"""

    def get_data(self):
        """
        THIS FUNCTION TAKES ALL DATA FROM ENTRIES AND STORE IT IN DICTIONARY
        i -> day
        j -> hour   (j = 0 <===> hour = 6;00-7;00)
        """
        for i in range(2):
            for j in range(18):
                self.data_dict[f'{i}{j}'] = self.all_entries[i][j]

    def write_data_from_entries_into_db(self):
        try:
            self.get_data()
            for n, day_w in enumerate(days[5:7], 0):
                # TODO
                print(n, day_w)
                day_entry = tuple([str(hour.get()) for hour in self.all_entries[n]])
                print(day_entry)
                conn = sqlite3.connect(f"database/{TIME['MONTH']}-{TIME['WEEK']}-{day_w}.db")
                c = conn.cursor()

                c.execute("""INSERT INTO weekplanner VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", day_entry)
                conn.commit()
                conn.close()
            messagebox.showinfo(title="Save", message="Database succesfully updated")
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Error: {e}.\nDatabase update failed!!!")


class HourLabels:

    def __init__(self, root):

        for i in range(18):
            self.label = Label(root, font=('Arial', 16), text=f'{i + 6}:00 - {i+7}:00')
            self.label.place(x=30, y=table_pos_y + i*(table_height + 5))


def day_to_numb(day_number):
    if len(day_number) == 2:
        return day_number
    elif len(day_number) == 1:
        return "0"+day_number
    else:
        raise ValueError()


def Openday(n_button, root):
    """ HELP FUNCTION -> AFTER IMPLEMENTING TOP BUTTONS DELETE IT ! """
    print(n_button)
    root.destroy()
    if n_button == "Weekend":
        main_disp(3)
    elif n_button is None:
        main_disp(1)
    else:
        main_disp(2, int(n_button))


class TopButtons:

    def __init__(self, root):
        self.all_buttons = list()

        """MONDAY"""
        self.monday = TkinterCustomButton(text=f"{days[0]}", corner_radius=10, command=lambda: Openday(0, root))
        self.monday.place(x=table_pos_x - 100 + 0 * (tp_butt_width + 100), y=button_pos_y, anchor=CENTER)
        """TUESDAY"""
        self.tuesday = TkinterCustomButton(text=f"{days[1]}", corner_radius=10, command=lambda: Openday(1, root))
        self.tuesday.place(x=table_pos_x - 100 + 1 * (tp_butt_width + 100), y=button_pos_y, anchor=CENTER)
        """WEDNESDAY"""
        self.wednesday = TkinterCustomButton(text=f"{days[2]}", corner_radius=10, command=lambda: Openday(2, root))
        self.wednesday.place(x=table_pos_x - 100 + 2 * (tp_butt_width + 100), y=button_pos_y, anchor=CENTER)
        """THURSDAY"""
        self.thursday = TkinterCustomButton(text=f"{days[3]}", corner_radius=10, command=lambda: Openday(3, root))
        self.thursday.place(x=table_pos_x - 100 + 3 * (tp_butt_width + 100), y=button_pos_y, anchor=CENTER)
        """FRIDAY"""
        self.friday = TkinterCustomButton(text=f"{days[4]}", corner_radius=10, command=lambda: Openday(4, root))
        self.friday.place(x=table_pos_x - 100 + 4 * (tp_butt_width + 100), y=button_pos_y, anchor=CENTER)
        """SATURDAY"""
        self.saturday = TkinterCustomButton(text=f"{days[5]}", corner_radius=10, command=lambda: Openday(5, root))
        self.saturday.place(x=table_pos_x - 100 + 5 * (tp_butt_width + 100), y=button_pos_y, anchor=CENTER)
        """SUNDAY"""
        self.sunday = TkinterCustomButton(text=f"{days[6]}", corner_radius=10, command=lambda: Openday(6, root))
        self.sunday.place(x=table_pos_x - 100 + 6 * (tp_butt_width + 100), y=button_pos_y, anchor=CENTER)
        """ALL DAYS"""
        self.all_buttons.append(self.monday)
        self.all_buttons.append(self.tuesday)
        self.all_buttons.append(self.wednesday)
        self.all_buttons.append(self.thursday)
        self.all_buttons.append(self.friday)
        self.all_buttons.append(self.saturday)
        self.all_buttons.append(self.sunday)

        self.all = TkinterCustomButton(text="All days", corner_radius=10, command=lambda: Openday(None, root))
        self.weekend = TkinterCustomButton(text="Weekend", corner_radius=10, command=lambda: Openday("Weekend", root))

        self.all.place(x=1020, y=button_pos_y/2)
        self.weekend.place(x=1160, y=button_pos_y/2)


def check_db_exists(day: str):
    if not os.path.exists(f"database/{TIME['MONTH']}-{TIME['WEEK']}-{day}.db"):
        conn = sqlite3.connect(f"database/{TIME['MONTH']}-{TIME['WEEK']}-{day}.db")
        c = conn.cursor()
        c.execute(""" CREATE TABLE weekplanner (
        hour67 text,
        hour78 text,
        hour89 text,
        hour910 text,
        hour1011 text,
        hour1112 text,
        hour1213 text,
        hour1314 text,
        hour1415 text,
        hour1516 text,
        hour1617 text,
        hour1718 text,
        hour1819 text,
        hour1920 text,
        hour2021 text,
        hour2122 text,
        hour2223 text,
        hour2324 text
        )""")
        conn.commit()
        conn.close()
        insert_study(day)


def insert_study(day):
    study_plan = {
        'Monday': (
        '-', '-', 'HUM wykl', 'HUM wykl/BI wykl', 'BI wykl', 'TS wyklad', 'TS wyklad', 'TS laby', 'Ts laby/BI laby', 'BI laby', '-', '-', '-', '-', '-',
        '-', '-', '-'),
        'Tuesday': (
            '-', 'WORK', 'WORK/PLC', 'WORK/PLC', 'WORK', 'WORK', 'WORK', 'WORK/SYS', 'WORK/SYS', '-', '-', '-', '-',
            '-', '-', '-', '-', '-'),
        'Wednesday': (
            '-', '-', 'Sys Rek laby', 'Sys Rek laby/ML', 'ML wykl', '-', 'Embd wykl', 'Embd wykl', 'ML laby', 'ML laby', '-', '-', '-', '-', '-', '-', '-', '-'),
        'Thursday': (
            '-', '-', 'WORK', 'WORK', 'WORK', 'WORK', 'WORK', 'WORK', 'WORK/TS', 'WORK/TS', '-', '-', '-', '-', '-', '-',
            '-', '-'),
        'Friday': (
            '-', '-', 'PLC laby', 'PLC laby', 'PLC laby', 'Embd laby', 'Embd laby', '-', '-', 'WORK', 'WORK', 'WORK', '-', '-', '-', '-',
            '-', '-'),
        'Saturday': (
            '-', '-', '-', '-', '-', '-', '-', '-', '-', ' -', '-', '-', '-', '-', '-', '-',
            '-', '-'),
        'Sunday': (
            '-', '-', '-', '-', '-', '-', '-', '-', '-', ' -', '-', '-', '-', '-', '-', '-',
            '-', '-'),
    }
    conn = sqlite3.connect(f"database/{TIME['MONTH']}-{TIME['WEEK']}-{day}.db")
    c = conn.cursor()

    c.execute(" INSERT INTO weekplanner VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", study_plan[day])
    conn.commit()
    conn.close()


def get_data_from_db(day: str):
    conn = sqlite3.connect(f"database/{TIME['MONTH']}-{TIME['WEEK']}-{day}.db")
    c = conn.cursor()
    c.execute(""" SELECT * FROM weekplanner""")
    data = c.fetchall()
    conn.close()
    return data


def time_left(time_start, time_end): #TODO
    value = ''
    y_diff = int(time_end[:4]) - int(time_start[0:4])
    m_diff = int(time_end[5:7]) - int(time_start[5:7])
    d_diff = int(time_end[8:10]) - int(time_start[8:10])

    if y_diff >= 0 and m_diff >= 0 and d_diff >= 0:
        value += str(str(y_diff) + "y ")
        value += str(str(m_diff) + "m ")
        value += str(str(d_diff) + "d")
    elif y_diff >= 0 and m_diff < 0:
        value += (str(y_diff - 1) + "y ")
        m_diff = int(12 + time_end[5:7]) - int(time_start[5:7])
        if d_diff >= 0:
            value += (str(d_diff) + "d")
            value += (str(m_diff) + "m ")
        else:
            m_diff -= 1
            value += (str(m_diff) + "m ")
            d_diff += 30
            value += (str(d_diff) + "d")
    elif d_diff < 0:
        m_diff -= 1
        d_diff += 30 # XD wstyd mi za ten kod
        value += (str(y_diff) + "y ")
        value += (str(m_diff) + "m ")
        value += (str(d_diff) + "d")
    return value


def create_goal(name: str, category: str, significance: float, start_date: str, end_date: str, time: float=5.0,
                curr_time: float = 0.0, status: str="WIP"):
    goal = Goal(name, category, significance, start_date, end_date, time, curr_time, status)
    goal.add_to_database()


def delete_goal(name_: str):
    conn = sqlite3.connect("database/goals.db")
    c = conn.cursor()
    c.execute("""DELETE from goals WHERE name=(?)""", name_)
    conn.commit()
    conn.close()


def get_goals_data():
    if os.path.exists("database/goals.db"):
        conn = sqlite3.connect("database/goals.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM main_goals """)
        goals_db = c.fetchall()
        conn.close()
        print(goals_db)
        return goals_db
    else:
        conn = sqlite3.connect("database/goals.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE main_goals (
        name text,
        category text,
        significance REAL,
        date_start text,
        date_end text,
        time REAL,
        curr_time REAL,
        status text
        )""")
        return list()


def AddGoal():
    Add = Tk()
    Add.geometry("600x400")
    Add.title("Add Goal")
    Add.wm_attributes('-transparentcolor', '#ab23ff')
    # logo_goals = PhotoImage(file='Image/plus.jpg')
    # Add.tk.call('wm', 'iconphoto', Add._w, logo_goals)
    #TODO
    # img = ImageTk.PhotoImage(
    #     (Image.open("Image/goals2.png")).resize((200, 100), Image.ANTIALIAS))
    # goal_label = Label(Add, image=img)
    # goal_label.place(x=350, y=50)
    # category, name, value = StringVar(), StringVar(), IntVar() #TODELETE
    entry_name_label = Label(Add, text="Name:")
    entry_name = Entry(Add)
    MenuCategory = CustomedOptionMenu(Add, 'Select Category', *lst_of_categories)
    scale_significance = Scale(Add, from_=0, to=10, state=ACTIVE, orient=HORIZONTAL, label='Significance',
                              resolution=0.5,
                              troughcolor="#6580c3", bg="#425b9a", length=150)
    entry_date_end_label = Label(Add, text="End date:")
    StatusMenu = CustomedOptionMenu(Add, 'Select Status', *lst_of_statuses)

    entry_name_label.place(x=10, y=10)
    entry_name.place(x=85, y=10)
    MenuCategory.place(x=82, y=35)
    scale_significance.place(x=84, y=70)
    entry_date_end_label.place(x=10, y=130)
    goal_calendar = Calendar(Add, selectmode='day', year=int(TIME['YEAR']), month=int(TIME['MONTH']),
                             day=int(TIME['DAY_NUMB']))
    goal_calendar.place(x=85, y=130)
    StatusMenu.place(x=85, y=325)

    Add_button = TkinterCustomButton(master=Add, text="Create Goal", command=lambda: create_goal(str(entry_name.get()),
                                    str(MenuCategory.var.get()), float(scale_significance.get()),
                                    f'{TIME["YEAR"]}-{TIME["MONTH"]}-{TIME["DAY_NUMB"]}',
      f'20{goal_calendar.get_date().split("/")[2]}-{day_to_numb(goal_calendar.get_date().split("/")[0])}-{day_to_numb(goal_calendar.get_date().split("/")[1])}',
                                                2.0, 0.0, str(StatusMenu.var.get()))) # 2.0 is time

    Add_button.place(x=450, y=300)

    Add.mainloop()


def goals_change_status(Goals_table, new_status=None):
    """
    This function is responsible for changing status of chosen task
    Steps:
    1. Check whether task is chosen, if not show error info and stop
    2. Gets value from tkinter table
    3. Connect to database, and find value by name
    4. Make a change in db or delete old task and create new -> first option prefferable
    5. Make a commit and close database
    6. Show message info that everything went okay
    :param Goals_table: which is Tkinter Table with chosen row
    :return:
    """
    curItem = Goals_table.focus() # This return Tkinter item
    dict_table = Goals_table.item(curItem) #This make curItem a dictionary
    if len(dict_table['values']) == 0:
        messagebox.showerror('Please select a goal!')
    else:
        """ Step 2 """
        curr_status, name_of_goal = str(dict_table['values'][5]), str(dict_table['values'][0])
        """ Step 3 """
        conn = sqlite3.connect("database/goals.db")
        c = conn.cursor()
        c.execute("""UPDATE main_goals SET status = ?
            WHERE name = ?
        """,  (new_status, name_of_goal))

        """ Step 4 """
        #TODO
        """ Step 5 """
        conn.commit()
        conn.close()
        """ Step 6 """
        messagebox.showinfo('Goal status changed successfully!')


def goals_delete(Goals_table):
    curItem = Goals_table.focus()  # This return Tkinter item
    dict_table = Goals_table.item(curItem)  # This make curItem a dictionary
    if len(dict_table['values']) == 0:
        messagebox.showerror('Please select a goal!')
    else:
        name_of_goal = str(dict_table['values'][0])
        conn = sqlite3.connect('database/goals.db')
        c = conn.cursor()
        c.execute(""" DELETE from main_goals WHERE name = ?
        """, (name_of_goal,))
        conn.commit()
        conn.close()


def goals_selected(master, goals_table, selected_status='Work in Progress'):
    """
    This function querying data from database and showing table only for chosen status
    :param selected_status:
    :param master:
    :param goals_table:
    :return:
    """
    global goals_data_db
    if selected_status == "All":
        goals_data_db = get_goals_data()
    else:
        conn = sqlite3.connect('database/goals.db')
        c = conn.cursor()
        c.execute("""SELECT * FROM main_goals WHERE status = ?
        """, (selected_status,))
        goals_data_db = c.fetchall() #modyfying global variable which contain goals

    master.destroy()
    Goals()


def UpdateTable(root, user_choice):
    global selection_of_key_sort
    Sort_keys = ["Category", "Significance", "Start date", "End date", "Status"]
    if user_choice == "Category":
        selection_of_key_sort = 1
    elif user_choice == "Significance":
        selection_of_key_sort = 2
    elif user_choice == "Status":
        selection_of_key_sort = 6
    elif user_choice == "Start date":
        selection_of_key_sort = 3
    elif user_choice == "End date":
        selection_of_key_sort = 4
    elif user_choice == "Time left":
        selection_of_key_sort = 7

    goals_data_db.sort(key= lambda v: v[selection_of_key_sort], reverse=True)
    root.destroy()

    Goals()


def Goals():
    global goals_data_db
    Goals = Toplevel()
    """LOGO"""
    Goals.wm_attributes('-transparentcolor', '#ab23ff')
    logo_goals = PhotoImage(file='Image/goals_logo.png')
    Goals.tk.call('wm', 'iconphoto', Goals._w, logo_goals)
    """BACKGROUND"""
    Goals.title("Goals")
    Goals.geometry(f"{int(goals_x_size)}x{int(goals_y_size)}+{screen_pos_x}+{screen_pos_y}")
    bg_goals = ImageTk.PhotoImage(
        (Image.open("Image/goals2.png")).resize((int(goals_x_size), int(goals_y_size)), Image.ANTIALIAS)
    )
    goals_label = Label(Goals, image=bg_goals)
    goals_label.place(x=0, y=0)

    add_button = TkinterCustomButton(master=Goals, text="Add Goal", command=AddGoal)
    add_button.place(x=int(goals_x_size/1.2), y=int(goals_y_size/1.3))

    """TABLE OF GOALS"""
    # Querying data from database
    # goals_data_db = get_goals_data()

    Goals_table = ttk.Treeview(Goals)
    # Goals_table_label.place()
    Goals_table['columns'] = ('Goal', 'Category', 'Significance', 'Start date', 'End date', 'Time', 'Status', 'Time left')

    goals_atributes_lst = ['Goal', 'Category', 'Significance', 'Start date', 'End date', 'Time', 'Status', 'Time left']

    """HEADERS OF COLUMNS"""
    Goals_table.column("#0", width=0, stretch=NO)
    for atribute in goals_atributes_lst:
        Goals_table.column(atribute, anchor=CENTER, width=120)
        Goals_table.heading(atribute, text=atribute, anchor=CENTER)


    """ Sorting goals by significance """
    Sort_keys = ["Category", "Significance", "Start date", "End date", "Status", "Time left"]

    SortMenu = CustomedOptionMenu(Goals, 'Sort by', *Sort_keys)
    SortMenu.place(x=int(goals_x_size / 6.2), y=int(goals_y_size / 26.17))
    SortButton = TkinterCustomButton(master=Goals, text="Sort", command= lambda: UpdateTable(Goals, SortMenu.var.get()))
    SortButton.place(x=int(goals_x_size / 40.5), y=int(goals_y_size / 30.17))

    for goal_id, goal in enumerate(goals_data_db):
        #TODO color depnds on goal time spend green/orange/red
        Goals_table.insert(parent='', index='end', iid=goal_id, text='', values=(*goal[:5], f'{goal[6]} / {goal[5]}', goal[7], time_left(goal[3], goal[4])))

    Goals_table.place(x=int(goals_x_size/45), y=int(goals_y_size/10))
    """Buttons for changing goals status"""

    StatusMenu = CustomedOptionMenu(Goals, 'Select Status', *lst_of_statuses)
    StatusMenu.place(x=int(goals_x_size / 10.5), y=int(goals_y_size / 1.17))

    ChagneStatusButton = TkinterCustomButton(master=Goals, text='Change Status',
                                             command=lambda: goals_change_status(Goals_table, StatusMenu.var.get()))
    ChagneStatusButton.place(x=int(goals_x_size / 10), y=int(goals_y_size / 1.3))

    DeleteGoalButton = TkinterCustomButton(master=Goals, text='Delete Goal', command=lambda: goals_delete(Goals_table))
    DeleteGoalButton.place(x=int(goals_x_size/4.3), y=int(goals_y_size/1.3))

    ShowWIPButton = TkinterCustomButton(master=Goals, text='Working in Progress',
                    command=lambda: goals_selected(Goals, Goals_table, "Work in Progress"), width=int(goals_x_size/6))
    ShowWIPButton.place(x=int(goals_x_size/2.77), y=int(goals_y_size/1.3))

    ShowAllButton = TkinterCustomButton(master=Goals, text='All', command=lambda: goals_selected(Goals, Goals_table,
                                                                        "All"), width=int(goals_x_size/10))
    ShowAllButton.place(x=int(goals_x_size/1.87), y=int(goals_y_size/1.3))

    ShowDoneButton = TkinterCustomButton(master=Goals, text='Done', command=lambda: goals_selected(Goals, Goals_table,
                                                                                                 "Done"),
                                        width=int(goals_x_size / 10))
    ShowDoneButton.place(x=int(goals_x_size / 1.55), y=int(goals_y_size / 1.3))


    Goals.mainloop()


def ShortTasks():
    ShortTasks = Toplevel()
    ShortTasks.title("ShortTasks")
    ShortTasks.geometry(f"{short_tasks_x_size}x{short_tasks_y_size}")
    """ LOGO """
    ShortTasks.wm_attributes('-transparentcolor', '#ab23ff')
    logo_ShortTasks = PhotoImage(file='Image/s_tasks_logo.png')
    ShortTasks.tk.call('wm', 'iconphoto', ShortTasks._w, logo_ShortTasks)
    """ BACKGROUND """
    bg_ShortTasks = ImageTk.PhotoImage(
        (Image.open("Image/slight.jpg")).resize((short_tasks_x_size, short_tasks_y_size), Image.ANTIALIAS)
    )
    goals_label = Label(ShortTasks, image=bg_ShortTasks)
    goals_label.place(x=int(goals_x_size/1.1), y=int(goals_y_size/1.1))

    ShortTasks.mainloop()


def Quit_app(root):
    root.destroy()
    quit()


def change_week(value: int, Root, tab, day_open=None):
    tab.write_data_from_entries_into_db(True) #autosave
    TIME['WEEK'] = day_to_numb(str(int(TIME['WEEK']) + value))
    Root.destroy()
    main_disp(table_look_flag, day_open)


def main_disp(disp_flag, day_open=None):
    """
    Getting data from database into python list.
    Each element of list contain database for specific day from Monday(0) to Sunday(7)
    """

    days_data = list()
    for day in days:
        check_db_exists(day)
        days_data.append(get_data_from_db(day))

    table_look_flag = disp_flag
    """ INITIAL """
    root = Tk()
    root.title('Planner')
    root.geometry(f'{X_size}x{Y_size}+{screen_pos_x}+{screen_pos_y}')

    """LOGO"""
    root.wm_attributes('-transparentcolor', '#ab23ff')
    logo_img = PhotoImage(file='Image/books.png')
    root.tk.call('wm', 'iconphoto', root._w, logo_img)

    """BACKGROUND"""
    background_img = ImageTk.PhotoImage(
        (Image.open("Image/background.jpg")).resize((X_size, Y_size), Image.ANTIALIAS)
    )
    bg_label = Label(root, image=background_img)
    bg_label.place(x=0, y=0)

    if table_look_flag == 1:
        """
        Display Week Table in main screen
        """
        table = Table(root, days_data)
    elif table_look_flag == 2:
        """
        Display Specific Day Table in main screen
        """
        if day_open is not None:
            specific_day_data = days_data[day_open][-1]
            table = TableDay(root, DAY_DICT[str(day_open)], specific_day_data)
        else:
            FileNotFoundError()
    elif table_look_flag == 3:
        """
        DISPLAY WEEKEND TABLE in main screen
        """
        weekend_data = days_data[5:7]
        print(weekend_data)
        table = TableWeekend(root, weekend_data)

    """Display Hours on the left side of screen"""
    hours = HourLabels(root)

    """
    Display Buttons on the top of screen. Buttons are responsible for open concrete day/week/weekend.
    They also shut down the original one.
     """  # TODO consider not shut down previous screen
    topbuttons = TopButtons(root)

    """SAVE"""
    save_button = TkinterCustomButton(text="Save", fg_color="#000000", text_color="#FFFFFF", hover_color="#333333",
                                      command=table.write_data_from_entries_into_db)
    save_button.place(x=save_x, y=save_y)

    """
     SHORT TASKS -> It opens new window where you are able to write and read short tasks like do washes, read conspect etc. 
     """
    # TODO connect with database (querying, deleting,adding)
    short_tasks_button = TkinterCustomButton(text="Short Tasks", bg_color="#B4B4B4", fg_color="#FFA511",
                                             hover_color="#EEB400",
                                             text_color="#FFFFFF", command=ShortTasks)
    short_tasks_button.place(x=st_x, y=st_y)

    """
     GOALS BUTTON -> It opens new window where you are able to write and read general GOALS 
     """
    # TODO connect with database (querying, deleting,adding)

    goals_button = TkinterCustomButton(text="Goals", bg_color="#B4B4B4", fg_color="#FFA511", hover_color="#EEB400",
                                       text_color="#FFFFFF", command=Goals)
    goals_button.place(x=goals_x, y=goals_y)

    """
    Next/Previous week button -> It changes week for next or previous 
    Auto save used there to avoid loosing data
    """
    next_button = TkinterCustomButton(text="Next Week", bg_color="#B4B4B4", fg_color="#22FF22", hover_color="#EEB400",
                                       text_color="#FFFFFF", command=lambda: change_week(1, root, table, day_open))
    next_button.place(x=int(X_size//1.65), y=int(Y_size//1.1))

    previous_button = TkinterCustomButton(text="Previous Week", bg_color="#DDDDCC", fg_color="#BF2222", hover_color="#EEB400",
                                      text_color="#FFFFFF", command=lambda: change_week(-1, root, table, day_open))
    previous_button.place(x=int(X_size//3.5), y=int(Y_size//1.1))

    """
    QUIT BUTTON -> Shut down programm (maybe in future it takes data from entries and save it in database.
    It would prevent user from loosing data in case of forget click save button.
    """
    quit_button = TkinterCustomButton(text="Quit", bg_color="#B4B4B4", fg_color="#EE0505", hover_color="#DD0300",
                                      text_color="#FFFFFF", command=lambda: Quit_app(root))
    quit_button.place(x=X_size // 20, y=Y_size / 1.1)

    root.update()
    root.mainloop()


if __name__ == '__main__':
    goals_data_db = get_goals_data()
    main_disp(table_look_flag)