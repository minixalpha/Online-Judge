#!/usr/bin/env python
#coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        k = ListNode(-1)
        k.next = head
        tk = k
        while tk.next:
            n1 = tk.next
            n2 = n1.next
            if n2:
                n1.next = n2.next
                n2.next = n1
                tk.next = n2
            tk = n1
        return k.next



def getList(m, n):
    h = th = ListNode(m)
    for i in range(m+1, n+1):
        th.next = ListNode(i)
        th = th.next
    return h

def printList(head):
    while head:
        print(head.val),
        head = head.next
    print('\n')

if __name__ == '__main__':
    s = Solution()
    head = getList(1,1)
    printList(head)
    printList(s.swapPairs(head))
