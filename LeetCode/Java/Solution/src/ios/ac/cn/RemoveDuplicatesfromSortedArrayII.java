package ios.ac.cn;

public class RemoveDuplicatesfromSortedArrayII {
	public int removeDuplicates(int[] A) {
		if (A == null || A.length == 0) {
			return 0;
		}

		int[] B = new int[A.length];
		int j = 0;
		B[j] = A[0];

		for (int i = 1; i < A.length; i++) {
			if (A[i] != B[j] || (j == 0 || B[j] != B[j - 1])) {
				B[++j] = A[i];
			}
		}

		for (int i = 0; i <= j; i++) {
			A[i] = B[i];
		}
		return j + 1;
	}

	public int removeDuplicatesConstantSpace(int[] A) {
		if (A == null || A.length == 0) {
			return 0;
		}

		int i = 0;
		for (int j = 0; j < A.length; j++) {
			/* Copy condition is the key */
			if ((i >= 2 && A[i - 1] == A[i - 2] && A[j] == A[i - 1]) == false) {
				A[i++] = A[j];
			}
		}
		return i;
	}
}
