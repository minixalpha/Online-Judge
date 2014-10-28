import java.util.Scanner;

public class Main1367 {
	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);

		while (cin.hasNext()) {
			int n = cin.nextInt();
			long[] array = new long[n];
			for (int i = 0; i < n; i++) {
				array[i] = cin.nextLong();
			}

			if (isPostOrder(array, 0, array.length - 1)) {
				System.out.println("Yes");
			} else {
				System.out.println("No");
			}
		}

		cin.close();
	}

	private static boolean isPostOrder(long[] array, int start, int end) {
		if (start >= end) {
			return true;
		}
		int pos = getSplitPos(array, start, end);
		if (pos == -1) {
			return false;
		}
		boolean leftIsPostOrder = isPostOrder(array, start, pos);
		if (leftIsPostOrder == false) {
			return false;
		}
		return isPostOrder(array, pos + 1, end - 1);
	}

	private static int getSplitPos(long[] array, int start, int end) {
		long root = array[end];
		int i = 0;
		while (i < end && array[i] < root) {
			i++;
		}
		int pos = i - 1;
		while (i < end && array[i] > root) {
			i++;
		}
		if (i == end) {
			return pos;
		} else {
			return -1;
		}
	}
}