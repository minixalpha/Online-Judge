#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        r = 0
        for i in range(0, 32):
            c = 0
            for a in A:
                if (a >> i) & 1:
                    c += 1
            r |= (c % 3) << i
        if r >> 31:
            r = -0x80000000 + (r & 0x7fffffff)
        return r


if __name__ == '__main__':
    s = Solution()
    assert 5 == s.singleNumber([1,2,3,3,1,2,2,1,3,5])
    assert -5 == s.singleNumber([-1,-2,-3,-3,-1,-2,-2,-1,-3,-5])
