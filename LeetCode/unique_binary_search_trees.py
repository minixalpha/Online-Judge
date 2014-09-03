#!/usr/bin/env python
#coding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return an integer
    def numTrees(self, n):
        if n <= 1: return 1

        nt = [1, 1]
        for i in range(2, n+1):
            s = 0
            for j in range(1, i+1):
                s += nt[j-1] * nt[i-j]
            nt.append(s)
        return nt[n]
