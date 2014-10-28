package ios.ac.cn;

public class PlusOne {
	public int[] plusOne(int[] digits) {
		if (digits == null || digits.length == 0) {
			return new int[0];
		}

		int n = digits.length;
		int carry = 1;
		int[] result = new int[n];

		for (int i = n - 1, j = n - 1; i >= 0; i--, j--) {
			int curSum = digits[i] + carry;
			carry = curSum / 10;
			result[j] = curSum % 10;
		}

		if (carry > 0) {
			int[] finalResult = new int[n + 1];
			finalResult[0] = carry;
			System.arraycopy(result, 0, finalResult, 1, n);
			return finalResult;
		} else {
			return result;
		}
	}
}
