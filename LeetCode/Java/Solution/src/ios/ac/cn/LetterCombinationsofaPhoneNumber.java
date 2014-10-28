package ios.ac.cn;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LetterCombinationsofaPhoneNumber {
	private static Map<Character, String> map = new HashMap<>();
	static {
		map.put('2', "abc");
		map.put('3', "def");
		map.put('4', "ghi");
		map.put('5', "jkl");
		map.put('6', "mno");
		map.put('7', "pqrs");
		map.put('8', "tuv");
		map.put('9', "wxyz");
	}

	public List<String> letterCombinations(String digits) {
		List<String> result = new ArrayList<>();
		if (digits != null && digits.length() > 0) {
			List<String> subResult = new ArrayList<>();
			if (digits.length() <= 1) {
				subResult.add("");
			} else {
				subResult = letterCombinations(digits.substring(1));
			}

			String prefix = map.get(digits.charAt(0));

			for (int i = 0; i < prefix.length(); i++) {
				for (String e : subResult) {
					StringBuilder builder = new StringBuilder();
					builder.append(prefix.charAt(i));
					builder.append(e);
					result.add(builder.toString());
				}
			}
		} else {
			result.add("");
		}
		return result;
	}

	public static void main(String[] args) {
		for (String e : new LetterCombinationsofaPhoneNumber()
				.letterCombinations("23")) {
			System.out.println(e);
		}
	}
}
