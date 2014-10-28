package ios.ac.cn;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class NQueen {
	private int[] usedCol;
	private int N;
	private List<String[]> result;

	private boolean isConflict(int[] usedCol, int row, int col) {
		for (int i = 0; i < row; i++) {
			if (usedCol[i] == col
					|| Math.abs(row - i) == Math.abs(col - usedCol[i])) {
				return true;
			}
		}
		return false;
	}

	private String getCurRow(int col) {
		char str[] = new char[N];
		for (int i = 0; i < N; i++) {
			str[i] = '.';
		}
		str[col] = 'Q';
		return new String(str);
	}

	private void solve(int curRow, String[] curSolution) {
		if (curRow == N) {
			result.add(Arrays.copyOf(curSolution, N));
			return;
		}

		for (int col = 0; col < N; col++) {
			if (this.isConflict(usedCol, curRow, col) == false) {
				usedCol[curRow] = col;
				curSolution[curRow] = getCurRow(col);
				this.solve(curRow + 1, curSolution);
			}
		}
	}

	public List<String[]> solveNQueens(int n) {
		usedCol = new int[n];
		N = n;
		result = new LinkedList<String[]>();
		String[] curSolution = new String[n];
		this.solve(0, curSolution);
		return result;
	}

	public static void main(String[] args) {
		NQueen nq = new NQueen();
		List<String[]> result = nq.solveNQueens(4);
		for(String[] solution: result) {
			for (String row: solution) {
				System.out.println(row);
			}
			System.out.println();
		}
	}
}
