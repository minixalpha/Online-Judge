#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _check(self, board, m, n, word, r, c, visit):
        if not word: return True

        if r < 0 or c < 0 or r >= m or c >= n or visit[r][c]: return False
        if board[r][c] != word[0]: 
            visit[r][c] = 0
            return False
        
        visit[r][c] = 1
        if self._check(board, m, n, word[1:], r+1, c, visit):
            return True
        if self._check(board, m, n, word[1:], r, c+1, visit):
            return True
        if self._check(board, m, n, word[1:], r-1, c, visit):
            return True
        if self._check(board, m, n, word[1:], r, c-1, visit):
            return True
        visit[r][c] = 0
        return False

    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not board or not word: return False
        m, n = len(board), len(board[0])
        i, j = 0, 0

        while i < m:
            j = 0
            while j < n:
                if board[i][j] == word[0]:
                    visit = [[0] * n for k in range(m)]
                    if self._check(board, m, n, word, i, j, visit):
                        return True
                j += 1
            i += 1
        return False
        
if __name__ == '__main__':
    s = Solution()
    board = [
      "ABCE",
      "SFCS",
      "ADEE"
    ]
    assert True == s.exist(board, "ABCCED")
    assert True == s.exist(board, "SEE")
    assert False == s.exist(board, "ABCB")
