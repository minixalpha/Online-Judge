#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix: return
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        zr, zc = set([]), set([])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zr.add(i)
                    zc.add(j)

        for r in zr:
            for j in range(n):
                matrix[r][j] = 0

        for c in zc:
            for i in range(m):
                matrix[i][c] = 0

if __name__ == '__main__':
    print(Solution().setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]))
                
