package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class PalindromePartitioning {
	public List<List<String>> partition(String s) {
		List<List<String>> result = new ArrayList<>();
		if (s == null || s.length() == 0) {
			return result;
		}
		if (s.length() == 1) {
			addToResult(s, result);
			return result;
		}

		for (int i = 1; i < s.length(); i++) {
			String head = s.substring(0, i);
			if (isPalindrome(head)) {
				List<List<String>> subResult = partition(s.substring(i));
				for (List<String> r : subResult) {
					List<String> e = new ArrayList<>();
					e.add(head);
					e.addAll(r);
					result.add(e);
				}
			}
		}

		if (isPalindrome(s)) {
			addToResult(s, result);
		}
		return result;
	}

	private void addToResult(String s, List<List<String>> result) {
		List<String> e = new ArrayList<>();
		e.add(s);
		result.add(e);
	}

	private boolean isPalindrome(String s) {
		int i = 0, j = s.length() - 1;
		while (i < j) {
			if (s.charAt(i) != s.charAt(j)) {
				return false;
			}
			++i;
			--j;
		}
		return true;
	}
	
	public static void main(String[] args) {
		for(List<String> strList: new PalindromePartitioning().partition("aab")) {
			for(String str: strList) {
				System.out.print(str + " ");
			}
			System.out.println();
		}
	}
}
