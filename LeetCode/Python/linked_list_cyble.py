#!/usr/bin/env python
#coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        visited = set([])
        h = head
        while h:
            if h in visited:
                return True
            else:
                visited.add(h)
            h = h.next

        return False

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    assert False == s.hasCycle(head)

    head.next = ListNode(2)
    assert False == s.hasCycle(head)

    head.next.next = head.next
    assert True == s.hasCycle(head)

        

