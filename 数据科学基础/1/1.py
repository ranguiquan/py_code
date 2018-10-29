#!/usr/bin/env python
# encoding: utf-8
"""
名称：测身材
作者：冉桂全
时间：2018.10.20
"""

def BMI_get(weight, height):
    return weight/(height**2)

standard1 = 18.5
standard2 = 23.9
standard3 = 27.9
standard4 = 35
weight = float(input("输入体重(kg):"))
height = float(input("输入身高(m):"))
bmi = BMI_get(weight, height)
if(bmi < standard1):
    print("体重过轻")
elif(standard1 <= bmi < standard2):
    print("体重正常")
elif(standard2 <= bmi < standard3):
    print("肥胖")
else:
    print("过度肥胖")#这是一个注释
