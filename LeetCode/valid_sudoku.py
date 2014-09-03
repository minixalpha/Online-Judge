#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _checkRule1(self, board):
        for row in board:
            x = set([])
            for e in row:
                if e != '.':
                    if e in x: return False
                    x.add(e)
        return True

    def _checkRule2(self, board):
        for col in range(0, 9):
            x = set([])
            for row in range(0, 9):
                e = board[row][col]
                if e != '.':
                    if e in x: return False
                    x.add(e)
        return True

    def _checkRule3(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                x = set([])
                for m in range(3):
                    for n in range(3):
                        e = board[i+m][j+n]
                        if e != '.':
                            if e in x: return False
                            x.add(e)
        return True

    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        r1 = self._checkRule1(board)
        if not r1: return False
        r2 = self._checkRule2(board)
        if not r2: return False
        r3 = self._checkRule3(board)
        if not r3: return False
        return True


if __name__ == '__main__':
    board = [['.'] * 9 for i in range(9)]
    s = Solution()
    assert True == s.isValidSudoku(board)
    board[0][0] = 5
    assert True == s.isValidSudoku(board)
    board[1][1] = 5
    assert False == s.isValidSudoku(board)

