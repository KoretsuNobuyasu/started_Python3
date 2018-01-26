#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/24.

# import
>>> import math
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.fabs(98.6)
98.6
>>> math.fabs(-271.1)
271.1
>>> math.floor(98.6)
98
>>> math.floor(-271.1)
-272
>>> math.ceil(98.6)
99
>>> math.ceil(-271.1)
-271
>>> math.factrial(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'factrial'
>>> math.factorial(0)
1
>>> math.factorial(1)
1
>>> math.factorial(2)
2
>>> math.factorial(3)
6
>>> math.factorial(4)
24
>>> math.factorial(10)
3628800
>>> math.log(1.0)
0.0
>>> math.log(math.e)
1.0
>>> math.log(8, 2)
3.0
>>> math.pow(2, 3)
8.0
>>> math.sqrt(100.0)
10.0
>>> x = 3.0
>>> y = 4.0
>>> math.hypot(x,y)
5.0

>>> from decimal import Decimal
>>> price = Decimal('19.99')
>>> tax = Decimal('0.06')
>>> total = price + (price * tax)
>>> total
Decimal('21.1894')
>>> from fractions import Fraction
>>> Fraction(1, 3) * Fraction(2, 3)
Fraction(2, 9)
>>>


