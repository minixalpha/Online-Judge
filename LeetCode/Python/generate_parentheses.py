#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _gen(self, r, cr, n_left, n_combined, n):
        if n_combined == n:
            r.append(''.join(cr))
            return

        if n_left < n - n_combined:
            cr.append('(')
            self._gen(r, cr, n_left+1, n_combined, n)
            cr.pop()

        if n_left > 0:
            cr.append(')')
            self._gen(r, cr, n_left-1, n_combined+1, n)
            cr.pop()

    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        r = []
        self._gen(r, [], 0, 0, n)
        return r


if __name__ == '__main__':
    s = Solution()
    #print(s.generateParenthesis(3))
    #print(s.generateParenthesis(2))
    #print(s.generateParenthesis(1))
    print(len(s.generateParenthesis(6)))
