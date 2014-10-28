#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _getList(self, start, row, col, matrix):
        cs = []

        for i in range(col):
            cs.append(matrix[start][start+i])
        for i in range(1,row):
            cs.append(matrix[start+i][start+col-1])
        
        if row > 1:
            for i in range(1,col):
                cs.append(matrix[start+row-1][start+col-1-i])
        
        if col > 1:
            for i in range(1,row-1):
                cs.append(matrix[start+row-1-i][start])
        return cs

    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if not matrix: return []

        rowN, colN = len(matrix), len(matrix[0])
        n = (1 + min(rowN, colN)) / 2

        result = []
        for i in range(n):
            cs = self._getList(i, rowN - 2 * i, colN - 2 * i, matrix)
            result.extend(cs)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([]))
    print(s.spiralOrder([[]]))
    print(s.spiralOrder(
        [ [1],
        ]))
    print(s.spiralOrder(
        [ [1, 2, 3 ],
          [4, 5, 6 ],
          [7, 8, 9 ]
        ]))
    print(s.spiralOrder(
        [ [1, 2 ],
          [4, 5 ],
          [7, 8 ]
        ]))
    print(s.spiralOrder(
        [ [1, 2, 3 ],
        ]))
    print(s.spiralOrder(
        [ [1],
          [4],
          [7]
        ]))
