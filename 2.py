#!/usr/bin/env python
# encoding: utf-8
class ListNode:
    val
    next
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTowNumbers(self, l1, l2):
        out = ListNode((l1.val + l2.val)%10)
        tmp = out
        tmp1 = l1
        tmp2 = l2
        while l1.next and l2.next:
            tmp.next = ListNode((tmp1.next.val + tmp2.next.val)%10 + (tmp1.val + tmp2.val)/10)
            tmp1 = tmp1.next
            tmp2 = tmp2.next
            tmp = tmp.next


