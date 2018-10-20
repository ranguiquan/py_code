#!/usr/bin/env python
# encoding: utf-8
"""
名称：限行
作者：冉桂全
时间：2018.10.20
"""

chart = {1:[2,7], 2:[3,8], 3:[4,9], 4:[5,0], 5:[1,6]}
day = int(input("今天星期几？请输入一个1~7的数字(7代表星期日):"))
plate = int(input("请输入车牌号:"))
if(day < 1 or day > 7):
    print("输入有误，程序终止")
else:
    tail = plate % 10
    if(day == 6 or day == 7):
        print("今天是周末，不限行")
    elif(tail in chart[day]):
        print("今天限行了")
    else:
        print("今天不限行")
