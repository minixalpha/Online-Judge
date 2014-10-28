import java.util.Scanner;

public class Main1283 {
	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			String input = cin.next();
			char[] chars = input.toCharArray();
			int[] times = new int[26];
			for (int i = 0; i < chars.length; i++) {
				times[chars[i] - 'A'] += 1;
			}

			int i;
			for (i = 0; i < chars.length; i++) {
				if (times[chars[i] - 'A'] == 1) {
					System.out.println(i);
					break;
				}
			}
			if (i == chars.length) {
				System.out.println(-1);
			}
		}

		cin.close();
	}
}
