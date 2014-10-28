package ios.ac.cn;

public class MaximumSubarrray {
	/*
	 * Tips:
	 * if A = {-1}, maxSubArray is -1, not 0,
	 * thus you must choose something
	 */
	public int maxSubArray(int[] A) {
		if (A == null || A.length == 0) {
			return 0;
		}
		
		int curSum = A[0], maxSum = A[0];
		for (int i = 1; i < A.length; i++) {
			curSum = Math.max(curSum + A[i], A[i]);
			maxSum = Math.max(maxSum, curSum);
		}
		
		return maxSum;
	}
}
