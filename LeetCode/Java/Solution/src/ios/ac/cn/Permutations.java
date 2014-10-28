package ios.ac.cn;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Permutations {
	private void swap(int[] num, int i, int j) {
		int tmp = num[i];
		num[i] = num[j];
		num[j] = tmp;
	}

	private List<List<Integer>> permuteHelper(int[] num, int start) {
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		if (start == num.length) {
			list.add(new ArrayList<Integer>());
			return list;
		}

		for (int i = start; i < num.length; i++) {
			swap(num, start, i);
			List<List<Integer>> subList = permuteHelper(num, start + 1);
			for (List<Integer> e : subList) {
				LinkedList<Integer> curList = new LinkedList<Integer>();
				curList.add(num[start]);
				curList.addAll(e);
				list.add(curList);
			}
			swap(num, i, start);
		}
		return list;
	}

	public List<List<Integer>> permute(int[] num) {
		if (num == null) {
			return new ArrayList<List<Integer>>();
		} else {
			return permuteHelper(num, 0);
		}
	}
}
