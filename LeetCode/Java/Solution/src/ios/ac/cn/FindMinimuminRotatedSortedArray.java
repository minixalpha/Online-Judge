package ios.ac.cn;

public class FindMinimuminRotatedSortedArray {
	public int findMin(int[] num) {
		int lo = 0, hi = num.length - 1;
		while (lo <= hi) {
			int mid = lo + (hi - lo) / 2;
			if (num[mid] > num[hi]) {
				lo = mid + 1;
			} else if (num[mid] < num[hi]) {
				hi = mid;
			} else {
				break;
			}
		}
		return num[lo];
	}
}
