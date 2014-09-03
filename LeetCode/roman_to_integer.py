#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return an integer
    def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ls, r, lens = 0, 0, len(s)
        while ls < lens - 1:
            sa = s[ls]
            a = d[sa]
            sb = s[ls + 1]
            b = d[sb]

            if a == b:
                r += (a+b)
                if ls + 2 < lens:
                    sc = s[ls + 2]
                    c = d[sc]
                    if a == c:
                        r += c
                        ls += 1
                ls += 2
                continue

            if ((sa == 'I' and sb != 'V' and sb != 'X')
                or (sa == 'X' and sb != 'L' and sb != 'C')
                or (sa == 'C' and sb != 'D' and sb != 'M')
                or (sa == 'M' or sa == 'D' or sa == 'V' or sa == 'L')
                ):
                r += a
                ls += 1
                continue

            if a > b:
                r += (a + b)
            else:
                r += (b - a)
            ls += 2
        if ls == len(s) - 1:
            r += d[s[ls]] 
        return r

if __name__ == '__main__':
    s = Solution()
    assert 1 == s.romanToInt('I')
    assert 2 == s.romanToInt('II')
    assert 3 == s.romanToInt('III')
    assert 4 == s.romanToInt('IV')
    assert 5 == s.romanToInt('V')
    assert 6 == s.romanToInt('VI')
    assert 7 == s.romanToInt('VII')
    assert 8 == s.romanToInt('VIII')
    assert 9 == s.romanToInt('IX')
    assert 10 == s.romanToInt('X')
    assert 11 == s.romanToInt('XI')
    assert 65 == s.romanToInt('LXV')
    assert 3999 == s.romanToInt('MMMCMXCIX')
    assert 1476 == s.romanToInt('MCDLXXVI')
    assert 2541 == s.romanToInt('MMDXLI')
    assert 1884 == s.romanToInt('MDCCCLXXXIV')
    assert 709 == s.romanToInt('DCCIX')
    assert 1695 == s.romanToInt('MDCXCV')
    assert 3586 == s.romanToInt('MMMDLXXXVI')
