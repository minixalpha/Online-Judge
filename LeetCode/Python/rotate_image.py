#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        lm = len(matrix)
        for i in range(0, lm/2):
            cl = lm - 2 * i - 1
            for j in range(i, i + cl):
                k = j - i
                t = matrix[i][j]
                matrix[i][j] = matrix[i+cl-k][i]
                matrix[i+cl-k][i] = matrix[i+cl][i+cl-k]
                matrix[i+cl][i+cl-k] = matrix[i+k][i+cl]
                matrix[i+k][i+cl] = t

        return matrix

if __name__ == '__main__':
    s = Solution()
    print(s.rotate([[1,2],[3,4]]))
    print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))
    print(s.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
