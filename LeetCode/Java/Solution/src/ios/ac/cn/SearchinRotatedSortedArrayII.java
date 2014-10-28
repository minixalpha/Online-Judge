package ios.ac.cn;

public class SearchinRotatedSortedArrayII {
	public boolean search(int[] A, int target) {
		if (A == null) {
			return false;
		}
		int left = 0, right = A.length - 1;

		while (left <= right) {
			int mid = left + (right - left) / 2;
			if (A[mid] == target) {
				return true;
			} else {
				if (A[mid] < A[right]) {
					if (target > A[mid] && target <= A[right]) {
						left = mid + 1;
					} else {
						right = mid - 1;
					}
				} else if (A[mid] > A[right]) {
					if (target >= A[left] && target < A[mid]) {
						right = mid - 1;
					} else {
						left = mid + 1;
					}
				} else {
					right -= 1;
				}
			}
		}

		return false;
	}
}
