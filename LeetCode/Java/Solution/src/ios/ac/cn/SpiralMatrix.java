package ios.ac.cn;

public class SpiralMatrix {
	public int[][] generateMatrix(int n) {
		int[][] matrix = new int[n][n];
		int num = 1;
		for (int s = 0; s < (n + 1) / 2; s++) {
			matrix[s][s] = num;
			int count = n - 2 * s;
			for (int i = 0; i < count - 1; i++) {
				matrix[s][s + i] = num++;
			}
			for (int i = 0; i < count - 1; i++) {
				matrix[s + i][s + count - 1] = num++;
			}
			for (int i = count - 1; i > 0; i--) {
				matrix[s + count - 1][s + i] = num++;
			}
			for (int i = count - 1; i > 0; i--) {
				matrix[s + i][s] = num++;
			}
		}
		return matrix;
	}

}
