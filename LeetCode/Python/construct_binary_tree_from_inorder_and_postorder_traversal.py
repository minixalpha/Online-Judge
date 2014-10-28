#!/usr/bin/env python
#coding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder: return None
        root = TreeNode(postorder[-1])
        root_i = inorder.index(postorder[-1])
        
        PL = postorder[:root_i]
        PR = postorder[root_i:-1]
        IL = inorder[:root_i]
        IR = inorder[root_i + 1:]

        L = self.buildTree(IL, PL)
        R = self.buildTree(IR, PR)

        root.left = L
        root.right = R
        return root

if __name__ == '__main__':
    s = Solution()
    t = s.buildTree([2,1,3], [2,3,1])
    assert 1 == t.val    
    assert 2 == t.left.val
    assert 3 == t.right.val

