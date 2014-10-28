#!/usr/bin/env python
#coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        st, sd = ListNode(0), ListNode(0)
        st.next = head
        t, k = sd, st

        while k.next:
            if k.next.val < x:
                kn = k.next
                k.next = kn.next

                kn.next = t.next
                t.next = kn
                t = kn
            else:
                k = k.next
        t.next = st.next
        return sd.next
    
def pl(h):
    while h:
        print(h.val),
        h = h.next
    print('')
if __name__ == '__main__':
    t = [ListNode(i) for i in [1,4,3,2,5,2]]
    for i in range(len(t)-1):
        t[i].next = t[i+1]
    pl(t[0])
    pl(Solution().partition(t[0], 3))

