package ios.ac.cn;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class ValidParentheses {
	private static final Map<Character, Character> map = new HashMap<>();
	static {
		map.put(']', '[');
		map.put('}', '{');
		map.put(')', '(');
	}

	public boolean isValid(String s) {
		LinkedList<Character> stack = new LinkedList<>();
		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (map.values().contains(c)) {
				stack.push(c);
			} else if (map.keySet().contains(c)) {
				Character top = stack.poll();
				if (top == null || top != map.get(c)) {
					return false;
				}
			} else {
				return false;
			}

		}
		return stack.isEmpty();
	}

	public static void main(String[] args) {
		new ValidParentheses().isValid("]");
	}
}
