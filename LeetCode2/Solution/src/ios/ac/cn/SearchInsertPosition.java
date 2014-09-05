package ios.ac.cn;

public class SearchInsertPosition {
    public int searchInsert(int[] A, int target) {
        if (A == null) {
        	return 0;
        }
        
        int left = 0, right = A.length - 1, mid = 0;
        while (left <= right) {
        	mid = left + (right - left) / 2;
        	if (A[mid] == target) {
        		return mid;
        	} else if (A[mid] > target) {
        		right = mid - 1;
        	} else {
        		left = mid + 1;
        	}
        }
        
        if (A[mid] > target) {
        	return mid;
        } else {
        	return mid + 1;
        }
    }
}
