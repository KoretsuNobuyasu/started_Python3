#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/01.

# import
import sqlite3



# class

#基本的に、モードでしか使えないと思う。
#一行ずつ実行する必要がある。
#同じ階層にdbファイルを作成しておく必要がある。
#main関数の中のコメント
#順番に実行していくため、残しているとエラーが出るので注意

def main():
    conn = sqlite3.connect('enterprise.db')
    curs = conn.cursor()
    curs.execute('''CREATE TABLE zoo (critter VARCHER(20)
    PRIMARY KEY, count INT, damages FLOAT)''')

    curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
    curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')

    ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
    curs.execute(ins, ('weasel', 1, 2000.0))

    curs.execute('SELECT * FROM zoo')

    rows = curs.fetchall()
    print(rows)

    curs.execute('SELECT * from zoo ORDER BY count')
    curs.fetchall()

    curs.execute('SELECT * from zoo ORDER BY count DESC')
    curs.fetchall()

    curs.execute('''SELECT * FROM zoo WHERE damages = (SELECT MAX(damages) FEOM zoo)''')
    curs.fetchall()

    curs.close()
    conn.close()
    return 0


if __name__ == '__main__':
    main()