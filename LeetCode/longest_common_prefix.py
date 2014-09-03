#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        lcomn = len(strs[0])

        for i in range(1, lcomn + 1):
            comn = strs[0][:i]
            for s in strs:
                if not s.startswith(comn):
                    return comn[:-1]
        return strs[0]


if __name__ == '__main__':
    s = Solution()
    assert '' == s.longestCommonPrefix(['a', 'b'])
    assert 'a' == s.longestCommonPrefix(['a', 'a'])
    assert 'a' == s.longestCommonPrefix(['aa', 'ab'])
    assert 'ab' == s.longestCommonPrefix(['ab', 'ab'])



