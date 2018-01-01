# usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by koretsunobuyasu on 2018/01/01
import pickle
import datetime

class Tiny():
    def __str__(self):
        return 'tiny'


def main():
    now1 = datetime.datetime.utcnow()
    pickled = pickle.dumps(now1)
    now2 = pickle.loads(pickled)
    print(now1)
    print(now2)
    print("\n\n\n\n")

    obj1 = Tiny()
    print(obj1)
    print(str(obj1))
    pickled = pickle.dumps(obj1)
    print(pickled)
    obj2 = pickle.loads(pickled)
    print(obj2)
    print(str(obj2))

    return 0


if __name__ == '__main__':
    main()