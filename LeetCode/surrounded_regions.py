#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _bfs(self, board, cr, cc, row, col, visit, live):
        if cr < 0 or cr >= row or cc < 0 or cc >= col: return
        if visit[cr][cc]: return

        visit[cr][cc], live[cr][cc] = True, True
        queue = [(cr,cc)]
        while queue:
            cr, cc = queue[0]
            tneighbor = [(cr-1,cc), (cr+1,cc), (cr,cc-1), (cr,cc+1)]
            neighbor = [(i,j) for i, j in tneighbor 
                    if (i>=0 and j>=0 and i <row and j <col
                        and not visit[i][j]
                        and board[i][j] == 'O')]
            for i, j in neighbor:
                visit[i][j] = True
                live[i][j] = True
            queue = queue[1:] + neighbor

    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board: return
        lboard = [list(b) for b in board]

        r, c = len(lboard), len(lboard[0])
        visit = [[False] * c for i in range(r)]
        live = [[False] * c for i in range(r)]

        for cr in [0, r-1]:
            for cc in range(c):
                if lboard[cr][cc] == 'O':
                    self._bfs(lboard, cr, cc, r, c, visit, live)

        for cc in [0, c-1]:
            for cr in range(r):
                if lboard[cr][cc] == 'O':
                    self._bfs(lboard, cr, cc, r, c, visit, live)

        for i in range(r):
            for j in range(c):
                if lboard[i][j] == 'O' and not live[i][j]:
                    lboard[i][j] = 'X'
        for i in range(r):
            board[i] = ''.join(lboard[i])

if __name__ == '__main__':
    board = [
            'XXXX',
            'XOOX',
            'XXOX',
            'XOXX'
            ]
    s = Solution()
    board = ["XOOOOOOOOOOOOOOOOOOO","OXOOOOXOOOOOOOOOOOXX","OOOOOOOOXOOOOOOOOOOX","OOXOOOOOOOOOOOOOOOXO","OOOOOXOOOOXOOOOOXOOX","XOOOXOOOOOXOXOXOXOXO","OOOOXOOXOOOOOXOOXOOO","XOOOXXXOXOOOOXXOXOOO","OOOOOXXXXOOOOXOOXOOO","XOOOOXOOOOOOXXOOXOOX","OOOOOOOOOOXOOXOOOXOX","OOOOXOXOOXXOOOOOXOOO","XXOOOOOXOOOOOOOOOOOO","OXOXOOOXOXOOOXOXOXOO","OOXOOOOOOOXOOOOOXOXO","XXOOOOOOOOXOXXOOOXOO","OOXOOOOOOOXOOXOXOXOO","OOOXOOOOOXXXOOXOOOXO","OOOOOOOOOOOOOOOOOOOO","XOOOOXOOOXXOOXOXOXOO"]
    s.solve(board)
    print(board)
