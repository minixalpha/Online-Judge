#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0: 
            return 0
        sign = 1 if x > 0 else -1
        x = sign * x
        sx = str(x)[::-1]
        i = 0
        while sx[i] == '0':
            i += 1
        x2 = int(sx[i:])
        return sign * x2


if __name__ == '__main__':
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(10) == 1
    assert s.reverse(-10) == -1
    assert s.reverse(0) == 0
    assert s.reverse(-0) == 0
