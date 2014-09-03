#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _index(self, L, c):
        x = -1
        for i in L:
            x += 1
            if i == c:
                return x
        return -1

    # @return an integer
    def lengthOfLongestSubstring(self, s):
        cl = ml = 0
        cset = []
        for c in s:
            i = self._index(cset, c)
            if i >= 0:
                if cl > ml: 
                    ml = cl
                cset = cset[i+1:]
                cset.append(c)
                cl = cl - i
            else:
                cset.append(c)
                cl += 1
        if cl > ml:ml = cl
        return ml


if __name__ == '__main__':
    s = Solution()
    assert 0 == s.lengthOfLongestSubstring('')
    assert 1 == s.lengthOfLongestSubstring('bbbb')
    assert 3 == s.lengthOfLongestSubstring('abcabcbb')
    assert 4 == s.lengthOfLongestSubstring('abcad')
