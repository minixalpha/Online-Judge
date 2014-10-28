#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        d = [([0]*n) for i in range(m)]
        d[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    d[i][j] += d[i-1][j]
                if j - 1 >= 0:
                    d[i][j] += d[i][j-1]
        return d[m-1][n-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(1,1))
    print(Solution().uniquePaths(1,2))
    print(Solution().uniquePaths(2,2))
    print(Solution().uniquePaths(3,7))

