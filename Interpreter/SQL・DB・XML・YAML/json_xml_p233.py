#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2017/12/29.

# import
import json
import datetime
from time import mktime

# class
class DTEncoder(json.JSONEncoder):
    def default(self,obj):
        #isinstance()はobjの型をチェックする
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        #でなければ、通常のデコーダの処理を行う
        return json.JSONEncoder.default(self,obj)




menu = \
{
    "breakfast" : {
        "hours" : "7-11",
        "items" : {
            "breakfast burritos" : "$6.00",
            "pancakes" : "$4.00",
        }
    },
    "lunch" : {
        "hours" : "11-3",
        "items" : {
            "hamburger" : "$5.00"
        }
    },
    "dinner" : {
        "hours" : "3-10",
        "items" : {
            "spaghetti" : "$8.00"
        }
    }
}


def main():
    menu_json = json.dumps(menu)
    print(menu_json)
    print("\n\n\n")
    menu2 = json.loads(menu_json)
    print(menu2)
    print("\n\n\n")

    now = datetime.datetime.utcnow()
    now_str = str(now)
    print(json.dumps(now_str))
    now_epoch = int(mktime(now.timetuple()))
    print(json.dumps(now_epoch))
    print(json.dumps(now, cls=DTEncoder))
    print("\n\n\n")

    print(type(now))
    print(isinstance(now, datetime.datetime))
    print(type(234))
    print(isinstance(234, int))
    print(type('hey'))
    print(isinstance('hey',str))

    return 0


if __name__ == '__main__':
    main()