#!/usr/bin/env python
# encoding: utf-8

"""
筛选法算素数
作者：冉桂全
时间：2018/10/29
"""
command = int(input("你想要多少以内的素数（包含）？"))
array = []
tmp = 0
for i in range(command+1):
    array.append(1)
array[0] = array[1] = 0
while tmp <= command//2:
    while array[tmp] == 0: tmp+=1
    for i in range(2, int(command/tmp)+1, 1):
        array[i*tmp] = 0
    tmp+=1

for i in range(command+1):
    if array[i] == 1:
        print(i, end = ' ')
print()

