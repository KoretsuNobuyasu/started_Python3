#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/16.
　　
>>> import calendar
>>> calendar.isleap(1900)
False
>>> calendar.isleap(1996)
True
>>> calendar.isleap(1999)
False



>>> from datetime import date
>>> halloween 0 date(2014, 10, 31)
  File "<stdin>", line 1
    halloween 0 date(2014, 10, 31)
              ^
SyntaxError: invalid syntax
>>> halloween = date(2014, 10, 31)
>>> halloween
datetime.date(2014, 10, 31)
>>> halloween.day
31
>>> halloween.month
10
>>> halloween.year
2014
>>> halloween.isoformat()
'2014-10-31'
>>> now = date.today()
>>> now
datetime.date(2018, 1, 16)
>>> from datetime import timedelta
>>> one_day = timedelta(days=1)
>>> tomorrow = now + oneday
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'oneday' is not defined
>>> tomorrow = now + one_day
>>> tomorrow
datetime.date(2018, 1, 17)
>>> now + 17*one_day
datetime.date(2018, 2, 2)
>>> yesterday = now - one_day
>>> yesterday
datetime.date(2018, 1, 15)
>>> from datetime import time
>>> noon = time(12, 0, 0)
>>> noon
datetime.time(12, 0)
>>> noon.hour
12
>>> noon.minute
0
>>> noon.microsecond
0
>>>



>>> from datetime import datetime
>>> some_day = datetime(2014, 1,2,3,4,5,6)
>>> some_day
datetime.datetime(2014, 1, 2, 3, 4, 5, 6)
>>> some_day.isoformat()
'2014-01-02T03:04:05.000006'
>>> now = datetime.now()
>>> now
datetime.datetime(2018, 1, 16, 14, 7, 3, 639321)
>>> now.year
2018
>>> now.monthe
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'datetime.datetime' object has no attribute 'monthe'
>>> now.month
1
>>> now.day
16
>>> now.hour
14
>>> now.minute
7
>>> now.second
3
>>> now.microsecond
639321
>>> from datetime import datetime, time, date
>>> noon = time(12)
>>> this_day = date.today()
>>> noon_today = datetime.combine(this_day, noon)
>>> noon_today
datetime.datetime(2018, 1, 16, 12, 0)
>>> noon_today.date()
datetime.date(2018, 1, 16)
>>> noon_today.time()
datetime.time(12, 0)
>>>




10.4.2  timeモジュールの使い方
>>> import time
>>> now = time.time()
>>> now
1516083078.363716
>>> time.ctime(now)
'Tue Jan 16 14:11:18 2018'
>>> time.localtime(now)
time.struct_time(tm_year=2018, tm_mon=1, tm_mday=16, tm_hour=14, tm_min=11, tm_sec=18, tm_wday=1, tm_yday=16, tm_isdst=0)
>>> time.gmtime(now)
time.struct_time(tm_year=2018, tm_mon=1, tm_mday=16, tm_hour=6, tm_min=11, tm_sec=18, tm_wday=1, tm_yday=16, tm_isdst=0)
>>> tm = time.localtime(now)
>>> time.mktime(tm0
...
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tm0' is not defined
>>> time.mktime(tm)
1516083078.0
>>>


10.4.3  日時の読み書き

>>> import time
>>> now = time.time()
>>> time.ctime(now)
'Tue Jan 16 14:14:34 2018'
>>> fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
>>> t = time.localtime()
>>> t
time.struct_time(tm_year=2018, tm_mon=1, tm_mday=16, tm_hour=14, tm_min=16, tm_sec=0, tm_wday=1, tm_yday=16, tm_isdst=0)
>>> time.strftime(fmt, t)
"It's Tuesday, January 16, 2018, local time 02:16:00PM"
>>> from datetime import date
>>> some_day = date(2014, 7, 4)
>>> some_day.strftime(fmt)
"It's Friday, July 04, 2014, local time 12:00:00AM"
>>> from datetime import time
>>> some_time = time(10, 35)
>>> some_time.strftime(fmt)
"It's Monday, January 01, 1900, local time 10:35:00AM"
>>> import time
>>> fmt = "%Y-%m-%d"
>>> time.strptime("2012 01 29", fmt)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/_strptime.py", line 494, in _strptime_time
    tt = _strptime(data_string, format)[0]
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/_strptime.py", line 337, in _strptime
    (data_string, format))
ValueError: time data '2012 01 29' does not match format '%Y-%m-%d'
>>> time.strptime("2012-01-29", fmt)
time.struct_time(tm_year=2012, tm_mon=1, tm_mday=29, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=29, tm_isdst=-1)
>>> time.strptime("2012-13-29", fmt)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/_strptime.py", line 494, in _strptime_time
    tt = _strptime(data_string, format)[0]
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/_strptime.py", line 337, in _strptime
    (data_string, format))
ValueError: time data '2012-13-29' does not match format '%Y-%m-%d'
>>>



>>> import locale
>>> names = locale.locale_alias.keys()
>>> good_names = [name for name in names if len(name) == 5 and name[2] == '_']
>>> goot_names[:5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'goot_names' is not defined
>>> good_names[:5]
['lb_lu', 'or_in', 'cs_cz', 'el_cy', 'sl_si']
>>>
