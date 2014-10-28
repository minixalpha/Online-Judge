#!/usr/bin/env python
#coding: utf-8

#
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        m = {}
        for a in A:
            m[a] = m.get(a,0) + 1

        for a in m:
            if m[a] == 1: return a


if __name__ == '__main__':
    s = Solution()
    assert s.singleNumber([2]) == 2
    assert s.singleNumber([2, 3, 3]) == 2
    assert s.singleNumber([4, 4, 2, 3, 3]) == 2
