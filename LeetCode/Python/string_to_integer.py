#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return an integer
    def atoi(self, str):
        if not str: return 0

        i, ls = 0, len(str)
        if ls == 0: return 0
        
        while i < ls and str[i] == ' ':
            i += 1

        sign = 1
        if i < ls and str[i] == '+':
            i += 1
        elif i < ls and str[i] == '-':
            sign = -1
            i += 1

        n = 0

        if i < ls and not (str[i] >= '0' and str[i] <= '9'):
            return 0
        
        z0 = ord('0')
        while i < ls:
            if not (str[i] >= '0' and str[i] <= '9'): break
            n = n * 10 + ord(str[i]) - z0
            i += 1
        
        r = n * sign
        if r > 0 and r > 2147483647: r = 2147483647
        if r < 0 and r < -2147483648: r = -2147483648
        return r

if __name__ == '__main__':
    s = Solution()
    assert 0 == s.atoi(None)
    assert 0 == s.atoi('')
    assert 0 == s.atoi('+')
    assert 0 == s.atoi('-')
    assert 10 == s.atoi('10')
    assert 10 == s.atoi('+10')
    assert -10 == s.atoi('-10')
    assert 10 == s.atoi('0010')
    assert 10 == s.atoi('10a32')
    assert 0 == s.atoi('+-2')
    assert 10 == s.atoi('      010')
    assert 10 == s.atoi('     +0010')
    assert 2147483647 == s.atoi('2147483648')
