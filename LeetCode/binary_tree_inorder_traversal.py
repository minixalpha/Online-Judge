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
    def inorderTraversal(self, root):
        if not root: return []
        s = []
        s.extend(self.inorderTraversal(root.left))
        s.append(root.val)
        s.extend(self.inorderTraversal(root.right))
        return s


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    assert [1,3,2] == s.preorderTraversal(root)
