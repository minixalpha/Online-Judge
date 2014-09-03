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
        h = head

        while h:
            nh = h.next
            while nh and nh.val == h.val:
                nh = nh.next
            h.next = nh
            h = h.next
        return head

if __name__ == '__main__':
    s1 = ListNode(1)
    s2 = ListNode(1)
    s3 = ListNode(2)
    s1.next = s2
    s2.next = s3

    s = Solution()
    s1 = s.deleteDuplicates(s1)
    assert s3 == s1.next
    assert None == s3.next
