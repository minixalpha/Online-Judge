package ios.ac.cn;

import java.util.LinkedList;

public class EvaluateReversePolishNotation {
	public int evalRPN(String[] tokens) {
		if (tokens == null) {
			return 0;
		}

		LinkedList<String> stack = new LinkedList<String>();
		for (String tk : tokens) {
			if (isOperators(tk)) {
				int op2 = Integer.valueOf(stack.pop());
				int op1 = Integer.valueOf(stack.pop());
				if (tk.equals("+")) {
					stack.push(Integer.toString(op1 + op2));
				} else if (tk.equals("-")) {
					stack.push(Integer.toString(op1 - op2));
				} else if (tk.equals("*")) {
					stack.push(Integer.toString(op1 * op2));
				} else {
					stack.push(Integer.toString(op1 / op2));
				}
			} else {
				stack.push(tk);
			}
		}
		return Integer.valueOf(stack.pop());
	}

	private boolean isOperators(String tk) {
		String[] operators = { "+", "-", "*", "/" };
		for (String op : operators) {
			if (tk.equals(op)) {
				return true;
			}
		}
		return false;
	}

	public static void main(String[] args) {

	}
}
