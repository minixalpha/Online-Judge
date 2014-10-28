import java.util.*;

public class Main10 {
	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);
		int n, x;
	
		n = cin.nextInt();
		for (int i = 0; i < n; i++) {
			x = cin.nextInt();
			int oneN = 0;
			for (int j = 0; j < 32; j ++) {
				if ((x & (1 << j)) != 0) {
					oneN ++;
				}
			}
			System.out.println(oneN);
		}

		cin.close();
	}
}