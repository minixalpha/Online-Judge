#!/usr/bin/env python
#coding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _sum(self, root, s):
        if not root: return 0
        accu = 10 * s + root.val
        if not root.left and not root.right:
            return accu
        
        ls, rs = 0, 0
        if root.left:
            ls = self._sum(root.left, accu)
        if root.right:
            rs = self._sum(root.right, accu)
        return ls + rs

    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self._sum(root, 0)


if __name__ == '__main__':
    t = [TreeNode(x) for x in range(0,4)]
    t[1].left = t[2]
    assert 12 == Solution().sumNumbers(t[1])
    t[1].right = t[3]
    assert 25 == Solution().sumNumbers(t[1])
