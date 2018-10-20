#!/usr/bin/env python
# encoding: utf-8
"""
名称：石头剪刀布
版本：1.0
作者：冉桂全
时间：2018.10.20
"""
import random
convertion = {0:"剪刀", 1:"石头", 2:"布"}
judger = [[0, -1, 1],
        [1, 0, -1],
        [-1, 1, 0]]
while(1):
    print("石头剪刀布游戏")
    print("选项:")
    print("0:开始玩")
    print("1:查看帮助")
    print("2:退出")
    print("请输入:", end='')
    option = input()
    while(option not in ['0','1','2']):
        print("输入错误，请重新输入:", end='')
        option = input()
    option = int(option)
    if(option == 0):
        while(1):
            print("开始猜拳！0:%s 1:%s 2:%s q:退出" %(convertion[0], convertion[1], convertion[2]))
            print("请输入:", end='')
            option = input()
            while(option not in ['0', '1', '2', 'q']):
                print("输入错误，请重新输入:", end='')
                option = input()
            if(option in ['0', '1', '2']):
                option = int(option)
                computer = random.randint(0,2)
                if(judger[option][computer] == 1):
                    print("恭喜您赢了！\n电脑出的<%s>而您出的<%s>" %(convertion[computer], convertion[option]))
                elif(judger[option][computer] == 0):
                    print("平局，都出的<%s>" %(convertion[computer]))
                elif(judger[option][computer] == -1):
                    print("很遗憾，电脑赢了。\n电脑出的<%s>而您出的<%s>" %(convertion[computer], convertion[option]))
            else: break
    elif(option == 1):
        print("这都要看帮助？你没救了")
        print("按回车继续...")
        input()
    elif(option == 2): break



