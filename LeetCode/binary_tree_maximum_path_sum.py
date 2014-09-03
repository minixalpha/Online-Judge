#!/usr/bin/env python
#coding: utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _mps(self, root):
        if not root: return None, None
        lmps, lms2r  = self._mps(root.left)
        rmps, rms2r  = self._mps(root.right)
        mps = max(
                lmps if lmps else root.val,
                rmps if rmps else root.val,
                root.val,
                root.val + (lms2r if lms2r else 0),
                root.val + (rms2r if rms2r else 0),
                root.val + (rms2r if rms2r else 0) + (lms2r if lms2r else 0)
                )
        ms2r = max(
                root.val,
                root.val + (lms2r if lms2r else 0),
                root.val + (rms2r if rms2r else 0),
                )
        return mps, ms2r


    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        mps, ms2r  = self._mps(root)
        return mps


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert 6 == s.maxPathSum(root)

    root = TreeNode(-1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    assert 1 == s.maxPathSum(root)

    t = [TreeNode(i) for i in [1,-2,-3,1,3,-2,-1]]
    t[0].left, t[0].right = t[1], t[2]
    t[1].left, t[1].right = t[3], t[4]
    t[2].left = t[5]
    t[3].left = t[6]
    assert 3 == s.maxPathSum(t[0])
