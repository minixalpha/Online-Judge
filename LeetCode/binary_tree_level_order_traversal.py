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
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root: return []
        p = []
        q = [root]
        while q:
            p.append([t.val for t in q])
            tq = q
            q = []
            for t in tq:
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
        return p

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = t = TreeNode(20)
    t.left = TreeNode(15)
    t.right = TreeNode(7)
    print(Solution().levelOrder(root))

