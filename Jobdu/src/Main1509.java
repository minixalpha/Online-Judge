import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main1509 {
	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);

		while (cin.hasNext()) {
			int n = cin.nextInt();
			cin.nextLine();
			for (int i = 0; i < n; i++) {
				String[] nodes = cin.nextLine().split(" ");
				String[] keys = cin.nextLine().split(" ");
				int commonRoot = findCommon(nodes, keys);
				if (commonRoot == -1) {
					System.out.println("My God");
				} else {
					System.out.println(commonRoot);
				}
			}
		}
	}

	private static int findCommon(String[] nodes, String[] keys) {
		int pos[] = new int[2];
		for (int i = 0; i < keys.length; i++) {
			for (int j = 0; j < nodes.length; j++) {
				if (nodes[j].equals(keys[i])) {
					pos[i] = j;
					break;
				}
			}
		}

		if (pos[0] == 0 || pos[1] == 0) {
			return -1;
		}

		List<Integer> p1 = findPath(pos[0]);
		List<Integer> p2 = findPath(pos[1]);

		int i = p1.size() - 1, j = p2.size() - 1;
		while (p1.get(i) == p2.get(j)) {
			i--;
			j--;
		}

		return p1.get(i);
	}

	private static List<Integer> findPath(int pos) {
		List<Integer> list = new ArrayList<Integer>();
		while (pos != 0) {
			list.add(pos);
			pos = (pos - 1) / 2;
		}
		list.add(0);
		return list;
	}
}
