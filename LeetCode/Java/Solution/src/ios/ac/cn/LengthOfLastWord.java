package ios.ac.cn;

public class LengthOfLastWord {
	public int lengthOfLastWord(String s) {
		if (s == null || s.length() == 0) {
			return 0;
		}
		char[] chars = s.toCharArray();

		int i = s.length() - 1;
		// WA: 从最后一个非空字符开始
		while (i >= 0 && chars[i] == ' ') {
			i--;
		}

		int len = 0;
		while (i >= 0 && chars[i] != ' ') {
			i--;
			len++;
		}
		return len;
	}
}
