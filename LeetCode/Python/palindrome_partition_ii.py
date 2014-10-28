#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if not s: return 0

        n = len(s)
        mincut = [n-1] * n
        ispalin = [[False] * n for i in range(n)]

        for i in range(n-1, -1, -1):
            mincut[i] = n - 1 - i
            for j in range(i, n):
                if s[i] == s[j] and (j-i<=2 or ispalin[i+1][j-1]):
                    ispalin[i][j] = True
                    if j + 1 == n:
                        mincut[i] = 0
                    elif mincut[j+1] + 1 < mincut[i]:
                        mincut[i] = mincut[j+1] + 1
        return mincut[0]


if __name__ == '__main__':
    s = Solution()
    #assert 1 == s.minCut("aab")
    #assert 0 == s.minCut("a")
    assert 0 == s.minCut("aa")
    assert 1 == s.minCut("aaabaa")
