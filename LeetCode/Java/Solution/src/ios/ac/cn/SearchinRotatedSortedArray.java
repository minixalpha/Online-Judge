package ios.ac.cn;

public class SearchinRotatedSortedArray {
	private int findSplitPos(int[] A) {
		int left = 0, right = A.length - 1;
		while (left < right) {
			int mid = left + (right - left) / 2;
			if (A[mid] < A[right]) {
				right = mid;
			} else {
				left = mid + 1;
			}
		}
		return left;
	}

	private int binSearch(int[] A, int start, int end, int target) {
		int left = start, right = end;

		while (left <= right) {
			int mid = left + (right - left) / 2;
			if (A[mid] == target) {
				return mid;
			} else if (A[mid] > target) {
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		}

		return -1;
	}

	public int search(int[] A, int target) {
		if (A == null) {
			return -1;
		}
		int splitPos = findSplitPos(A);
		int findLeft = binSearch(A, 0, splitPos - 1, target);
		if (findLeft != -1) {
			return findLeft;
		}
		int findRight = binSearch(A, splitPos, A.length - 1, target);
		return findRight;
	}
}
