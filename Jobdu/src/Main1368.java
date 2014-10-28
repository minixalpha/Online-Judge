import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main1368 {
	static class Node {
		int val;
		int left;
		int right;
	}

	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			int n = cin.nextInt();
			int key = cin.nextInt();
			Node[] nodes = new Node[n + 1];
			for (int i = 1; i <= n; i++) {
				nodes[i].val = cin.nextInt();
				nodes[i].left = cin.nextInt();
				nodes[i].right = cin.nextInt();
			}

			List<Integer> curR = new ArrayList<>();
			List<List<Integer>> result = new ArrayList<>();
			solve(nodes, key, 0, curR, result);
		}

		cin.close();
	}

	private static void solve(Node[] nodes, int key, int sum,
			List<Integer> curR, List<List<Integer>> result) {
		if (nodes[0].left == -1 && nodes[0].right == -1) {
			if (sum == key) {
				result.add(curR);
			}
		}
		
	}
}
