#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/11.

# import
from bottle import route, run



# class



@route('/')
def home():
    return "It isn't fancy, but it's my home page"


def main():
    run(host='localhost', port = 9999)

    return 0


if __name__ == '__main__':
    main()