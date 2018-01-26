#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/11.

# import
from bottle import route, run, static_file



# class

@route('/')
def home():
    return static_file('index.html',root='.')

@route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s!" % thing



def main():
    run(host='localhost', port=9999)
    return 0


if __name__ == '__main__':
    main()