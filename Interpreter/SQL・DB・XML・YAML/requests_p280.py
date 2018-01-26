#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/10.

# import
import requests


# class


url = 'https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/fortune_cookie_random2.txt'


def main():
    resp = requests.get(url)
    print('resp',end=' | ')
    print(resp)

    print('\n---resp.text---')
    print(resp.text)
    return 0


if __name__ == '__main__':
    main()