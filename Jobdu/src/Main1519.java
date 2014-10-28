import java.util.*;

class Node {
	public int val;
	public Node next;
	
	public Node(int val, Node next) {
		this.val = val;
		this.next = next;
	}
}

public class Main1519 {
	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);
		int m, n;
		while (cin.hasNext()) {
			n = cin.nextInt();
			m = cin.nextInt();

			if (m == 0 && n == 0) {
				System.out.println("NULL");
				continue;
			}

			ArrayList<Integer> listN = new ArrayList<Integer>();
			for (int i = 0; i < n; i++) {
				listN.add(cin.nextInt());
			}

			ArrayList<Integer> listM = new ArrayList<Integer>();
			for (int j = 0; j < m; j++) {
				listM.add(cin.nextInt());
			}

			ArrayList<Integer> listCombine = new ArrayList<Integer>();
			int ci = 0, cj = 0;
			while (ci < n && cj < m) {
				if (listN.get(ci) < listM.get(cj)) {
					listCombine.add(listN.get(ci));
					ci++;
				} else {
					listCombine.add(listM.get(cj));
					cj++;
				}
			}
			while (ci < n) {
				listCombine.add(listN.get(ci));
				ci++;
			}
			while (cj < m) {
				listCombine.add(listM.get(cj));
				cj++;
			}
			
			StringBuilder buidler = new StringBuilder();
			buidler.append(listCombine.get(0));
			for (int i = 1; i < listCombine.size(); i++) {
				buidler.append(" " + listCombine.get(i));
			}
			System.out.println(buidler.toString());
		}

		cin.close();
	}
}