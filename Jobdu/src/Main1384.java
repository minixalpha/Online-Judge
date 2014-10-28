import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main1384 {
	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);
		int[][] array = new int[1000][1000];
		
		start:
		while (cin.hasNext()) {
			int n = cin.nextInt();
			int m = cin.nextInt();
			int k = cin.nextInt();

			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					array[i][j] = cin.nextInt();
				}
			}

			int i = 0, j = m - 1;
			while (i < n && j >= 0) {
				if (array[i][j] == k) {
					System.out.println("Yes");
					continue start;
				} else if (array[i][j] > k) {
					j--;
				} else {
					i++;
				}
			}
			System.out.println("No");
		}

		cin.close();
	}
}
