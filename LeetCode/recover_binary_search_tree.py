#!/usr/bin/env python
#coding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _recover(self, root):
        if not root: return None, None

        lmin, lmax = self._recover(root.left)
        if not lmin: lmin, lmax = root, root
        rmin, rmax = self._recover(root.right)
        if not rmin: rmin, rmax = root, root

        # do not need recover
        if (lmin.val <= root.val and lmax.val <= root.val
            and rmin.val >= root.val and rmax.val >= root.val):
            return lmin, rmax

        # recover
        if lmax.val > root.val:
            lmax.val, root.val = root.val, lmax.val
            self._recover(root.left)
        if rmin.val < root.val:
            rmin.val, root.val = root.val, rmin.val
            self._recover(root.right)
        if lmax.val > root.val:
            lmax.val, root.val = root.val, lmax.val
            self._recover(root.left)

        return lmin, rmax

    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self._recover(root)
        return root

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    assert root.val == s.recoverTree(root).val

    left = TreeNode(0)
    root.left = left
    assert root.val == s.recoverTree(root).val

    right = TreeNode(2)
    root.right = right
    assert root.val == s.recoverTree(root).val

    root.left = right
    root.right = left
    s.recoverTree(root)
    assert root.val == s.recoverTree(root).val

    root = TreeNode(3)
    right = TreeNode(2)
    root.right = right
    rr = TreeNode(1)
    right.right = rr
    root = s.recoverTree(root)
    assert 1 == root.val
    assert 2 == root.right.val
    assert 3 == root.right.right.val
