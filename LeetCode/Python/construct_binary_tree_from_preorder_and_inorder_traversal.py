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
    def buildTree(self, preorder, inorder):
        if not preorder: return None
        root = TreeNode(preorder[0])
        root_i = inorder.index(preorder[0])
        
        PL = preorder[1:root_i+1]
        PR = preorder[root_i+1:]
        IL = inorder[:root_i]
        IR = inorder[root_i + 1:]

        L = self.buildTree(PL, IL)
        R = self.buildTree(PR, IR)

        root.left = L
        root.right = R
        return root

if __name__ == '__main__':
    s = Solution()
    t = s.buildTree([1,2,3], [2,1,3])
    assert 1 == t.val    
    assert 2 == t.left.val
    assert 3 == t.right.val

