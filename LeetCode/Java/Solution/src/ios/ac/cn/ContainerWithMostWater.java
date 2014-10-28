package ios.ac.cn;

public class ContainerWithMostWater {
	public int maxArea(int[] height) {
		if (height == null) {
			return 0;
		}
		int low = 0, high = height.length - 1;
		int max = 0;
		while (low < high) {
			if (height[low] < height[high]) {
				/*
				 * if height[low] < height[high], then the max area which is
				 * related to height[low] is (height[low] * (high - low))
				 */
				max = Math.max(max, height[low] * (high - low));
				low++;
			} else {
				max = Math.max(max, height[high] * (high - low));
				high--;
			}
		}
		return max;
	}
}
