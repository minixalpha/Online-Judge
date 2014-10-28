#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if start == end: return 0
        dict.add(end)
        curWords, nextWords = set([start]), set([])
        chars = map(chr, range(ord('a'), ord('z')+1))
        layer = 1

        while curWords:
            dict -= curWords
            for head in curWords:
                for i in range(len(head)):
                    for e in chars:
                        nb = head[:i] + e + head[i+1:]
                        if nb in dict: 
                            if nb == end: return layer + 1
                            nextWords.add(nb)
            curWords, nextWords = nextWords, set([])
            layer += 1
        return 0

if __name__ == '__main__':
    s = Solution()
    pl = s.ladderLength('hit', 'cog', set([]))
    assert 0 == pl
    pl = s.ladderLength('hit', 'hog', set(['hig']))
    assert 3 == pl
    pl = s.ladderLength('hit', 'cog', set(["hot","dot","dog","lot","log"]))
    assert 5 == pl
    pl = s.ladderLength('a','c', set(['a','b','c']))
    assert 2 == pl
