#!/usr/bin/env python
#coding: utf-8

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        d = {}
        cnode = UndirectedGraphNode(node.label)
        d[node] = cnode
        q = [node]

        while q:
            x = q.pop()
            cx = d[x]
            for y in x.neighbors:
                if not y in d:
                    cy = UndirectedGraphNode(y.label)
                    d[y] = cy
                    q.append(y)
                else:
                    cy = d[y]
                cx.neighbors.append(cy)
        return cnode

if __name__ == '__main__':
    n0 = UndirectedGraphNode(0)
    n1 = UndirectedGraphNode(1)
    n2 = UndirectedGraphNode(2)

    n0.neighbors = [n1, n2]
    n1.neighbors = [n0, n2]
    n2.neighbors = [n0, n1, n2]

    s = Solution()
    m0 = s.cloneGraph(n0)
    m1, m2 = m0.neighbors
    assert m0.label == 0
    assert m1.label == 1
    assert m2.label == 2
    assert m1.neighbors == [m0, m2]
    assert m2.neighbors == [m0, m1, m2]
