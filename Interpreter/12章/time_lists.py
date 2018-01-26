#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/22.

# import
from timeit import timeit


def make_list_1():
    result = []
    for value in range(1000):
        result.append(value)
    return result

def make_list_2():
    result = [value for value in range(1000)]
    return result



def main():
    print("make_list_1 takes",timeit(make_list_1,number=1000),"seconds")
    print("make_list_2 takes",timeit(make_list_2,number=1000),"seconds")
    return 0


if __name__ == '__main__':
    main()