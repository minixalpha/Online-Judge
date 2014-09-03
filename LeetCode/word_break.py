#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _wb(self, s, ls, start, dict, cache):
        if cache[start] != None: return cache[start]
        for i in range(start+1, ls+1):
            cs = s[start:i]
            if cs in dict and (i == ls or self._wb(s, ls, i, dict, cache)):
                cache[start] = True
                return True
        cache[start] = False
        return False

    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        ls = len(s)
        cache = [None for i in range(ls)]
        return self._wb(s, ls, 0, dict, cache)


if __name__ == '__main__':
    s = Solution()
    assert True == s.wordBreak("leetcode", ["leet", "code"])

    assert False == s.wordBreak(100 * 'a' + 'b', 
            ["a","aa","aaa","aaaa","aaaaa",
            "aaaaaa","aaaaaaa","aaaaaaaa",
            "aaaaaaaaa","aaaaaaaaaa"])
