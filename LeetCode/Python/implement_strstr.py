#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if haystack == None or needle == None: return None

        m, n = len(haystack), len(needle)
        if m == n == 0: return ""

        i = 0
        while i < m:
            if m - i < n: return None
            j, k = 0, i
            while j < n and k < m:
                if haystack[k] != needle[j]: break
                k += 1
                j += 1
            if j == n: return haystack[i:]
            i += 1
        return None

if __name__ == '__main__':
    s = Solution()
    assert None == s.strStr(None, None)
    assert None == s.strStr("ab", None)
    assert None == s.strStr(None, "ab")
    assert None == s.strStr("abcd", "e")
    assert "bac" == s.strStr("abac", "b")
    assert "ab" == s.strStr("ab", "ab")
    assert "" == s.strStr("", "")
