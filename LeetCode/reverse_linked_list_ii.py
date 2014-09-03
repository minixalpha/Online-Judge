#!/usr/bin/env python
#coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n: return head

        senti = ListNode(-1)
        senti.next = head

        h, i = senti, 1
        while i < m:
            h = h.next
            i += 1
        
        nh = h
        s = h.next
        while i < n:
            nh = nh.next
            i += 1

        e = nh.next
        h.next = nh.next
        nh.next = None
        
        while s:
            ns = s.next
            if e:
                s.next = e.next
                e.next = s
            s = ns
        return senti.next
    
def makeList(m, n):
    head = h = ListNode(m)
    for e in range(m+1, n+1):
        h.next = ListNode(e)
        h = h.next
    return head

def printList(head):
    while head:
        print(head.val),
        head = head.next
    print('')

if __name__ == '__main__':
    s = Solution()
    head = makeList(1,5)
    printList(head)
    printList(s.reverseBetween(head, 2, 4))

    head = makeList(1,1)
    printList(head)
    printList(s.reverseBetween(head, 1, 1))

    head = makeList(1,2)
    printList(head)
    printList(s.reverseBetween(head, 1, 2))

