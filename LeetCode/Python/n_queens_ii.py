#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _conflict(self, row, col, used_col, n):
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if used_col[i] == j: return True
            i -= 1
            j += 1

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if used_col[i] == j: return True
            i -= 1
            j -= 1
        return False

    def _solve(self, r, used_col, cur_row, n):
        if cur_row == n: 
            r[0] += 1
            return

        for i in range(n):
            if (not i in used_col 
                and not self._conflict(cur_row, i, used_col, n)):
                used_col.append(i)
                self._solve(r, used_col, cur_row + 1, n)
                used_col.pop()

    # @return a list of lists of string
    def totalNQueens(self, n):
        if not n: return 0
        result, used_col = [0], []
        self._solve(result, used_col, 0, n)
        return result[0]

if __name__ == '__main__':
    s = Solution()
    for n in range(0, 9):
        print(s.totalNQueens(n))
