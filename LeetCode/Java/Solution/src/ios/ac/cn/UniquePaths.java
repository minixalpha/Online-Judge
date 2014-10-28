package ios.ac.cn;

public class UniquePaths {
	private int getN(int[][] matrix, int i, int j) {
		int m = matrix.length, n = matrix[0].length;
		if (i >= 0 && i < m && j >= 0 && j < n) {
			return matrix[i][j];
		} else {
			return 0;
		}
	}

	public int uniquePaths(int m, int n) {
		int[][] matrix = new int[m][n];
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (i == 0 && j == 0) {
					/* remember bootstrap */
					matrix[i][j] = 1;
				} else {
					matrix[i][j] = getN(matrix, i - 1, j)
							+ getN(matrix, i, j - 1);
				}
			}
		}
		return matrix[m - 1][n - 1];
	}
}
