package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class PascalsTriangleII {
	public List<Integer> getRow(int rowIndex) {
		List<Integer> list = new ArrayList<>();

		list.add(1);
		for (int i = 1; i <= rowIndex; i++) {
			List<Integer> nextList = new ArrayList<>();
			nextList.add(1);
			for (int j = 0; j < list.size() - 1; j++) {
				nextList.add(list.get(j) + list.get(j + 1));
			}
			nextList.add(1);
			list = nextList;
		}
		return list;
	}
}
