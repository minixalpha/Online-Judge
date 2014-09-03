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
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        return max(ld, rd) + 1


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    #root.left = TreeNode(2)
    print(s.maxDepth(root))
