import java.util.Scanner;

public class Main1516 {
	private static void solve(int[] array) {
		int n = array.length;
		int[] oldA = new int[n];
		int[] evenA = new int[n];
		int oldN = 0, evenN = 0;
		for (int i = 0; i < n; i++) {
			if (array[i] % 2 == 0) {
				evenA[evenN++] = array[i];
			} else {
				oldA[oldN++] = array[i];
			}
		}

		int j = 0;
		for (int i = 0; i < oldN; i++) {
			array[j++] = oldA[i];
		}
		for (int i = 0; i < evenN; i++) {
			array[j++] = evenA[i];
		}
	}

	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);

		while (cin.hasNext()) {
			int n = cin.nextInt();
			int[] array = new int[n];
			for (int i = 0; i < n; i++) {
				array[i] = cin.nextInt();
			}
			solve(array);

			for (int i = 0; i < n; i++) {
				System.out.print(array[i]);
				if (i != n - 1) {
					System.out.print(" ");
				}

			}
			System.out.println();
		}
	}
}
