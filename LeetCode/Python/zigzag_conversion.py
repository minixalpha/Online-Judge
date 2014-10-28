#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1: return s
        x = [[] for i in range(nRows)]
        
        i, down = 0, True
        for c in s:
            x[i].append(c)
            if down and i == nRows - 1:
                down = False
            if not down and i == 0:
                down = True
            if down: i += 1
            else: i -= 1
        
        y = [''.join(i) for i in x]
        return ''.join(y)

if __name__ == '__main__':
    s = Solution()
    assert 'PAHNAPLSIIGYIR' == s.convert('PAYPALISHIRING', 3)
    assert 'AB' == s.convert('AB', 1)
