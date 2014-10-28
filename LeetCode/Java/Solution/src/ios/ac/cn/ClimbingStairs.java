package ios.ac.cn;

public class ClimbingStairs {

	/*
	 * F[0] = 1, F[1] = 1, F[n] = F[n-1] + F[n-2]
	 */
	public int climbStairs(int n) {
		int pre = 1, next = 1;

		for (int i = 1; i < n; i++) {
			int tmp = pre + next;
			pre = next;
			next = tmp;
		}

		return next;
	}
}
