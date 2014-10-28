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
    def levelOrder(self, root):
        if not root: return []
        p = []
        q = [root]
        while q:
            p.append([t for t in q])
            tq = q
            q = []
            for t in tq:
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
        return p

    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        level = self.levelOrder(root)
        for le in level:
            for i in range(len(le)-1):
                le[i].next = le[i+1]

        

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n7 = TreeNode(7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n7

    s = Solution()
    s.connect(n1)

    assert n1.next == None
    assert n2.next == n3
    assert n3.next == None
    assert n4.next == n5
    assert n5.next == n7
    assert n7.next == None
