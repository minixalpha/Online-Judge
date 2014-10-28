#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a list of integers
    def grayCode(self, n):
        r = []
        for i in range(2**n):
            r.append((i>>1) ^ i)
        return r

if __name__ == '__main__':
    s = Solution()
    assert [0,1,3,2] == s.grayCode(2)
