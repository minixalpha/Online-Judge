#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = 1
        if dividend < 0:
            dividend = -dividend
            sign = - sign
        if divisor < 0:
            divisor = -divisor
            sign = - sign
        
        curN, res = 0, 0
        for i in range(31, -1, -1):
            curN <<= 1
            curN |= ((dividend >> i) & 1)

            res <<= 1
            if curN >= divisor:
                curN -= divisor
                res |= 1
            
        return res if sign > 0 else 0-res


if __name__ == '__main__':
    s = Solution()
    assert -1 == s.divide(-1, 1)
    assert 0 == s.divide(0, 1)
    assert 0 == s.divide(0, -1)
    assert 1 == s.divide(3, 2)
    assert 1 == s.divide(3, 3)
    assert 0 == s.divide(3, 4)
    assert 2147483647 == s.divide(2147483647, 1)
