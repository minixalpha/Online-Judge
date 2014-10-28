package ios.ac.cn;

public class AddBinary {
	public String addBinary(String a, String b) {
		int len = Math.max(a.length(), b.length()) + 1;
		char[] revResult = new char[len];

		int k = 0, c = 0;

		for (int i = a.length() - 1, j = b.length() - 1; i >= 0 || j >= 0; i--, j--) {
			int r = c;
			if (i >= 0) {
				r += a.charAt(i) - '0';
			}
			if (j >= 0) {
				r += b.charAt(j) - '0';
			}
			revResult[k++] = (char) (r % 2 + '0');
			c = r / 2;
		}
		if (c > 0) {
			revResult[k++] = '1';
		}

		StringBuilder builder = new StringBuilder();
		while (--k >= 0) {
			builder.append(revResult[k]);
		}
		return builder.toString();
	}

	public static void main(String[] args) {
		System.out.println(new AddBinary().addBinary("1", "11"));
	}
}
