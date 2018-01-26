#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/22.

# import
from time import time


def main():
    t1 = time()
    num = 5
    num *= 2
    print(time() - t1)
    return 0


if __name__ == '__main__':
    main()