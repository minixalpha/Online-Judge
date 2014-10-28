package ios.ac.cn;
public class UniqueBinarySearchTree {
	public int numTrees(int n) {
		int[] f = new int[n + 1];
		f[0] = 1;
		for (int m = 1; m <= n; m++) {
			int fm = 0;
			for (int i = 0; i < m; i++) {
				fm += (f[i] * f[m - 1 - i]);
			}
			f[m] = fm;
		}
		return f[n];
	}
}
