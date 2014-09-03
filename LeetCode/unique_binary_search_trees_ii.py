#!/usr/bin/env python
#coding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _gen(self, nlist):
        if not nlist: return [None]

        ln = len(nlist)
        r = []
        for i in range(ln):
            L = self._gen(nlist[:i])
            R = self._gen(nlist[i+1:])
            for j in L:
                for k in R:
                    root = TreeNode(nlist[i])
                    root.left = j
                    root.right = k
                    r.append(root)

        return r 
    # @return a list of tree node
    def generateTrees(self, n):
        return self._gen(range(1, n+1))

def printT(root):
    if not root: return
    printT(root.left),
    print(root.val),
    printT(root.right),

if __name__ == '__main__':
    tlist = Solution().generateTrees(3)
    print([t.val for t in tlist])
    for t in tlist:
        printT(t)
        print('')

