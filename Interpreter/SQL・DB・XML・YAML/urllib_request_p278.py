#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/04.

# import
import urllib.request as ur


# class




def main():
    url = 'https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/fortune_cookie_random1.txt'
    conn = ur.urlopen(url)
    print('conn',end=' | ')
    print(conn)

    data = conn.read()
    print('data',end=' | ')
    print(data)

    print('conn.status',end=' | ')
    print(conn.status)

    print('conn.getheader("Content-Type")',end=" | ")
    print(conn.getheader('Content-Type'))

    print('{0:>25s} {1:>25s}'.format('key','value'))
    for key, value in conn.getheaders():
        print('{0:>35s} {1:>55s}'.format(key, value))
    return 0


if __name__ == '__main__':
    main()