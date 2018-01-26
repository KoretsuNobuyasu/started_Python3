#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/22.

def dump(func):
    "入力引数と出力ちを表示する"
    def wrapped(*args, **kwargs):
        print('Function name: %s' % func.__name__)
        print('Input arguments: %s' % ' '.join(map(str, args)))
        print('Input keyword arguments: %s' % kwargs.items())
        output = func(*args, **kwargs)
        print('Output:',output)
        return output
    return wrapped
