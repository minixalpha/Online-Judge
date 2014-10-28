package ios.ac.cn;

public class MininumPathSum {
	private int getN(int[][] minSum, int i, int j) {
		int m = minSum.length, n = minSum[0].length;
		if (i >= 0 && i < m && j >= 0 && j < n) {
			return minSum[i][j];
		} else {
			return Integer.MAX_VALUE;
		}
	}

	public int minPathSum(int[][] grid) {
		if (grid == null || grid.length == 0) {
			return 0;
		}

		int m = grid.length, n = grid[0].length;
		int[][] minSum = new int[m][n];

		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (i == 0 && j == 0) {
					minSum[i][j] = grid[i][j];
				} else {
					minSum[i][j] = grid[i][j]
							+ Math.min(getN(minSum, i - 1, j),
									getN(minSum, i, j - 1));
				}
			}
		}
		return minSum[m - 1][n - 1];
	}
}
