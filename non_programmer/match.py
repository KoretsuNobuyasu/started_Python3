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

    phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #グループなし
    print('Cell: 415-555-9999 Work: 212-555-0000',end=' | ')
    print(phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

    phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
    print('Cell: 415-555-9999 Work: 212-555-0000', end=' | ')
    print(phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
    print("\n\n\n\n")

    print("7.6      p168    課題文字集合")
    xmas_regex = re.compile(r'\d+\s\w+')
    print('12 drummers, 11 pipers, 10 loads, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge',end=' | ')
    print(xmas_regex.findall('12 drummers, 11 pipers, 10 loads, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
    print("\n\n\n\n")

    print("7.7      p168    課題独自に文字集合を定義する")
    vowel_regex = re.compile(r'[aeiouAEIOU]')
    print('RoboCop eats baby food. BABY FOOD.',end=' | ')
    print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))
    constant_regex = re.compile(r'[^aeiouAEIOU]')
    print('RoboCop eats baby food. BABY FOOD.',end=' | ')
    print(constant_regex.findall('RoboCop eats baby food. BABY FOOD.'))
    print("\n\n\n\n")

    print("7.8      p169    課題キャレットとドル記号")
    begins_with_hello = re.compile(r'^Hello')
    print('Hello world!',end=' | ')
    print(begins_with_hello.search('Hello world!'))
    print('search  "He said Hello" Helloから始まらない。NoneであればTrueを返す。',end=' | ')
    print(begins_with_hello.search('He said Hello.') == None)

    ends_with_number = re.compile(r'\d$')
    print("数字で終わる文字列にマッチする      Your number is 42",end=' | ')
    print(ends_with_number.search('Your number is 42'))
    print("文字列が数字で終わらない。NoneであればTrueを返す。 　'You are 42 years old.'",end=' | ')
    print(ends_with_number.search('You are 42 years old.') == None)

    whole_string_is_num = re.compile(r'^\d+$')
    print('1234567890の中から、全体が1文字以上の数字である文字列とマッチする',end=' | ')
    print(whole_string_is_num.search(('1234567890')))
    print('12345xyz67890    で、1文字以上の数字である文字列と一致する。int型の中にstrなどがあると一致しない。よって、一致しないことを確認する。NoneであればTrueを返す。',end=' | ')
    print(whole_string_is_num.search('12345xyz67890') == None)
    print('12 34567890      で、1文字以上の数字である文字列と一致する。空白文字が入っているので一致しないはず。よって、NoneであればTrueを返す。',end=' | ')
    print(whole_string_is_num.search('12 34567890') == None)
    print("\n\n\n\n")

    print("7.9      p170    課題ワイルドカード文字")
    at_regex = re.compile(r'.at')
    print('atが入った文字列をリストに入れprintする。',end=" | ")
    print(at_regex.findall('The cat in the hat sat on the flat mat.'))
    print("\n\n\n\n")

    print("7.9.1    p179    ドットとアスタリスクであらゆる文字列とマッチする。")
    name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
    print('First Name: Al Last Name: Sweigar　の中で、名前や苗字に一致するものを羅列する',end=' | ')
    mo = name_regex.search('First Name: Al Last Name: Sweigart')
    print(mo.group(1),end=' --  ')
    print(mo.group(2))

    nongreedy_regex = re.compile(r'<.*?>')  #非貪欲
    mo = nongreedy_regex.search('<To serve man > for dinner.>')
    print("<To serve man > for dinner.>       <>の中で最も小さいものを表示する",end=' | ')
    print(mo.group())
    greedy_regex = re.compile(r'<.*>')  #貪欲
    mo = greedy_regex.search('<To serve man> for dinner.>')
    print('<To serve man> for dinner.>      の中で最も大きい<>の中を表示する',end=" | ")
    print(mo.group())
    print("\n\n\n\n")

    print("7.9.2    p171    課題ドット文字を開業とマッチさせる")
    no_newline_regex = re.compile('.*')
    print("ここから\n")
    print('Serve the puclic trust.\nProtect the innocent.\nUphold the law.')
    print("\nここまでの中で、改行コード以外のあらゆる文字とマッチする。今回は、改行コートが含まれるところまで。",end=" | ")
    print(no_newline_regex.search('Serve the puclic trust.\nProtect the innocent.\nUphold the law.').group())
    print("\n\n前回同様ここから")
    print('Serve the puclic trust.\nProtect the innocent.\nUphold the law.')
    print("\nここまでの同じ文章の中で、今回は改行コードを含む全ての文字とマッチするようになる。",end=" | ")
    newline_regex = re.compile('.*',re.DOTALL)
    print(newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
    print("\n\n\n\n")

    print("7.11     p173    課題大文字・小文字を無視したマッチ")
    regex1 = re.compile('RoboCop')
    regex2 = re.compile('ROBOCOP')
    regex3 = re.compile('robOcop')
    regex4 = re.compile('RobocOp')
    robocop = re.compile(r'robocop', re.I)
    print(robocop.search('RoboCop is part man, part machine, all cop.').group())
    print(robocop.search('ROBOCOP protects the innocent.').group())
    print(robocop.search('Al, why does your programming book talk about robocop so much?').group())
    print("\n\n\n\n")

    print("7.12     p173    課題sub()メソッドを用いて文字列を置換する")





    print()
    return 0


if __name__ == '__main__':
    main()