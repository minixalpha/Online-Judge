#!/usr/bin/env python
#coding: utf-8

## Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num: return None
        ln = len(num)
        if ln == 1: return TreeNode(num[0])

        m = ln / 2
        root = TreeNode(num[m])
        root.left = self.sortedArrayToBST(num[:m])
        root.right = self.sortedArrayToBST(num[m+1:])
        return root
