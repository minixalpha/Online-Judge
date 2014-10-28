#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        ls = len(s)
        i, j = 0, ls - 1
        while i < ls and s[i] == ' ':
            i += 1
        while j >= 0 and s[j] == ' ':
            j -= 1
        if i > j: return False

        if s[i] == '+' or s[i] == '-':
            i += 1
        if i > j: return False

        hasDot = False
        if s[i] == '.':
            i += 1
            hasDot = True
        if i > j: return False

        if not (s[i].isdigit() or s[i]=='.'): return False

        candidates = map(str, range(0, 10)) + ['.', 'e', '+', '-']
        hasE = False
        while i <= j:
            if not s[i] in candidates:
                return False
            if s[i] == '.':
                if hasDot or hasE: return False
                hasDot = True
            if s[i] == 'e':
                if hasE: return False
                if i == j: return False
                hasE = True
            if s[i] == '+' or s[i] == '-':
                if i-1 < 0 or i+1 > j or s[i-1] != 'e' or not s[i+1].isdigit():
                    return False
            i += 1

        return True


if __name__ == '__main__':
    s = Solution()
    assert True == s.isNumber('0') 
    assert True == s.isNumber(' 0.1 ') 
    assert False == s.isNumber('1 a') 
    assert True == s.isNumber('2e10')
    assert False == s.isNumber('abc') 
    assert False == s.isNumber('e9')
    assert False == s.isNumber(' ')
    assert True == s.isNumber('.1')
    assert False == s.isNumber('.')
    assert False == s.isNumber('0e')
    assert True == s.isNumber('01')
    assert False == s.isNumber('5e')
    assert True == s.isNumber('5e20')
    assert False == s.isNumber('1e.')
    assert False == s.isNumber('6e6.5')
    assert True == s.isNumber(' 005047e+6')
    assert True == s.isNumber(' 005047e-6')
    assert False == s.isNumber( '4e+')
