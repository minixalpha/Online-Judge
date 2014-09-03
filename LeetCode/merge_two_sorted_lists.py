#!/usr/bin/env python
#coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        t1, t2 = l1, l2
        if l1.val < l2.val:
            h = l1
            t1 = t1.next
        else:
            h = l2
            t2 = t2.next

        th = h

        while t1 and t2:
            if t1.val < t2.val:
                th.next = t1
                th = t1
                t1 = t1.next
            else:
                th.next = t2
                th = t2
                t2 = t2.next
        if not t1:
            th.next = t2
        if not t2:
            th.next = t1

        return h

def makeList(m, n):
    th = h = ListNode(m)
    for i in range(m+1, n+1):
        th.next = ListNode(i)
        th = th.next
    return h

def printList(h):
    while h:
        print(h.val),
        h = h.next
    print('\n')

if __name__ == '__main__':
    l1 = makeList(1, 3)
    l2 = makeList(4, 9)
    printList(Solution().mergeTwoLists(l1, l2))
