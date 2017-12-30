#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2017/12/30.

# import

import yaml


# class




def main():
    with open('mcintyre.yaml', 'rt') as fin:
        text = fin.read()

    data = yaml.load(text)
    print(data['details'])

    print(len(data['poems']))
    print(data['poems'][1]['title'])
    return 0


if __name__ == '__main__':
    main()