#!/usr/bin/env python
#coding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _pathSum(self, root, sum, accu, accuList):
        if not root.left and not root.right:
            if accu + root.val == sum: return [accuList + [root.val]]
            else: return []
        
        L, R = [], []
        a, b = accu + root.val, accuList + [root.val]
        if root.left:
            L = self._pathSum(root.left, sum, a, b)
        if root.right:
            R = self._pathSum(root.right, sum, a, b)
        r = []
        if L: 
            for x in L:
                r.append(x)
        if R: 
            for x in R:
                r.append(x)
        return r

    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if not root: return []
        return self._pathSum(root, sum, 0, [])

if __name__ == '__main__':
    s = Solution()
    t = [TreeNode(i) for i in [5,4,8,11,13,4,7,2,5,1]]
    t[0].left, t[0].right = t[1], t[2]
    t[1].left = t[3]
    t[2].left, t[2].right = t[4], t[5]
    t[3].left, t[3].right = t[6], t[7]
    t[5].left, t[5].right = t[8], t[9]
    print(s.pathSum(t[0], 22))
