#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        la = len(A)
        nstep, nstep_max, cur_max = 0, 0, 0

        for i in range(la):
            if i > nstep_max:
                if cur_max == nstep_max and nstep_max < la-1:
                    return -1
                nstep_max = cur_max
                nstep += 1
            cur_max = max(cur_max, i + A[i])
        return nstep

if __name__ == '__main__':
    s = Solution()
    assert 2 == s.jump([2,3,1,1,4])
    assert 0 == s.jump([2])
    assert 5 == s.jump(
        [8,4,3,4,0,0,9,7,2,3,5,7,3,
        1,1,5,1,8,6,1,1,6,1,1,8,0,4])
    assert 1 == s.jump(
         range(25000, 23698, -1) + [23])
