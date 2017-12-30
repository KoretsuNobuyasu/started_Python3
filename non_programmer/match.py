#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2017/12/29.

# import
import re


# class




def main():
    print("7.3.4    p164    課題アスタリスクを用いた0回以上のマッチ")
    bat_regex = re.compile(r'Bat(wo)*man')
    mo1 = bat_regex.search('The Adventures of Batman')
    print('The Adventures of Batman',end=' | ')
    print(mo1.group())

    mo2 = bat_regex.search('The Adventures of Batwoman')
    print('The Adventures of Batwoman',end=' | ')
    print(mo2.group())

    mo3 = bat_regex.search('The Adventures of Batwowowowoman')
    print('The Adventures of Batwowowoman',end=' | ')
    print(mo3.group())
    print("\n\n\n\n")


    print("7.3.5    p164    課題プラスを用いた1回以上のマッチ")
    bat_regex = re.compile(r'Bat(wo)+man')
    mo1 = bat_regex.search('The Adventures of Batwoman')
    print('The Adventures of Batman',end=' | ')
    print(mo1.group())

    mo2 = bat_regex.search('The Adventures of Batwowowowoman')
    print('The Adventures of Batwowowowoman',end=' | ')
    print(mo2.group())

    mo3 = bat_regex.search('The Adventures of Batman')
    print('The Adventures of Batman')
    print('mo3 == None',end=' | ')
    print(mo3 == None)
    print('\n\n\n\n')


    print("7.3.6    p165    課題波カッコを用いて繰り返し回数を指定する")
    ha_regex = re.compile(r'(Ha){3,5}')
    mo1 = ha_regex.search('HaHaHaHaHa')
    print(mo1.group())
    mo2 = ha_regex.search('Ha')
    print('mo2 == None',end=' | ')
    print(mo2 == None)
    print("\n\n\n\n")


    print("7.4      p166    課題貪欲マッチを非貪欲マッチ")
    greedy_Ha_regex = re.compile(r'(Ha){3,5}')
    mo1 = greedy_Ha_regex.search('HaHaHaHaHa')
    print(mo1.group())
    nongreedy_Ha_regex = re.compile(r'(Ha){3,5}?')
    mo2 = nongreedy_Ha_regex.search('HaHaHaHaHa')
    print(mo2.group())
    print("\n\n\n\n")

    print("7.5      p167    課題findall()メソッド")
    phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phone_num_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
    print('Cell: 415-555-9999 Work: 212-555-0000',end=' | ')
    print(mo.group())


    return 0


if __name__ == '__main__':
    main()