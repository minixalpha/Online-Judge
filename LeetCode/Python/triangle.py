#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        lt = len(triangle)
        d = [0 for i in range(lt)]

        for i in range(lt):
            for j in range(i, -1, -1):
                if j == 0:
                    d[j] = d[j] + triangle[i][j]
                elif j == i:
                    d[j] = d[j-1] + triangle[i][j]
                else:
                    d[j] = min(d[j-1], d[j]) + triangle[i][j]
        return min(d)

if __name__ == '__main__':
    assert 11 == Solution().minimumTotal([
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
        ])
