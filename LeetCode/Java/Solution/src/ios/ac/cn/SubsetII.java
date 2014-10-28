package ios.ac.cn;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class SubsetII {
	public List<List<Integer>> subsetsWithDup(int[] num) {
		Arrays.sort(num);
		List<List<Integer>> sets = new ArrayList<>();
		sets.addAll(subsetsWithDup(num, 0));
		return sets;
	}

	private Set<List<Integer>> subsetsWithDup(int[] num, int start) {
		Set<List<Integer>> totalSubSets = new HashSet<>();
		if (start >= num.length) {
			totalSubSets.add(new ArrayList<Integer>());
		} else {

			Set<List<Integer>> subSubSets = subsetsWithDup(num, start + 1);
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
