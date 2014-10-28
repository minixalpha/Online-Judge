package ios.ac.cn;

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
	public int[] twoSum(int[] numbers, int target) {
		Map<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < numbers.length; i++) {
			map.put(numbers[i], i);
		}

		int[] result = { 0, 0 };
		for (int i = 0; i < numbers.length; i++) {
			Integer match = map.get(target - numbers[i]);
			if (match != null && match != i) {
				result[0] = i + 1;
				result[1] = match + 1;
				return result;
			}
		}
		return result;
	}
}
