package ios.ac.cn;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class L3Sum {
	public List<List<Integer>> threeSum(int[] num) {
		List<List<Integer>> result = new ArrayList<>();
		if (num == null) {
			return result;
		}

		List<Integer> data = new ArrayList<>();
		for (int i = 0; i < num.length; i++) {
			data.add(num[i]);
		}
		Collections.sort(data);

		for (int i = 0; i < data.size(); i++) {
			if (i > 0 && num[i] == num[i - 1])
				continue;
			int j = i + 1, k = data.size() - 1;
			while (j < k) {
				int sum = data.get(i) + data.get(j) + data.get(k);
				if (sum == 0) {
					result.add(Arrays.asList(data.get(i), data.get(j),
							data.get(k)));
					j++;
				} else if (sum < 0) {
					j++;
				} else {
					k--;
				}
			}
		}
		return result;
	}
}
