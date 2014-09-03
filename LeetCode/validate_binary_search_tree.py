#!/usr/bin/env python
#coding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _valid(self, root):
        if not root: return 0, 0, True
        if not root.left and not root.right: 
            return root.val, root.val, True
        if root.left:
            lmax, lmin, lvalid = self._valid(root.left)
        if root.right:
            rmax, rmin, rvalid = self._valid(root.right)
        
        if root.left and root.right:
            return (rmax, lmin, 
                    lvalid and rvalid 
                    and lmax < root.val and rmin > root.val)
        elif root.left:
            return (root.val, lmin,
                    lvalid and lmax < root.val)
        else:
            return (rmax, root.val,
                    rvalid and rmin > root.val)


    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        _, _, x = self._valid(root)
        return x

if __name__ == '__main__':
    s = Solution()
    t0 = TreeNode(0)
    t1 = TreeNode(-1)
    t0.left = t1
    assert True == s.isValidBST(t0)
