package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class GrayCode {
	public List<Integer> grayCode(int n) {
		List<Integer> list = new ArrayList<>();
		list.add(0);

		if (n == 0) {
			return list;
		}

		for (int i = 1; i < Math.pow(2, n); i++) {
			list.add(i ^ (i >> 1));
		}
		return list;
	}

	public static void main(String[] args) {
		GrayCode gc = new GrayCode();
		gc.grayCode(2);
	}
}
