package ios.ac.cn;

import java.util.HashMap;
import java.util.Map;

public class WordSearch {
	private Map<Integer, String> cache = new HashMap<>();

	public boolean exist2(char[][] board, String word) {
		int wordLen = word.length(), row = board.length, col = board[0].length;
		boolean dp[][][] = new boolean[wordLen][row][col];

		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				for (int k = 0; k < wordLen; k++) {
					dp[i][j][k] = false;
				}
				if (dp[i][j][wordLen] == true) {
					return true;
				}
			}
		}
		return false;
	}

	public boolean exist(char[][] board, String word) {
		if (word == null || word.length() == 0) {
			return false;
		}

		int row = board.length, col = board[0].length;
		boolean[][] visit = new boolean[row][col];
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (exist(board, i, j, word, visit)) {
					return true;
				}
			}
		}

		return false;
	}

	private boolean exist(char[][] board, int r, int c, String word,
			boolean[][] visit) {
		if (r < 0 || c < 0 || r >= board.length || c >= board[0].length
				|| board[r][c] != word.charAt(0) || visit[r][c]) {
			return false;
		} else {
			if (word.length() == 1) {
				return true;
			} else {
				visit[r][c] = true;
				if (exist(board, r - 1, c, word.substring(1), visit)) {
					return true;
				} else if (exist(board, r + 1, c, word.substring(1), visit)) {
					return true;
				} else if (exist(board, r, c + 1, word.substring(1), visit)) {
					return true;
				} else if (exist(board, r, c - 1, word.substring(1), visit)) {
					return true;
				} else {
					visit[r][c] = false;
					return false;
				}
			}
		}
	}

	public static void main(String[] args) {
		WordSearch ws = new WordSearch();
		char[][] board = { { 'a', 'b', 'c', 'e' }, { 's', 'f', 'c', 's' },
				{ 'a', 'd', 'e', 'e' } };
		System.out.println(ws.exist(board, "ABCCED".toLowerCase()));
	}
}
