package ios.ac.cn;

public class RemoveDumplicateFromSortedArray {
	public int removeDuplicates(int[] A) {
		if (A == null || A.length == 0) {
			return 0;
		}

		int end = 0;
		for (int cur = 0; cur < A.length - 1; cur++) {
			if (A[cur] != A[cur + 1]) {
				A[end++] = A[cur];
			}
		}
		A[end++] = A[A.length - 1];
		return end;
	}
}
