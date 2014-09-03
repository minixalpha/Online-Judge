#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        d = [[0] * n for i in range(n)]
        i, k, tn = 0, 1, n / 2
        while i <= tn:
            for j in range(i, n - i):
                d[i][j] = k
                k += 1
            for j in range(i+1, n - i):
                d[j][n-i-1] = k
                k += 1
            for j in range(n - i - 2, i-1, -1):
                d[n-i-1][j] = k
                k += 1
            for j in range(n - i - 2, i, -1):
                d[j][i] = k
                k += 1

            i += 1
        return d

if __name__ == '__main__':
    for i in (Solution().generateMatrix(5)):
        print(i)
