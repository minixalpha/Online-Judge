#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not grid: 0

        m, n = len(grid), len(grid[0])
        d = [[0] * n for t in range(m)]
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    d[i][j] = min(d[i-1][j], d[i][j-1]) + grid[i][j]
                elif i - 1 >= 0:
                    d[i][j] = d[i-1][j] + grid[i][j]
                else:
                    d[i][j] = d[i][j-1] + grid[i][j]
        return d[m-1][n-1]


if __name__ == '__main__':
    assert 3 == Solution().minPathSum([[1,2]])
    assert 2 == Solution().minPathSum([[1,2],[-1,2]])
