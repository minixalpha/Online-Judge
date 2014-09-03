#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _com(self, digits, d):
        if not digits: return ['']
        x = d[digits[0]]
        y = self._com(digits[1:], d)
        r = []
        for p in x:
            for q in y:
                r.append(p + q)
        return r

    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        d ={'2':'abc', '3':'def', '4':'ghi',
            '5':'jkl', '6':'mno', '7':'pqrs',
            '8':'tuv', '9':'wxyz'}
        return self._com(digits, d)

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
