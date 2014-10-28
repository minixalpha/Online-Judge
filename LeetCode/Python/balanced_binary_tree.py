#!/usr/bin/env python
#coding: utf-8

## Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def setHeight(self, root):
        if not root: return 0
        leftH = self.setHeight(root.left)
        rightH = self.setHeight(root.right)
        root.val = max(leftH, rightH) + 1
        return root.val
    
    def _isBalanced(self, root):
        if not root: return True
        if not root.left and not root.right: return True
        if not root.left and root.right: return root.right.val == 1
        if root.left and not root.right: return root.left.val == 1

        return (self._isBalanced(root.left) and self._isBalanced(root.right)
                and (abs(root.left.val - root.right.val) <= 1))

    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        self.setHeight(root)
        return self._isBalanced(root)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert True == s.isBalanced(root)
