#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if not word1: return len(word2)
        if not word2: return len(word1)
        lw1, lw2 = len(word1) + 1, len(word2) + 1

        ed = [[0] * lw2 for i in range(lw1)]
        for i in range(0, lw2):
            ed[0][i] = i
        for i in range(0, lw1):
            ed[i][0] = i

        for i in range(1, lw1):
            for j in range(1, lw2):
                r = 0 if word1[i-1] == word2[j-1] else 1
                ed[i][j] = min(
                        ed[i-1][j-1] + r, 
                        ed[i-1][j] + 1, 
                        ed[i][j-1] + 1)
        return ed[lw1 - 1][lw2 - 1]

if __name__ == '__main__':
    s = Solution()
    assert 1 == s.minDistance('a', 'b')
    assert 0 == s.minDistance('', '')
    assert 1 == s.minDistance('', 'a')
    assert 1 == s.minDistance('a', 'ab')
    assert 1 == s.minDistance('ab', 'a')

