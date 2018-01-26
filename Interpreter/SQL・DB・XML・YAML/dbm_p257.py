#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/03.

# import
import dbm


# class




def main():
    db = dbm.open('definitions','c')
    db['mustard'] = 'yellow'
    db['ketchup'] = 'red'
    db['pesto'] = 'green'

    print('len(db)',end='       | ')
    print(len(db))
    print('db["pesto"]',end='   | ')
    print(db['pesto'])

    db.close()
    db = dbm.open('definitions','r')
    print('\n読み込みモードに変更')
    print('db["mustard"]',end=' | ')
    print(db['mustard'])


    return 0


if __name__ == '__main__':
    main()