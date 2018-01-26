#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/19.

# import
from msgpackrpc import Server, Address

class Services():
    def double(self, num):
        return num * 2


server = Server(Services())
server.listen(Address("localhost", 6789))
server.start()
