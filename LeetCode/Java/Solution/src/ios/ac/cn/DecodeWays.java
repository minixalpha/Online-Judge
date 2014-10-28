package ios.ac.cn;

public class DecodeWays {
	/* 注意字符为 0 的特殊情况 */
	public int numDecodings(String s) {
		if (s.length() == 0) {
			return 0;
		}

		int prePre = 0, pre = 0;
		if (s.charAt(0) != '0') {
			prePre = pre = 1;
		}
		for (int i = 1; i < s.length(); i++) {
			int nextPre = 0;
			if (s.charAt(i) != '0') {
				nextPre += pre;
			}

			int n = Integer.valueOf(s.substring(i - 1, i + 1));
			if (n <= 26 && s.charAt(i - 1) != '0') {
				nextPre += prePre;
			}
			prePre = pre;
			pre = nextPre;
		}

		return pre;
	}
}
