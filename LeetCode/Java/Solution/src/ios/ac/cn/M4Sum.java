package ios.ac.cn;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.TreeMap;

public class M4Sum {
	private int[] getSortedNum(int[] num) {
		List<Integer> list = new ArrayList<>();
		for (int i = 0; i < num.length; i++) {
			list.add(num[i]);
		}
		Collections.sort(list);
		int[] knum = new int[list.size()];
		int i = 0;
		for (Integer e : list) {
			knum[i++] = e;
		}
		return knum;
	}

	private TreeMap<Integer, List<Pair>> getSumPair(int[] num) {
		TreeMap<Integer, List<Pair>> map = new TreeMap<>();
		for (int i = 0; i < num.length; i++) {
			for (int j = i + 1; j < num.length; j++) {
				int p = num[i], q = num[j];
				int sum = p + q;
				if (map.containsKey(sum) == false) {
					List<Pair> pairList = new ArrayList<>();
					pairList.add(new Pair(i, j));
					map.put(sum, pairList);
				} else {
					map.get(sum).add(new Pair(i, j));
				}
			}
		}
		return map;
	}

	private int[] getPairSum(TreeMap<Integer, List<Pair>> map) {
		Set<Integer> keys = map.keySet();
		int[] pairSum = new int[keys.size()];
		int i = 0;
		for (Integer e : keys) {
			pairSum[i++] = e;
		}
		return pairSum;
	}

	public List<List<Integer>> fourSum(int[] num, int target) {
		Set<List<Integer>> result = new HashSet<>();
		int[] unum = getSortedNum(num);
		TreeMap<Integer, List<Pair>> map = getSumPair(unum);
		int[] pairSum = getPairSum(map);

		int j = 0, k = pairSum.length - 1;
		while (j <= k) {
			int sum = pairSum[j] + pairSum[k];
			if (sum == target) {
				for (Pair p1 : map.get(pairSum[j])) {
					for (Pair p2 : map.get(pairSum[k])) {
						List<Integer> item = new ArrayList<>();
						if (p2.mFirst > p1.mSecond) {
							item.add(unum[p1.mFirst]);
							item.add(unum[p1.mSecond]);
							item.add(unum[p2.mFirst]);
							item.add(unum[p2.mSecond]);
							result.add(item);
						}
					}
				}

				if (j + 1 < k && pairSum[j] == pairSum[j + 1]) {
					j++;
				} else {
					k--;
				}
			} else if (sum < target) {
				j++;
			} else {
				k--;
			}
		}
		return new ArrayList<>(result);
	}

	class Pair {
		Integer mFirst;
		Integer mSecond;

		public Pair(int first, int second) {
			mFirst = first;
			mSecond = second;
		}
	}

	public static void main(String[] args) {
		// int[] num = { 1, 0, -1, 0, -2, 2 };
		int[] num = { 0, 0, 0, 0 };
		List<List<Integer>> result = new M4Sum().fourSum(num, 0);
		for (List<Integer> list : result) {
			for (Integer e : list) {
				System.out.print(e + " ");
			}
			System.out.println();
		}
	}
}
