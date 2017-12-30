#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2017/12/21.

# import
from sources import daily, weekly


# class




def main():
    print("Daily forecast:",daily.forecast())
    print("Weekly forecast:",weekly.forecast())
    for number, outlook in enumerate(weekly.forecast(),1):
        print(number,outlook)

    return 0


if __name__ == '__main__':
    main()