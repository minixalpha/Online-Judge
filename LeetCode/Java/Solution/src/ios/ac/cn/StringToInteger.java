package ios.ac.cn;

public class StringToInteger {
	public int atoi(String str) {
		int start = 0;
		long sum = 0;
		while (start < str.length() && str.charAt(start) == ' ') {
			start++;
		}
		int sign = 1;
		if (start < str.length() && str.charAt(start) == '+') {
			sign = 1;
			start++;
		} else if (start < str.length() && str.charAt(start) == '-') {
			sign = -1;
			start++;
		}
		for (int i = start; i < str.length()
				&& Character.isDigit(str.charAt(i)); i++) {
			sum = 10 * sum + str.charAt(i) - '0';
		}

		sum = sign * sum;
		if (sum > Integer.MAX_VALUE) {
			return Integer.MAX_VALUE;
		} else if (sum < Integer.MIN_VALUE){
			return Integer.MIN_VALUE;
		} else {
			return (int) sum;
		}
	}

	public static void main(String[] args) {
		System.out.println(new StringToInteger().atoi("123"));
		System.out.println(new StringToInteger().atoi("-123"));
	}
}
