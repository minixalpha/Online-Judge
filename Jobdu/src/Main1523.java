import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main1523 {
	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);

		while (cin.hasNext()) {
			int n = cin.nextInt();
			int[] value = new int[n];
			for (int i = 0; i < n; i++) {
				value[i] = cin.nextInt();
			}

			int[] left = new int[n];
			int[] right = new int[n];

			for (int i = 0; i < n; i++) {
				String type = cin.next();
				if (type.equals("d")) {
					left[i] = cin.nextInt() - 1;
					right[i] = cin.nextInt() - 1;
				} else if (type.equals("l")) {
					left[i] = cin.nextInt() - 1;
				} else if (type.equals("r")) {
					right[i] = cin.nextInt() - 1;
				}
			}
			printTreeByLevel(value, left, right);
		}
	}

	private static void printTreeByLevel(int[] value, int[] left, int[] right) {
		LinkedList<Integer> curLevel = new LinkedList<Integer>();
		curLevel.add(0);
		List<Integer> result = new ArrayList<Integer>();

		while (curLevel.isEmpty() == false) {
			LinkedList<Integer> nextLevel = new LinkedList<Integer>();
			for (Integer e : curLevel) {
				result.add(value[e]);
				if (left[e] != 0) {
					nextLevel.add(left[e]);
				}
				if (right[e] != 0) {
					nextLevel.add(right[e]);
				}
			}
			curLevel = nextLevel;
		}

		if (result.size() > 0) {
			System.out.print(result.get(0));
		}
		for (int i = 1; i < result.size(); i++) {
			System.out.print(" " + result.get(i));
		}
		System.out.println();
	}
}
