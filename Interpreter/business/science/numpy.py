#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/25.

# import
>>> import numpy as np
>>> b = np.array([2,4,6,8])
>>> b
array([2, 4, 6, 8])
>>> b.ndim
1
>>> b.size
4
>>> b.shape
(4,)
>>> a = np.arrange(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'numpy' has no attribute 'arrange'
>>> a = np.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a.ndim
1
>>> a.shape
(10,)
>>> a.size
10
>>> a = np.arange(7,11)
>>> a
array([ 7,  8,  9, 10])
>>> a = np.arange(7,11,2)
>>> a
array([7, 9])
>>> f = np.arange(2.0,9.8,0.3)
>>> f
array([2. , 2.3, 2.6, 2.9, 3.2, 3.5, 3.8, 4.1, 4.4, 4.7, 5. , 5.3, 5.6,
       5.9, 6.2, 6.5, 6.8, 7.1, 7.4, 7.7, 8. , 8.3, 8.6, 8.9, 9.2, 9.5,
       9.8])
>>> g = np.arange(10,4,-1.5,dtype=np.float)
>>> g
array([10. ,  8.5,  7. ,  5.5])

>>> a = np.zeros((3,))
>>> a
array([0., 0., 0.])
>>> a.ndim
1
>>> a.shape
(3,)
>>> a.size
3
>>> b = np.zeros((2,4))
>>> b
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> b.ndim
2
>>> b.shape
(2, 4)
>>> b.size
8
>>> k = np.ones((3,5))
>>> k
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])
>>> k.ndim
2
>>> m = np.random.random((3,5))
>>> m
array([[0.39907443, 0.4914677 , 0.35963247, 0.85375712, 0.62643268],
       [0.93739306, 0.59479565, 0.07368394, 0.2516766 , 0.73146721],
       [0.47805449, 0.87919163, 0.58913828, 0.54813715, 0.52181896]])


>>> a = np.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a = a.reshape(2,5)
>>> a
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
>>> a.ndim
2
>>> a.shape
(2, 5)
>>> a.size
10
>>> a = a.reshape(5,2)
>>> a
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])
>>> a.ndim
2
>>> a.shape
(5, 2)
>>> a.size
10
>>> a.shape(2,5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object is not callable
>>> a.shape = (2,5)
>>> a
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
>>> a = a.reshape(3,4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot reshape array of size 10 into shape (3,4)


>>> a = np.arange(10)
>>> a[7]
7
>>> a[-1]
9
>>> a.shape = (2,5)
>>> a
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
>>> a[1,2]
7
>>> l = [ [0,1,2,3,4],[5,6,7,8,9] ]
>>> l
[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
>>> l[1,2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> l[1][2]
7
>>> a = np.arange(10)
>>> a = a.reshape(2,5)
>>> a
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
>>> a[0, 2:]
array([2, 3, 4])
>>> a[-1, :3]
array([5, 6, 7])
>>> a[:, 2:4] = 1000
>>> a
array([[   0,    1, 1000, 1000,    4],
       [   5,    6, 1000, 1000,    9]])


