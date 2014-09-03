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
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root: return False
        if not root.left and not root.right: return root.val == sum
        sub_sum = sum - root.val
        return (self.hasPathSum(root.left, sub_sum) 
                or self.hasPathSum(root.right, sub_sum))

if __name__ == '__main__':
    s = Solution()
    assert False == s.hasPathSum(None, 0)
    assert True == s.hasPathSum(TreeNode(1), 1)
    root = TreeNode(1)
    root.left = t0 = TreeNode(2)
    assert False == s.hasPathSum(root, 1)
    t0.left = t1 = TreeNode(3)
    t1.left = t2 = TreeNode(4)
    t2.left = TreeNode(5)
    assert False == s.hasPathSum(root, 6)
