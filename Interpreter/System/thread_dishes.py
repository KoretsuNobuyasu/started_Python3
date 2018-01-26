#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/18.

# import
import threading, queue
import time



# class


def washer(dishes, dish_queue):
    for dish in dishes:
        print("Washing", dish)
        time.sleep(5)
        dish_queue.put(dish)

def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print("Drying", dish)
        time.sleep(10)
        dish_queue.task_done()


def main():
    dish_queue = queue.Queue()
    for n in range(2):
        dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
        dryer_thread.start()

    dishes = ['salad', 'bread', 'entree', 'desert']
    washer(dishes, dish_queue)
    dish_queue.join()
    return 0


if __name__ == '__main__':
    main()