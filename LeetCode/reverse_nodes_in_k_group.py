#!/usr/bin/env python
#coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        h = ch = ListNode(-1)

        t = cn = head
        i = 0
        while cn:
            cn_next = cn.next
            cn.next = ch.next
            ch.next = cn
            i += 1
            if i == k:
                i = 0
                ch = t
                t = cn_next
            cn = cn_next
        
        if i != 0:
            cn = ch.next.next
            ch.next.next = None
            while cn:
                cn_next = cn.next
                cn.next = ch.next
                ch.next = cn
                cn = cn_next
        return h.next

def makeL(m, n):
    x = [ListNode(i) for i in range(m, n+1)]
    for i in range(len(x) - 1):
        x[i].next = x[i+1]
    return x[0]

def printL(head):
    while head:
        print(head.val),
        head = head.next
    print('')

if __name__ == '__main__':
    head = makeL(1,5)
    printL(head)
    s = Solution()
    printL(s.reverseKGroup(head, 2))
    head = makeL(1,5)
    printL(s.reverseKGroup(head, 3))
