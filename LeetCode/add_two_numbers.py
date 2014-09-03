#!/usr/bin/env python
#coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        h = ch = ListNode(-1)
        
        n1, n2, c = l1, l2, 0
        while n1 or n2:
            a = n1.val if n1 else 0
            b = n2.val if n2 else 0

            s = a + b + c
            ch.next = ListNode(s % 10)
            c = s / 10
            ch = ch.next

            if n1: n1 = n1.next
            if n2: n2 = n2.next
        if c:
            ch.next = ListNode(c)
            
        return h.next

def printL(x):
    for i in x:
        print(i.val),
    print('')

if __name__ == '__main__':
    t0 = [ListNode(i) for i in (2,4,3)]
    t0[0].next = t0[1]
    t0[1].next == t0[2]
    t1 = [ListNode(i) for i in (5,6,4)]
    t1[0].next = t1[1]
    t1[1].next == t1[2]
    t2 = [ListNode(i) for i in (7,0,8)]
    t2[0].next = t2[1]
    t2[1].next == t2[2]
    printL(t0), printL(t1), printL(t2)
    s = Solution()
    assert t2[0].val == s.addTwoNumbers(t0[0], t1[0]).val
