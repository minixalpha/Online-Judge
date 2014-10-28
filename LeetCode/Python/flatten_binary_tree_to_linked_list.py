#!/usr/bin/env python
#coding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _flatten(self, root, parent):
        if not root: return []
        x = self._flatten(root.left, root)
        y = self._flatten(root.right, x)
        return [root] + x + y


    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root: return None
        t = self._flatten(root, None)
        pe = t[0]
        for e in t[1:]:
            pe.right = e
            pe.left = None
            pe = e


if __name__ == '__main__':
    t = [TreeNode(i) for i in range(0,7)]
    t[1].left = t[2]
    t[1].right = t[5]
    t[2].left = t[3]
    t[2].right = t[4]
    t[5].right = t[6]
    Solution().flatten(t[1])
    assert None == t[1].left
    assert t[2] == t[1].right
    assert t[3] == t[2].right
    assert None == t[2].left
    assert t[4] == t[3].right
    assert None == t[3].left
    assert t[5] == t[4].right
    assert None == t[4].left
    assert t[6] == t[5].right
    assert None == t[5].left
    assert None == t[6].left
    assert None == t[6].right
