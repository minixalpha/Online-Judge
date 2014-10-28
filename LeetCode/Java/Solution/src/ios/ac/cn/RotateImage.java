package ios.ac.cn;

public class RotateImage {
	public void rotate(int[][] matrix) {
		if (matrix == null) {
			return;
		}

		int n = matrix.length;
		int[][] rotateMatrix = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				rotateMatrix[i][j] = matrix[n - 1 - j][i];
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				matrix[i][j] = rotateMatrix[i][j];
			}
		}
	}

	public void rotateInPlace(int[][] matrix) {
		if (matrix == null) {
			return;
		}
		int n = matrix.length;

		for (int i = 0; i < n / 2; i++) {
			/* j < n - i - 1, not j < n - i */
			for (int j = i; j < n - i - 1; j++) {
				int temp = matrix[i][j];
				matrix[i][j] = matrix[n - 1 - j][i];
				matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
				matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
				matrix[j][n - 1 - i] = temp;
			}
		}
	}
	
	public static void main(String[] args) {
		RotateImage ri = new RotateImage();
		int[][] matrix = {{1,2},{3,4}};
		ri.rotateInPlace(matrix);
	}
}
