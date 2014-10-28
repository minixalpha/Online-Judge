package ios.ac.cn;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class SubSets {
	public List<List<Integer>> subsets(int[] S) {
		Arrays.sort(S);
		List<List<Integer>> sets = new ArrayList<>();
		sets.addAll(subsets(S, 0));
		return sets;
	}

	private Set<List<Integer>> subsets(int[] num, int start) {
		Set<List<Integer>> totalSubSets = new HashSet<>();
		if (start >= num.length) {
			totalSubSets.add(new ArrayList<Integer>());
		} else {

			Set<List<Integer>> subSubSets = subsets(num, start + 1);
			totalSubSets.addAll(subSubSets);
			for (List<Integer> sets : subSubSets) {
				List<Integer> set = new ArrayList<>();
				set.add(num[start]);
				set.addAll(sets);
				totalSubSets.add(set);
			}
		}
		return totalSubSets;
	}
}
