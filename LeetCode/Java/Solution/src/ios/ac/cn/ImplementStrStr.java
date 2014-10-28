package ios.ac.cn;

public class ImplementStrStr {
	// 注意对空串的处理
	// 注意起始点的范围是 [0, la-lb]，不是　[0,la-lb)
	public String strStr(String haystack, String needle) {
		for (int i = 0; i <= haystack.length() - needle.length(); i++) {
			int j;
			for (j = 0; j < needle.length(); j++) {
				if (haystack.charAt(i + j) != needle.charAt(j)) {
					break;
				}
			}
			if (j == needle.length()) {
				return haystack.substring(i);
			}
		}

		return null;
	}
}
