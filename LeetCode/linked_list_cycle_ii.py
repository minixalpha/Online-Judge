#!/usr/bin/env python
#coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        visited = set([])
        h = head
        while h:
            if h in visited:
                return h
            else:
                visited.add(h)
            h = h.next

        return None
