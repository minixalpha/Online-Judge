package ios.ac.cn;

public class PalindromeNumber {
	public boolean isPalindrome(int x) {
		if (x < 0) { return false; }
		int revx = 0, tmpx = x;
		while (tmpx != 0) {
			revx = 10 * revx + tmpx % 10;
			tmpx /= 10;
		}
		return revx == x;
	}
}
