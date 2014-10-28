package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class ZigZagConversion {
	public String convert(String s, int nRows) {
		List<List<Character>> result = new ArrayList<>();
		for (int i = 0; i < nRows; i++) {
			result.add(new ArrayList<Character>());
		}

		int i = 0, len = s.length();
		while (i < len) {
			for (int j = 0; j < nRows && i < len; j++, i++) {
				result.get(j).add(s.charAt(i));
			}
			for (int j = nRows - 2; j >= 1 && i < len; j--, i++) {
				result.get(j).add(s.charAt(i));
			}
		}

		StringBuilder builder = new StringBuilder();
		for (int j = 0; j < nRows; j++) {
			for (Character c : result.get(j)) {
				builder.append(c);
			}
		}
		return builder.toString();
	}
	
	public static void main(String[] args) {
		System.out.println(new ZigZagConversion().convert("PAYPALISHIRING", 3));
	}
}
