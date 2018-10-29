#!/usr/bin/env python
# encoding: utf-8

string = input()
tmplist = list(string)
tmplist.reverse()
string = "".join(tmplist)
print(string)
