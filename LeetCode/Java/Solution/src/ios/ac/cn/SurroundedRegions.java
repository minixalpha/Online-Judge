package ios.ac.cn;

import java.util.LinkedList;

public class SurroundedRegions {
	private static final char HOLDER = '+';
	private int mRow;
	private int mCol;

	public void solve(char[][] board) {
		mark(board);
		clear(board);
		recover(board);
	}

	private void mark(char[][] board) {
		mRow = board.length;
		if (mRow > 0) {
			mCol = board[0].length;
		}
		for (int i = 0; i < mCol; i++) {
			markAtPosBFS(board, 0, i);
		}
		for (int i = 0; i < mCol; i++) {
			markAtPosBFS(board, mRow - 1, i);
		}
		for (int i = 1; i < mRow - 1; i++) {
			markAtPosBFS(board, i, 0);
		}
		for (int i = 1; i < mRow - 1; i++) {
			markAtPosBFS(board, i, mCol - 1);
		}
	}

	private class Pair {
		public int mRow;
		public int mCol;

		public Pair(int row, int col) {
			mRow = row;
			mCol = col;
		}
	}

	private void markAtPosBFS(char[][] board, int r, int c) {
		LinkedList<Pair> queue = new LinkedList<>();
		addToQueue(board, r, c, queue);
		while (queue.isEmpty() == false) {
			Pair pair = queue.remove();
			r = pair.mRow;
			c = pair.mCol;
			addToQueue(board, r + 1, c, queue);
			addToQueue(board, r - 1, c, queue);
			addToQueue(board, r, c + 1, queue);
			addToQueue(board, r, c - 1, queue);
		}
	}

	private void addToQueue(char[][] board, int r, int c, LinkedList<Pair> queue) {
		if (needMark(board, r, c)) {
			board[r][c] = HOLDER;
			queue.add(new Pair(r, c));
		}
	}

	private boolean needMark(char[][] board, int r, int c) {
		if (r < 0 || c < 0 || r >= mRow || c >= mCol || board[r][c] != 'O') {
			return false;
		} else {
			return true;
		}
	}

	private void clear(char[][] board) {
		for (int i = 0; i < mRow; i++) {
			for (int j = 0; j < mCol; j++) {
				if (board[i][j] == 'O') {
					board[i][j] = 'X';
				}
			}
		}
	}

	private void recover(char[][] board) {
		for (int i = 0; i < mRow; i++) {
			for (int j = 0; j < mCol; j++) {
				if (board[i][j] == HOLDER) {
					board[i][j] = 'O';
				}
			}
		}
	}

	// Stack Overflow
	@Deprecated
	private void markAtPosDFS(char[][] board, int r, int c) {
		if (r < 0 || c < 0 || r >= mRow || c >= mCol || board[r][c] != 'O') {
			return;
		}
		board[r][c] = HOLDER;
		markAtPosBFS(board, r, c + 1);
		markAtPosBFS(board, r, c - 1);
		markAtPosBFS(board, r + 1, c);
		markAtPosBFS(board, r - 1, c);
	}

}
