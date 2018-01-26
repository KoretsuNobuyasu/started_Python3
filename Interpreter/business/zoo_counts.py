#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/22.

# import
import csv
from collections import Counter

def main():
    counts = Counter()
    with open('zoo.csv','rt') as fin:
        cin = csv.reader(fin)
        for num, row in enumerate(cin):
            if num > 0:
                counts[row[0]] += int(row[-1])
    for animal, hush in counts.items():
        print("%10s %10s" % (animal, hush))
    return 0


if __name__ == '__main__':
    main()