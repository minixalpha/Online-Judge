import java.util.Scanner;

public class Main1348 {
	private static int reverseNum(int[] array) {
		int n = array.length;
		
		int revN = 0;
		for(int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (array[i] > array[j]) {
					revN++;
				}
			}
		}
		return revN;
	}

	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);

		while (cin.hasNext()) {
			int n = cin.nextInt();
			int[] array = new int[n];
			for (int i = 0; i < n; i++) {
				array[i] = cin.nextInt();
			}
			System.out.println(reverseNum(array));
		}
	}

}
