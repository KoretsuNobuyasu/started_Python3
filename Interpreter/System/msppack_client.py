#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/19.

# import
from msgpackrpc import Client, Address

client = Client(Address("localhost",6789))
num = 8
result = client.call('double', num)
print("Double %s is %s" % (num, result))