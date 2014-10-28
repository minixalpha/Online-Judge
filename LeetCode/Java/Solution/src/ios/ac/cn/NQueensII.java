package ios.ac.cn;

public class NQueensII {
	private int result;
	private int[] usedCol;
	private int N;

	private boolean isConflict(int[] usedCol, int row, int col) {
		for (int i = 0; i < row; i++) {
			if (usedCol[i] == col
					|| Math.abs(row - i) == Math.abs(col - usedCol[i])) {
				return true;
			}
		}
		return false;
	}

	private void solve(int curRow) {
		if (curRow == N) {
			result += 1;
			return;
		}

		for (int col = 0; col < N; col++) {
			if (this.isConflict(usedCol, curRow, col) == false) {
				usedCol[curRow] = col;
				this.solve(curRow + 1);
			}
		}
	}

	public int totalNQueens(int n) {
		usedCol = new int[n];
		N = n;
		this.solve(0);
		return result;
	}

	public static void main(String[] args) {
		NQueensII nq2 = new NQueensII();
		System.out.println(nq2.totalNQueens(8));
	}
}
