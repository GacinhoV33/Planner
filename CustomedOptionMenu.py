#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *


class CustomedOptionMenu(OptionMenu):
    def __init__(self, master, status, *options):
        self.var = StringVar(master)
        self.var.set(status)
        OptionMenu.__init__(self, master, self.var, *options)
        self.config(font=('calibri', (10)),bg='white',width=12)
        self['menu'].config(font=('calibri', (10)),bg='white')