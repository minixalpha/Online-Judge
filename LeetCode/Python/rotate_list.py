#!/usr/bin/env python
#coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def _gettk(self, head, k):
        h, l = head, 0
        while h:
            h = h.next
            l += 1
        return k % l

    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head: return None
        k = self._gettk(head, k)
        if k == 0: return head
        
        p, i = head, 0
        while p and i < k:
            p = p.next
            i += 1
        if not p: return head
        
        q = head
        while p.next:
            p = p.next
            q = q.next
        
        nh = q.next
        p.next = head
        q.next = None
        return nh


def makeL(n):
    t = [ListNode(i) for i in range(1, n+1)]
    for i in range(0, n-1):
        t[i].next = t[i+1]
    return t[0]

if __name__ == '__main__':
    s = Solution()
    assert None == s.rotateRight(None, 0)

    h = s.rotateRight(makeL(5), 2)
    assert 4 == h.val
    assert 5 == h.next.val
    assert 1 == h.next.next.val
    assert 2 == h.next.next.next.val
    assert 3 == h.next.next.next.next.val
    assert None == h.next.next.next.next.next

    h = s.rotateRight(makeL(5), 6)
    assert 5 == h.val
    assert 1 == h.next.val

    h = s.rotateRight(makeL(2), 3)
    assert 2 == h.val
    assert 1 == h.next.val
