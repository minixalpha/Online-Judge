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
    def minDepth(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        ld = self.minDepth(root.left)
        rd = self.minDepth(root.right)
        return min(ld,rd) + 1

if __name__ == '__main__':
    t = [TreeNode(i) for i in range(10)]
    s = Solution()
    assert 1 == s.minDepth(t[0])

    t[0].left = t[1]
    assert 2 == s.minDepth(t[0])

    t[0].right = t[2]
    assert 2 == s.minDepth(t[0])

    t[1].left = t[3]
    assert 2 == s.minDepth(t[0])

