#!/usr/bin/env python
#coding: utf-8

import testutil

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def _findMid(self, head):
        hfast = hslow = head

        while hslow and hslow.next:
            hfast = hfast.next
            hslow = hslow.next
            if hslow: hslow = hslow.next

        return hfast

    def _reverseList(self, head):
        if not head: return None

        t = ListNode(0)
        t.next = head

        cur = head.next
        head.next = None
        while cur:
            ncur = cur.next
            cur.next = t.next
            t.next = cur
            cur = ncur

        return t.next

    def _combine(self, h1, h2):
        p1, p2 = h1, h2

        while p2:
            np2 = p2.next

            p2.next = p1.next
            p1.next = p2
            p1 = p2.next

            p2 = np2

        return h1

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head: return None

        mid = self._findMid(head)
        half_start = mid.next
        mid.next = None
        rev_half_start = self._reverseList(half_start)

        h = self._combine(head, rev_half_start)
        return h



if __name__ == '__main__':
    s = Solution()
    #h = None
    #s.reorderList(h)
    #assert None == h

    #h = testutil.makeL(4)
    #s.reorderList(h)
    #assert 1 == h.val
    #assert 4 == h.next.val
    #assert 2 == h.next.next.val
    #assert 3 == h.next.next.next.val
    #assert None == h.next.next.next.next

    #h = testutil.makeL(2)
    #s.reorderList(h)
    #assert 1 == h.val
    #assert 2 == h.next.val
    #assert None == h.next.next

    #h = testutil.makeL(1)
    #s.reorderList(h)
    #assert 1 == h.val
    #assert None == h.next

    for i in range(1, 11):
        h = testutil.makeL(i)
        s.reorderList(h)

