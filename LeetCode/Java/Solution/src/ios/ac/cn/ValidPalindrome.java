package ios.ac.cn;

public class ValidPalindrome {
	/*
	 *  1) 注意字母和数字都需要检查是否相等
	 *  2) 注意字母大小写忽略
	 */
	public boolean isPalindrome(String s) {
		char[] chars = s.toCharArray();
		int i = 0, j = chars.length - 1;
		while (i < j) {
			while (i < j && Character.isLetterOrDigit(chars[i]) == false) {
				i++;
			}
			while (i < j && Character.isLetterOrDigit(chars[j]) == false) {
				j--;
			}
			if (i < j
					&& Character.toLowerCase(chars[i]) != Character
							.toLowerCase(chars[j])) {
				return false;
			}
			i++;
			j--;
		}
		return true;
	}
}
