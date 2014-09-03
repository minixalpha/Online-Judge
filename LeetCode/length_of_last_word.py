#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        ls = len(s) - 1
        while ls >= 0 and s[ls] == ' ':
            ls -= 1
        sum = 0
        while ls >= 0 and s[ls] != ' ':
            ls -= 1
            sum += 1
        return sum

if __name__ == '__main__':
    s = Solution()
    assert 0 == s.lengthOfLastWord('      ')
    assert 0 == s.lengthOfLastWord('')
    assert 1 == s.lengthOfLastWord('a')
    assert 2 == s.lengthOfLastWord('ab')
    assert 5 == s.lengthOfLastWord('Hello World')


