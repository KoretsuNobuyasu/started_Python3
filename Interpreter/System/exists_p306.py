#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/15.

>>> import os
>>> os.path.exits('oops.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'posixpath' has no attribute 'exits'
>>> os.path.exists('oops.txt')
True
>>> os.path.exists('./oops.txt')
True
>>> os.path.exists('waffles')
False
>>> os.path.exists('.')
True
>>> os.path.exists('..')
True
>>>
>>>
>>> #10.1.3
...
>>> name = 'oops.txt'
>>> os.path.isfile(name)
True
>>> os.path.isdir(name)
False
>>> os.path.isdir('.')
True
>>> os.path.isabs(name)
False
>>> os.path.isabs('/big/fake/name')
True
>>> os.path.isabs('big/fake/name/without/a/leading/slash')
False


>>> import shutil
>>> shutil.copy('oops.txt', 'ohno.txt')
'ohno.txt'
>>> import os
>>> os.rename('ohno.txt', 'ohwell.txt')
>>>
>>> os.link('oops.txt', 'yikes.txt')
>>> os.path.isfile('yikes.txt')
True
>>> os.symlink('oops.txt', 'jeepers.txt')
>>> os.path.islink('jeepers.txt')
True
>>>
>>> os.chmod('oops.txt', 0o400)
>>> import stat
>>> os.chmod('oops.txt', stat.S_IRUSR)
>>> uid = 5
>>> git = 22
>>> os.chown('oops',uid,gid)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'gid' is not defined
>>> gid = 22
>>> os.chown('oops',uid,gid)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'oops'
>>> os.chown('oops.txt',uid,gid)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
PermissionError: [Errno 1] Operation not permitted: 'oops.txt'
>>> os.chown('oops',uid,gid)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'oops'
>>>


>>> os.path.abspath('oops.txt')
'/Users/nobuskate/Desktop/Desktop/started_Python3/Interpreter/System/oops.txt'
>>> os.path.realpath('jeepers.txt')
'/Users/nobuskate/Desktop/Desktop/started_Python3/Interpreter/System/oops.txt'
>>> os.remove('oops.txt')
>>> os.path.exists('oops.txt')
False
>>>


>>> os.mkdir('poems')
>>> os.path.exists('poems')
True
>>> os.rmdir('poems')
>>> os.path.exists('poems')
False
>>> os.mkdir('poems')
>>> os.listdir('poems')
[]
>>> os.mkdir('poems/mcintyre')
>>> os.listdir('poems')
['mcintyre']
>>> fout = open('poems/mcintyre/the_good_man', 'wt')
>>> fout.write('''Cheerful and happy was his mood,
... He to the poor was kind and good,
... And he oft' times did find them food,
... Also supplies of coal and wood,
... He never spake a word was rude,
... And cheer'd those did o'er sorrows brood,
... He passed away not understood,
... Because no poet in his lays
... Had penned a sonnet in his praise,
... 'Tis sad, but such is world's ways.
... ''')
341
>>> fout.close()
>>> os.listdir('poems/mcintyre')
['the_good_man']
>>>

>>> import os
>>> os.chdir('poems')
>>> os.listdir('.')
['mcintyre']
>>> import glob
>>> glob.glob('m*')
['mcintyre']
>>> glob.glob('??')
[]
>>> glob.glob('m??????e')
['mcintyre']
>>> glob.glob('[klm]*e')
['mcintyre']
>>>


10.3.1
iPython 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import subprocess
>>> ret = subprocess.getoutput('date')
>>> ret
'2018年 1月16日 火曜日 13時38分39秒 CST'
>>> ret = subprocess.getoutput('date -u')
>>> ret
'2018年 1月16日 火曜日 05時41分16秒 UTC'
>>> ret = subprocess.getoutput('date -u | wc')
>>> ret
'       1       5      48'
>>>
>>> ret = subprocess.check_output(['date'm '-u'])
  File "<stdin>", line 1
    ret = subprocess.check_output(['date'm '-u'])
                                         ^
SyntaxError: invalid syntax
>>> ret = subprocess.check_output(['date', '-u'])
>>> ret
b'2018\xe5\xb9\xb4 1\xe6\x9c\x8816\xe6\x97\xa5 \xe7\x81\xab\xe6\x9b\x9c\xe6\x97\xa5 05\xe6\x99\x8246\xe5\x88\x8629\xe7\xa7\x92 UTC\n'
>>> ret = subprocess.getstatusoutput('date')
>>> ret
(0, '2018年 1月16日 火曜日 13時46分52秒 CST')
>>> ret = subprocess.call('date')
2018年 1月16日 火曜日 13時47分27秒 CST
>>> ret
0
>>> ret = subprocess.call(['date','-u'])
2018年 1月16日 火曜日 05時48分24秒 UTC
>>>



