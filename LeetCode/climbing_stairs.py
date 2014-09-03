#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        k = [0, 1, 2]
        i = 3
        while i <= n:
            k.append(k[i-1] + k[i-2])
            i += 1
        return k[n]



if __name__ == '__main__':
    s = Solution()
    assert 1 == s.climbStairs(1)
    assert 2 == s.climbStairs(2)
    assert 3 == s.climbStairs(3)
