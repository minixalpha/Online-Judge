package ios.ac.cn;

public class ValidSudoku {
	public boolean isValidSudoku(char[][] board) {
		return checkRow(board) && checkCol(board) && checkArea(board);
	}

	private boolean setAndCheck(boolean[] used, char c) {
		if (c != '.') {
			if (used[c - '0'] != true) {
				used[c - '0'] = true;
			} else {
				return false;
			}
		}
		return true;
	}

	private boolean checkRow(char[][] board) {
		for (int i = 0; i < board.length; i++) {
			boolean[] used = new boolean[10];
			for (int j = 0; j < board[0].length; j++) {
				if (!setAndCheck(used, board[i][j])) {
					return false;
				}
			}
		}
		return true;
	}

	private boolean checkCol(char[][] board) {
		for (int i = 0; i < board[0].length; i++) {
			boolean[] used = new boolean[10];
			for (int j = 0; j < board.length; j++) {
				if (!setAndCheck(used, board[j][i])) {
					return false;
				}
			}
		}
		return true;
	}

	private boolean checkArea(char[][] board) {
		for (int i = 0; i < 9; i += 3) {
			for (int j = 0; j < 9; j += 3) {
				boolean[] used = new boolean[10];
				for (int a = 0; a < 3; a++) {
					for (int b = 0; b < 3; b++) {
						if (!setAndCheck(used, board[i + a][j + b])) {
							return false;
						}
					}
				}
			}
		}
		return true;
	}
}
