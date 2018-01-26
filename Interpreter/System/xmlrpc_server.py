#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/19.

# import
from xmlrpc.server import SimpleXMLRPCServer

def double(num):
    return num * 2


server = SimpleXMLRPCServer(('localhost',6789))
server.register_function(double, 'double')
server.serve_forever()