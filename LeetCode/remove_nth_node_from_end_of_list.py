#!/usr/bin/env python
#coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        q = []
        h = head
        while h:
            q.append(h)
            h = h.next
        lq = len(q)
        pre = lq-n-1
        if pre >= 0:
            q[pre].next = q[lq-n+1] if lq-n+1 < lq else None
        else:
            head = q[1] if lq > 1 else None
        return head

if __name__ == '__main__':
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(3)
    t4 = ListNode(4)
    t5 = ListNode(5)
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    Solution().removeNthFromEnd(t1, 2)
    assert t3.next == t5

    tk = ListNode(1)
    assert None == Solution().removeNthFromEnd(tk, 1)

    t1 = ListNode(1)
    t2 = ListNode(2)
    t1.next = t2
    assert t1 == Solution().removeNthFromEnd(t1, 1)
