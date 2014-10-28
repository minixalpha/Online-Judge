import java.util.Scanner;

public class Main1515 {
	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);

		while (cin.hasNext()) {
			int n = cin.nextInt();
			printOneToN(n);
		}
	}

	private static void printOneToN(int n) {
		int limit = (int) Math.pow(10, n) - 1;
		for (int i = 1; i <= limit; i++) {
			System.out.println(i);
		}
	}
}
