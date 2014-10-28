#!/usr/bin/env python
#coding: utf-8

import testutil

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head: return None

        rf = ListNode(0)
        rf.next = head

        h, nh, pins = head, head.next, rf
        while nh:
            if h.val > nh.val:
                h.next = nh.next
                if nh.val < pins.next.val:
                    pins = rf
                while pins.next.val < nh.val:
                    pins = pins.next
                nh.next = pins.next
                pins.next = nh
            else:
                h = nh
            nh = h.next
        return rf.next

if __name__ == '__main__':
    h = testutil.makeL(10)
    testutil.printL(h)
    s = Solution()
    h = s.insertionSortList(h)
    testutil.printL(h)

    h = testutil.makeList([3,2,4])
    testutil.printL(h)
    h = s.insertionSortList(h)
    testutil.printL(h)

    h = testutil.makeList([3,2,1])
    testutil.printL(h)
    h = s.insertionSortList(h)
    testutil.printL(h)

    h = testutil.makeList(range(5000,0,-1))
    h = s.insertionSortList(h)
    testutil.printL(h)

    h = testutil.makeL(5000)
    h = s.insertionSortList(h)
    testutil.printL(h)

    h = testutil.makeList([4,19,14,5,-3,1,8,5,11,15])
    h = s.insertionSortList(h)
    testutil.printL(h)

    h = testutil.makeList([
        -84,142,41,-17,-71,170,186,183,-21,-76,76,10,29,81,112,-39,-6,-43,58,41,111,33,69,97,-38,82,-44,-7,99,135,42,150,149,-21,-30,164,153,92,180,-61,99,-81,147,109,34,98,14,178,105,5,43,46,40,-37,23,16,123,-53,34,192,-73,94,39,96,115,88,-31,-96,106,131,64,189,-91,-34,-56,-22,105,104,22,-31,-43,90,96,65,-85,184,85,90,118,152,-31,161,22,104,-85,160,120,-31,144,115])

    h = s.insertionSortList(h)
    testutil.printL(h)
