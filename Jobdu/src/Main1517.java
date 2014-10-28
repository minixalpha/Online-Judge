import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main1517 {
	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);

		while (cin.hasNext()) {
			int n = cin.nextInt();
			int k = cin.nextInt();
			if (k <= 0 || k > n) {
				System.out.println("NULL");
				continue;
			}

			List<Integer> list = new LinkedList<Integer>();
			for (int i = 0; i < n; i++) {
				list.add(cin.nextInt());
			}

			Iterator<Integer> first = list.iterator();
			for (int i = 0; i < k; i++) {
				first.next();
			}
			Iterator<Integer> second = list.iterator();
			while (first.hasNext()) {
				first.next();
				second.next();
			}
			System.out.println(second.next());
		}

		cin.close();
	}
}
