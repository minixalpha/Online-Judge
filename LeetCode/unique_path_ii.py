#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid: return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        d = [([0]*n) for i in range(m)]
        d[0][0] = 1 if obstacleGrid[0][0] != 1 else 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1: continue
                if i - 1 >= 0 and obstacleGrid[i-1][j] != 1:
                    d[i][j] += d[i-1][j]
                if j - 1 >= 0 and obstacleGrid[i][j-1] != 1:
                    d[i][j] += d[i][j-1]
        return d[m-1][n-1]

if __name__ == '__main__':
    obstacleGrid = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
            ]
    assert 2 == Solution().uniquePathsWithObstacles(obstacleGrid)
    obstacleGrid = [[1]]
    assert 0 == Solution().uniquePathsWithObstacles(obstacleGrid)
    obstacleGrid = [[0,1]]
    assert 0 == Solution().uniquePathsWithObstacles(obstacleGrid)
