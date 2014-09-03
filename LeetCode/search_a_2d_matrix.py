#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if not matrix: return False

        m, n = len(matrix), len(matrix[0])
        i, j = 0, m - 1
        while i <= j:
            k = (i + j) / 2
            if matrix[k][0] == target: return True
            elif matrix[k][0] < target:
                i = k + 1
            else:
                j = k - 1

        if matrix[k][0] < target:
            p = k
        else:
            p = k - 1
        if p < 0: return False
        
        i, j = 0, n - 1
        while i <= j:
            k = (i + j) / 2
            if matrix[p][k] == target: return True
            elif matrix[p][k] < target: 
                i = k + 1
            else:
                j = k - 1
        return False

if __name__ == '__main__':
    matrix = [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,50]
            ]
    s = Solution()
    assert True == s.searchMatrix(matrix, 11)
    assert True == s.searchMatrix(matrix, 3)
    assert True == s.searchMatrix(matrix, 1)
    assert True == s.searchMatrix(matrix, 50)
    assert False == s.searchMatrix(matrix, -1)
    assert False == s.searchMatrix(matrix, 51)
