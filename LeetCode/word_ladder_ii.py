#!/usr/bin/env python
#coding: utf-8
import collections

class Solution:
    def _buildPath(self, preList, root, start, path, pathList):
        path.append(root)
        if root == start:
            pathList.append(path[::-1])
            return
        for node in preList[root]:
            self._buildPath(preList, node, start, list(path), pathList)

    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        chars = map(chr, range(ord('a'), ord('z')+1))
        preList = collections.defaultdict(list)
        curNodes, nextNodes = set([start]), set([])
        dict.add(end)

        while curNodes and not end in curNodes:
            dict -= curNodes
            for node in curNodes:
                for i in range(len(node)):
                    for c in chars:
                        newNode = node[:i] + c + node[i+1:]
                        if newNode in dict:
                            nextNodes.add(newNode)
                            preList[newNode].append(node)
            curNodes, nextNodes = nextNodes, set([])
        pathList = []
        self._buildPath(preList, end, start, [], pathList)
        return pathList


if __name__ == '__main__':
    s = Solution()
    pl = s.findLadders('hit', 'cog', set(["hot","dot","dog","lot","log"]))
    print(pl)
    pl = s.findLadders('hit', 'cog', set([]))
    print(pl)
    pl = s.findLadders('hit', 'hog', set(['hig']))
    print(pl)
    pl = s.findLadders('a','c', set(['a','b','c']))
    print(pl)
    pl = s.findLadders("red", "tax", set(["ted","tex","red","tax","tad","den","rex","pee"]))
    print(pl)
