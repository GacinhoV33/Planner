#!/usr/bin/python
# -*- coding: utf-8 -*-


def get_key(dic, val):
    for k,v in dic.items():
        if dic[k] == val:
            return k