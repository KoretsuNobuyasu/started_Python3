#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/15.

# import



# class




def main():
    fout = open('oops.txt', 'wt')
    print('Oops, I created a file.', file=fout)
    fout.close()
    return 0


if __name__ == '__main__':
    main()