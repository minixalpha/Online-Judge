package ios.ac.cn;

public class MaximumProductSubArray {
	
	/*
	 * dpMax[i] = max(A[i], A[i] * dpMax[i-1], A[i] * dpMin[i-1])
	 * dpMin[i] = min(A[i], A[i] * dpMax[i-1], A[i] * dpMin[i-1])
	 */
	public int maxProductN(int[] A) {
		int[] dpMax = new int[A.length];
		int[] dpMin = new int[A.length];
		int max = A[0];
		dpMax[0] = dpMin[0] = A[0];
		for (int i = 1; i < A.length; i++) {
			dpMax[i] = tripleMax(A[i], A[i] * dpMax[i - 1], A[i] * dpMin[i - 1]);
			dpMin[i] = tripleMin(A[i], A[i] * dpMax[i - 1], A[i] * dpMin[i - 1]);
			max = Math.max(max, dpMax[i]);
		}
		return max;
	}

	public int maxProduct(int[] A) {
		int curMin, curMax, max;
		curMin = curMax = max = A[0];

		for (int i = 1; i < A.length; i++) {
			int tmax = curMax, tmin = curMin;
			curMax = tripleMax(A[i], A[i] * tmax, A[i] * tmin);
			curMin = tripleMin(A[i], A[i] * tmax, A[i] * tmin);
			max = Math.max(max, curMax);
		}

		return max;
	}

	private int tripleMax(int a, int b, int c) {
		return Math.max(c, Math.max(a, b));
	}

	private int tripleMin(int a, int b, int c) {
		return Math.min(c, Math.min(a, b));
	}

	public static void main(String[] args) {
		int[] A = { 2, 3, -2, 4 };
		System.out.println(new MaximumProductSubArray().maxProduct(A));

		int[] B = { -2, 3, -4 };
		System.out.println(new MaximumProductSubArray().maxProduct(B));
	}
}
