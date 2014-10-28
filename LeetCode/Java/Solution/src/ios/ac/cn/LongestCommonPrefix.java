package ios.ac.cn;

public class LongestCommonPrefix {
	public String longestCommonPrefix(String[] strs) {
		if (strs == null || strs.length == 0) {
			return "";
		}
		int longestLen = strs[0].length();

		for (int i = 1; i < strs.length; i++) {
			longestLen = commonPrefixLen(strs[i - 1], strs[i], longestLen);
		}
		return strs[0].substring(0, longestLen);
	}

	private int commonPrefixLen(String a, String b, int len) {
		int maxLen = Math.min(a.length(), b.length());
		maxLen = Math.min(maxLen, len);

		for (int i = 0; i < maxLen; i++) {
			if (a.charAt(i) != b.charAt(i)) {
				return i;
			}
		}
		return maxLen;
	}
}
