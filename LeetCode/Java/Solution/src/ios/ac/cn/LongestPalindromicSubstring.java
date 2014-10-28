package ios.ac.cn;

public class LongestPalindromicSubstring {
	// 需要考虑以单个字符为中心及以两个字符为中心两种情况
	public String longestPalindrome(String s) {
		String longestOdd = getLongestOdd(s);
		String longestEven = getLongestEven(s);

		return longestEven.length() > longestOdd.length() ? longestEven
				: longestOdd;
	}

	private String getLongestEven(String s) {
		int max = 0, start = 0, end = 0;
		for (int center = 0; center < s.length(); center++) {
			int i = center, j = center + 1;
			int halfLen = 0;
			while (i >= 0 && j < s.length() && i < j) {
				if (s.charAt(i) != s.charAt(j)) {
					break;
				} else {
					halfLen += 1;
				}
				--i;
				++j;
			}
			if (halfLen * 2 > max) {
				max = halfLen * 2;
				start = center - halfLen + 1;
				end = center + halfLen;
			}
		}
		return s.substring(start, end + 1);
	}

	private String getLongestOdd(String s) {
		int max = 1, start = 0, end = 0;
		for (int center = 0; center < s.length(); center++) {
			int i = center - 1, j = center + 1;
			int halfLen = 0;
			while (i >= 0 && j < s.length() && i < j) {
				if (s.charAt(i) != s.charAt(j)) {
					break;
				} else {
					halfLen += 1;
				}
				--i;
				++j;
			}
			if (halfLen * 2 + 1 > max) {
				max = halfLen * 2 + 1;
				start = center - halfLen;
				end = center + halfLen;
			}
		}
		return s.substring(start, end + 1);
	}

	public static void main(String[] args) {
		System.out.println(new LongestPalindromicSubstring()
				.longestPalindrome("a"));
		System.out.println(new LongestPalindromicSubstring()
				.longestPalindrome("aab"));
		System.out.println(new LongestPalindromicSubstring()
		.longestPalindrome("abcba"));
	}
}
