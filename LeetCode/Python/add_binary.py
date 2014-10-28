#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        c = '0'
        r = []
        la, lb = len(a) - 1, len(b) - 1
        i, j = la, lb
        while i >= 0 or j >= 0:
            x = a[i] if i >= 0 else '0'
            y = b[j] if j >= 0 else '0'
            if x == '1' and y == '1':
                r.append(c)
                c = '1'
            elif x == '1' or y == '1':
                r.append('0' if c == '1' else '1')
            else:
                r.append(c)
                c = '0'
            j -= 1
            i -= 1
        if c == '1':
            r.append(c)

        return ''.join(r[::-1])

if __name__ == '__main__':
    s = Solution()
    assert '100' == s.addBinary('11', '1')
    assert '100' == s.addBinary('1', '11')
    assert '0' == s.addBinary('0', '0')

