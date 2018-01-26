#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/16.

# import
import multiprocessing
import os


# class


def do_this(what):
    whoami(what)

def whoami(what):
    print('Process %s says: %s' % (os.getpid(),what))


if __name__ == '__main__':
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this,
                                    args=("I'm function %s" % n,))
        p.start()