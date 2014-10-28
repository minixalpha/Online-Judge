#!/usr/bin/env python
#coding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _traverseL(self, root):
        if not root: return [None]
        return ([root.val] 
                + self._traverseL(root.left) 
                + self._traverseL(root.right))

    def _traverseR(self, root):
        if not root: return [None]
        return ([root.val] 
                + self._traverseR(root.right) 
                + self._traverseR(root.left))

    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root: return True
        lt = self._traverseL(root.left)
        rt = self._traverseR(root.right)
        return lt == rt


if __name__ == '__main__':
    root = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t5 = TreeNode(4)
    t6 = TreeNode(4)
    t7 = TreeNode(3)
    root.left = t2
    root.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    assert True == Solution().isSymmetric(root)
