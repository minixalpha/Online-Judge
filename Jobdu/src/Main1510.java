import java.util.Scanner;

public class Main1510 {
	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);

		while (cin.hasNext()) {
			String input = cin.nextLine();

			int blankCount = getBlankNum(input);
			char[] finalChars = new char[input.length() + 2 * blankCount];
			int j = finalChars.length - 1;
			for (int i = input.length() - 1; i >= 0; i--) {
				if (input.charAt(i) != ' ') {
					finalChars[j--] = input.charAt(i);
				} else {
					finalChars[j--] = '0';
					finalChars[j--] = '2';
					finalChars[j--] = '%';
				}
			}
			System.out.println(finalChars);
		}
		cin.close();
	}

	private static int getBlankNum(String input) {
		int count = 0;
		for (int i = 0; i < input.length(); i++) {
			if (input.charAt(i) == ' ') {
				count++;
			}
		}
		return count;
	}
}
