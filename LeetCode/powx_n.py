#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        b = 1
        if n > 0: m = n
        else: m = -1 * n
        tm = m

        while m:
            m >>= 1
            b <<= 1
        b >>= 1

        p = 1.0
        while b:
            if b & tm:
                p = p * p * x
            else:
                p = p * p
            b >>= 1
        if n < 0: return 1.0 / p
        else: return p

if __name__ == '__main__':
    s = Solution()
    assert 1024 == s.pow(2, 10)
    assert 9 == s.pow(3, 2)
    assert 1 == s.pow(9, 0)


