#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _add(self, rowSet, colSet, cubSet, i, j, e):
        rowSet[i].add(e)
        colSet[j].add(e)
        cubSet[i/3][j/3].add(e)

    def _remove(self, rowSet, colSet, cubSet, i, j, e):
        rowSet[i].remove(e)
        colSet[j].remove(e)
        cubSet[i/3][j/3].remove(e)
        
    def _solve(self, board, totalSet, rowSet, colSet, cubSet, ptList, k):
        if k >= len(ptList): return True
        rowN, colN = len(board), len(board[0])
        i, j = ptList[k]
        candiset = (totalSet - (rowSet[i] | colSet[j] | cubSet[i/3][j/3]))
        if not candiset: return False

        for e in candiset:
            board[i][j] = e
            self._add(rowSet, colSet, cubSet, i, j, e)
            sub = self._solve(board, totalSet, rowSet, colSet, cubSet, ptList, k+1)
            if sub: return True
            else: self._remove(rowSet, colSet, cubSet, i, j, e)
        return False

    def _getRCSet(self, board):
        rowN, colN = len(board), len(board[0])
        rowSet = [set() for i in range(rowN)]
        colSet = [set() for i in range(colN)]
        cubSet = [[set() for i in range(3)] for j in range(3)]
        ptList = []

        for i in range(rowN):
            for j in range(colN):
                if board[i][j] != '.':
                    self._add(rowSet, colSet, cubSet, i, j, board[i][j])
                else:
                    ptList.append((i,j))
        return rowSet, colSet, cubSet, ptList


    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        if not board: return 

        rowN, colN = len(board), len(board[0])
        totalSet = set(map(str, range(1,10)))
        rowSet, colSet, cubSet, ptList = self._getRCSet(board)
        if not ptList: return
        self._solve(board, totalSet, rowSet, colSet, cubSet, ptList, 0)

        
if __name__ == '__main__':
    s = Solution()
    board = [
            "53..7....",
            "6..195...",
            ".98....6.",
            "8...6...3",
            "4..8.3..1",
            "7...2...6",
            ".6....28.",
            "...419..5",
            "....8..79"
            ]
    lboard = [list(i) for i in board]
    s.solveSudoku(lboard)

    for i in lboard:
        print(i)
