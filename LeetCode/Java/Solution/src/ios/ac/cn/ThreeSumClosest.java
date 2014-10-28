package ios.ac.cn;

import java.util.Arrays;

public class ThreeSumClosest {
	/*
	 * 以 i 为起点, j, k 在　[i+1:) 上游走，使得 num[i] + num[j] + num[k] 尽力逼近 target
	 */
	public int threeSumClosest(int[] num, int target) {
		Arrays.sort(num);
		int closestVal = num[0] + num[1] + num[2];
		int closestGap = Math.abs(closestVal - target);

		for (int i = 0; i < num.length - 2; i++) {
			int j = i + 1, k = num.length - 1;
			while (j < k) {
				int curVal = num[i] + num[j] + num[k];
				int curGap = Math.abs(curVal - target);

				if (curGap < closestGap) {
					closestGap = curGap;
					closestVal = curVal;
				}

				// 使得　curVal 不断逼近　target
				if (curVal > target) {
					--k;
				} else {
					++j;
				}
			}

		}
		return closestVal;
	}

	public static void main(String[] args) {
		int[] num = { 1, 2, 4, 8, 16, 32, 64, 128 };
		System.out.print(new ThreeSumClosest().threeSumClosest(num, 82));
	}
}
