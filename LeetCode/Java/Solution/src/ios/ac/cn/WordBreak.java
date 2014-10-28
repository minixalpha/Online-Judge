package ios.ac.cn;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class WordBreak {
	private Map<String, Boolean> cache = new HashMap<>();

	public boolean wordBreak(String s, Set<String> dict) {
		if (cache.containsKey(s)) {
			return cache.get(s);
		}

		if (dict.contains(s)) {
			cache.put(s, true);
			return true;
		}
		for (int i = 1; i < s.length(); i++) {
			if (dict.contains(s.substring(0, i))
					&& wordBreak(s.substring(i), dict)) {
				cache.put(s, true);
				return true;
			}
		}

		cache.put(s, false);
		return false;
	}

	public boolean wordBreak2(String s, Set<String> dict) {
		/* canMake[i] 从0开始，长度为 i 的字符串是否可由 dict 构成 */
		boolean[] canMake = new boolean[s.length() + 1];
		canMake[0] = true;

		for (int i = 1; i <= s.length(); i++) {
			for (int j = 0; j < i; j++) {
				if (canMake[j] && dict.contains(s.subSequence(j, i))) {
					canMake[i] = true;
					break;
				}
			}
		}
		return canMake[s.length()];
	}
}
