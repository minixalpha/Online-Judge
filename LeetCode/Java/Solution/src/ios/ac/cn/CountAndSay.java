package ios.ac.cn;

public class CountAndSay {
	public String countAndSay(int n) {
		String cur = "1";
		for (int i = 1; i < n; i++) {
			cur = next(cur);
		}
		return cur;
	}

	private String next(String str) {
		StringBuilder builder = new StringBuilder();

		char c = str.charAt(0);
		int n = 1;
		for (int i = 1; i < str.length(); i++) {
			if (str.charAt(i) == c) {
				n++;
			} else {
				builder.append(n);
				builder.append(c);
				c = str.charAt(i);
				n = 1;
			}
		}
		/* 别忘记最后一次　*/
		builder.append(n);
		builder.append(c);

		return builder.toString();
	}

	public static void main(String[] args) {
		System.out.println(new CountAndSay().countAndSay(4));
	}
}
