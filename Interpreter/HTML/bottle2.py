#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/11.

# import
from bottle import route, run, static_file




# class


@route('/')
def main():
    return static_file('index.html',root='.')

run(host='localhost', port=9999)



if __name__ == '__main__':
    main()