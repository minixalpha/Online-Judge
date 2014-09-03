#!/usr/bin/env python
#coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head: return None

        h = nh = ListNode(-1)
        ch = head
        while ch and ch.next:
            if ch.val == ch.next.val:
                while ch.next and ch.val == ch.next.val:
                    ch = ch.next
                ch = ch.next
            else:
                t = ch.next
                ch.next = None
                nh.next = ch
                nh = ch
                ch = t
        if ch:
            nh.next = ch
            ch.next = None
        return h.next

def makeL(x):
    for i in range(len(x) - 1):
        x[i].next = x[i+1]
    return x[0]

def printL(head):
    while head:
        print(head.val),
        head = head.next
    print('')


if __name__ == '__main__':
    t = [ListNode(i) for i in [1,2,3,3,4,4,5]]
    t = makeL(t)
    printL(Solution().deleteDuplicates(t))

    t = [ListNode(i) for i in [1,1,1,2,3]]
    t = makeL(t)
    printL(Solution().deleteDuplicates(t))

