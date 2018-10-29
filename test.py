#!/usr/bin/env python
# encoding: utf-8
l1 = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
l2 = ['1','0','X','9','8','7','6','5','4','3','2']
number = '53010219200508011X'
out = 0
for i in range(17):
    out += int(number[i]) * l1[i]
print(l2[out%11])
