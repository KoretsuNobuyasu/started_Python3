#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/20.

# import



# class

"ここにモジュールのdocstringを書く"

def func():
    "ここに関数のdocstringを書く"
    first = 1
    second = 2
    third = 3
    print(first)
    print(second)
    print(third)

func()

"""
nobu-Air:12章 nobuskate$ pylint style3.py
No config file found, using default configuration
************* Module style3
C: 22, 0: Final newline missing (missing-final-newline)

-----------------------------------
Your code has been rated at 8.75/10

nobu-Air:12章 nobuskate$ pylint style3.py
No config file found, using default configuration

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 8.75/10, +1.25)
"""