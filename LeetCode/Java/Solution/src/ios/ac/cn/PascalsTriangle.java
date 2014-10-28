package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class PascalsTriangle {
	public List<List<Integer>> generate(int numRows) {
		List<List<Integer>> result = new ArrayList<>();
		if (numRows <= 0) {
			return result;
		}

		List<Integer> firstList = new ArrayList<>();
		firstList.add(1);
		result.add(firstList);

		for (int i = 1; i < numRows; i++) {
			List<Integer> preList = result.get(i - 1);
			List<Integer> curList = new ArrayList<>();

			curList.add(1);
			for (int j = 0; j < preList.size() - 1; j++) {
				curList.add(preList.get(j) + preList.get(j + 1));
			}
			curList.add(1);

			result.add(curList);
		}

		return result;
	}
}
