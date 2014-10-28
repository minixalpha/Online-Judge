package ios.ac.cn;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class GenerateParentheses {
	public List<String> generateParenthesis(int n) {
		List<String> list = new ArrayList<>();

		if (n == 0) {
			list.add("");
			return list;
		}

		for (int i = 0; i < n; i++) {
			List<String> innerList = generateParenthesis(i);
			List<String> rightList = generateParenthesis(n - 1 - i);

			for (String inner : innerList) {
				for (String right : rightList) {
					list.add("(" + inner + ")" + right);
				}
			}
		}
		return list;
	}

	public List<String> generateParenthesisIteration(int n) {
		List<String> list = new ArrayList<>();
		LinkedList<String> strStack = new LinkedList<>();
		LinkedList<Integer> closedNumStack = new LinkedList<>();

		strStack.push("(");
		closedNumStack.push(0);

		while (strStack.isEmpty() == false) {
			String curStr = strStack.pop();
			int curClosedNum = closedNumStack.pop();

			if (curStr.length() == 2 * n) {
				list.add(curStr);
				continue;
			}

			/* if non-closeNum < n, then we could add '(' */
			if (curStr.length() - curClosedNum < n) {
				strStack.push(curStr + "(");
				closedNumStack.push(curClosedNum);
			}

			/*
			 * If closeNum < non-closeNum , thus closeNum * 2 < totalNum,
			 * then we could add ')'
			 */
			if (curClosedNum * 2 < curStr.length()) {
				strStack.push(curStr + ")");
				closedNumStack.push(curClosedNum + 1);
			}
		}

		return list;
	}
}
