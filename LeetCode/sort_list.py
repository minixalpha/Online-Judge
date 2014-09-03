#!/usr/bin/env python
#coding: utf-8

#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if not head or not head.next:
            return head

        l = 0
        h = head
        while h:
            l += 1
            h = h.next

        
        a, b, c = head, head, None
        i, j = 0, l/2
        while i < j:
            c = b
            b = b.next
            i += 1
        c.next = None

        p, q = self.sortList(a), self.sortList(b)
        r = t = ListNode(0)

        while p and q:
            if p.val < q.val:
                r.next = p
                p = p.next
            else:
                r.next = q
                q = q.next
            r = r.next

        if p:
            r.next = p
        if q:
            r.next = q

        return t.next

def pl(ln):
    if not ln:
        print('\n')
        return
    print(ln.val),
    pl(ln.next)


if __name__ == '__main__':
    import random
    s = Solution()
    n = 5
    a = t = ListNode(0)
    while n:
        p = random.randint(1, 100)
        t.next = ListNode(p)
        t = t.next
        t.next = ListNode(p)
        t = t.next
        n -= 1
    pl(a)
    pl(s.sortList(a))
