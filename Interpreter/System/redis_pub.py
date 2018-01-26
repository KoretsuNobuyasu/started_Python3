#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/18.

# import
import redis
import random



# class

conn = redis.Redis()
cats = ['siamese', "persian", 'maine coon', 'norwegian forest']
hats = ['stovepipe', 'bowler', 'tam-o-shanter', 'dedora']
for msg in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    print('Publish: %s wears a %s' % (cat, hat))
    conn.publish(cat, hat)