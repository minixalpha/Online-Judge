package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class Combinations {
	public List<List<Integer>> combine(int n, int k) {
		int[] nlist = new int[n];
		for (int i = 1; i <= n; i++) {
			nlist[i - 1] = i;
		}
		return _combine(nlist, 0, k);
	}

	private List<List<Integer>> _combine(int[] nlist, int start, int k) {
		List<List<Integer>> result = new ArrayList<>();
		if (k == 1) {
			for (int i = start; i < nlist.length; i++) {
				List<Integer> curList = new ArrayList<>();
				curList.add(nlist[i]);
				result.add(curList);
			}
			return result;
		}

		for (int i = start; i < nlist.length - k + 1; i++) {
			List<List<Integer>> subResult = _combine(nlist, i + 1, k - 1);
			for (List<Integer> subList : subResult) {
				List<Integer> curList = new ArrayList<>();
				curList.add(nlist[i]);
				curList.addAll(subList);
				result.add(curList);
			}

		}
		return result;
	}

	public static void main(String[] args) {
		List<List<Integer>> result = new Combinations().combine(4, 2);

		for (List<Integer> curList : result) {
			for (Integer e : curList) {
				System.out.print(e + " ");
			}
			System.out.println();
		}
	}
}