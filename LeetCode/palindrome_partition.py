#!/usr/bin/env python
#coding: utf-8


class Solution:
    def _parti(self, s, start, ls):
        begin = start
        if start == ls: return [[]]

        r = []
        while begin < ls:
            if self._ispalindrome(s, start, begin):
                sub_r = self._parti(s, begin+1, ls)
                for sub in sub_r:
                    r.append([s[start:begin+1]] + sub)
            begin += 1
        return r

    def _ispalindrome(self, s, begin, end):
        while begin < end:
            if s[begin] != s[end]: return False
            begin += 1
            end -= 1
        return True

    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s: return []
        ls = len(s)
        return self._parti(s, 0, ls)


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))
    print(s.partition(""))
    print(s.partition("ab"))
    print(s.partition("bb"))
