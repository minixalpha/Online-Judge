#!/usr/bin/env python
#coding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def _con(self, child, parent):
        if not child:
            return

        if parent:
            if child == parent.left:
                child.next = parent.right
            else:
                child.next = parent.next.left if parent.next else None

        self._con(child.left, child)
        self._con(child.right, child)

    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        self._con(root, None)
        

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    s = Solution()
    s.connect(n1)

    assert n1.next == None
    assert n2.next == n3
    assert n3.next == None
    assert n4.next == n5
    assert n5.next == n6
    assert n6.next == n7
    assert n7.next == None
