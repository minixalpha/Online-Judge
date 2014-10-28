#!/usr/bin/env python
#coding: utf-8

import testutil

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def _merge(self, L1, L2):
        if not L1: return L2
        if not L2: return L1

        h = ch = ListNode(0)
        p, q = L1, L2

        while p and q:
            if p.val < q.val:
                ch.next = p
                p = p.next
            else:
                ch.next = q
                q = q.next
            ch = ch.next
        
        if p: ch.next = p
        if q: ch.next = q

        return h.next

    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if not lists: return None
        
        list_len = len(lists)
        while list_len != 1:
            nlist = []
            
            for i in range(0, list_len, 2):
                if i == list_len - 1: nlist.append(lists[i])
                else: nlist.append(self._merge(lists[i], lists[i+1]))

            lists = nlist
            list_len = len(lists)

        return lists[0]


if __name__ == '__main__':
    s = Solution()

    assert None == s.mergeKLists(None)
    assert [] == s.mergeKLists([])

    h = [ListNode(i) for i in [1, 3, 2]]
    x, y = h[0], s.mergeKLists(h)
    assert x == y


    h = [ListNode(i) for i in [2, 1, 3]]
    x, y = h[1], s.mergeKLists(h)
    assert x == y

    h = [ListNode(i) for i in [2, 1, 3, 5]]
    x, y = h[1], s.mergeKLists(h)
    assert x == y
