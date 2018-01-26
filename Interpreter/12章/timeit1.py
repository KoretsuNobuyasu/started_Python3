#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/22.

# import
from timeit import timeit

def main():
    print(timeit('num = 5; num *= 2',number=1))
    return 0


if __name__ == '__main__':
    main()