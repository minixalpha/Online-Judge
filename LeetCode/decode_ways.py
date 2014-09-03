#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _nd(self, s, i, cache, ls):
        if i >= ls: return 1
        if i in cache: return cache[i]
        x, y = 0, 0

        if s[i] >= '1' and s[i] <= '9':
            x = self._nd(s, i+1, cache, ls)

        if i + 1 < ls:
            if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
                y = self._nd(s, i+2, cache, ls)
        cache[i] = x + y
        return cache[i]


    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s: return 0
        ls = len(s)
        return self._nd(s, 0, {}, ls)


if __name__ == '__main__':
    s = Solution()
    assert 2 == s.numDecodings("12")
    assert 1 == s.numDecodings("1")
    assert 1 == s.numDecodings("27")
    assert 2 == s.numDecodings("26")
    assert 0 == s.numDecodings("0")
