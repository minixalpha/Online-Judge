#!/usr/bin/env python
#coding: utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def makeL(n):
    """
    make a single linkedlist: [1, 2, ..., n]
    """
    t = [ListNode(i) for i in range(1, n+1)]
    for i in range(0, n-1):
        t[i].next = t[i+1]
    
    return t[0]

def makeList(ln):
    t = [ListNode(i) for i in ln]
    for i in range(0, len(ln)-1):
        t[i].next = t[i+1]
    
    return t[0]

def printL(ln):
    """
    print single linkedlist
    """
    h = ln
    while h:
        print(h.val),
        h = h.next
    print('')
