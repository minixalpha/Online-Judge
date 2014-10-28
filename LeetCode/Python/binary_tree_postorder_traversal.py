#!/usr/bin/env python
#coding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if not root: return []
        leftL = self.postorderTraversal(root.left)
        rightL = self.postorderTraversal(root.right)
        return leftL + rightL + [root.val]
