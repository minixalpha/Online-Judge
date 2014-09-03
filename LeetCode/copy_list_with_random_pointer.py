#!/usr/bin/env python
#coding: utf-8

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        h = ch = RandomListNode(-1)

        k = head
        d, i = {}, 0
        while k:
            d[k] = i
            k = k.next
            i += 1

        k = head
        a = []
        while k:
            ch.next = RandomListNode(k.label)
            a.append(ch.next)
            ch = ch.next
            k = k.next
        
        k, ch = head, h.next
        while k:
            if k.random:
                i = d[k.random]
                ch.random = a[i]
            k = k.next
            ch = ch.next
        return h.next

if __name__ == '__main__':
    s = Solution()
    t = RandomListNode(1)
    t1 = RandomListNode(2)
    t.next = t1
    t1.random = t

    g = s.copyRandomList(t)
    assert g.random == None
    assert g.next.random == g
