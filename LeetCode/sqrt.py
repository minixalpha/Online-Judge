#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        guess = x
        while guess * guess > x:
            guess = (guess + x / guess) / 2

        return guess

if __name__ == '__main__':
    s = Solution()
    assert 19 == s.sqrt(19 * 19)
    assert 1 == s.sqrt(1)
    assert 1 == s.sqrt(2)
