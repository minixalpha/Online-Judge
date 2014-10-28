package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class Triangle {
	public int minimumTotal(List<List<Integer>> triangle) {
		int len = triangle.size();
		int[] minArray = new int[len + 1];

		for (int j = len - 1; j >= 0; j--) {
			List<Integer> curRow = triangle.get(j);
			int i = 0;
			for (Integer e : curRow) {
				minArray[i] = e + Math.min(minArray[i], minArray[i + 1]);
				i++;
			}
		}
		return minArray[0];
	}

	public static void main(String[] args) {
		List<List<Integer>> triangle = new ArrayList<>();
		List<Integer> list = new ArrayList<>();
		list.add(-1);
		triangle.add(list);

		list = new ArrayList<>();
		list.add(-2);
		list.add(-3);
		triangle.add(list);
		System.out.println(new Triangle().minimumTotal(triangle));
	}
}
