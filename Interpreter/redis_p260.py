#このプログラムもmemcachedと同様にRedisサーバをインストールしていないと使用することができない。



#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/03.

# import
import redis


# class



"""
def main():
    conn = redis.Redis()
    print('conn.keys("*")',end=' | ')
    print(conn.keys('*'))
    conn.set('secret','ni!')
    conn.set('carats', 24)
    conn.set('fever', '101.5')
    print('conn.get("secret")', end=' | ')
    print(conn.get('secret'))
    print('conn.get("carats")', end=' | ')
    print(conn.get('carats'))
    print('conn.get("fever")', end=' | ')
    print(conn.get('fever'))
    return 0


if __name__ == '__main__':
    main()
"""