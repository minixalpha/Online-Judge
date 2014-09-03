#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _makeR(self, used_col, n):
        r = []
        for i in range(n):
            cr = ['.'] * n
            for j in range(n):
                if used_col[i] == j:
                    cr[j] = 'Q'
                    break
            r.append(''.join(cr))
        return r

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
            return r.append(self._makeR(used_col, n))

        for i in range(n):
            if (not i in used_col 
                and not self._conflict(cur_row, i, used_col, n)):
                used_col.append(i)
                self._solve(r, used_col, cur_row + 1, n)
                used_col.pop()

    # @return a list of lists of string
    def solveNQueens(self, n):
        result, used_col = [], []
        self._solve(result, used_col, 0, n)
        return result

if __name__ == '__main__':
    s = Solution()
    for n in range(0, 5):
        print(s.solveNQueens(n))
