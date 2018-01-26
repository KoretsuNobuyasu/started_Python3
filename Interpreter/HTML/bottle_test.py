#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/11.

# import
import requests


# class




def main():
    resp = requests.get('http://localhost:9999/echo/Mothra')
    if resp.status_code == 200 and resp.text == 'Say hello to my little friend: Mothra!':
        print('It worked! That almost never happens!')
    else:
        print('Argh, got this:', resp.text)

    return 0


if __name__ == '__main__':
    main()