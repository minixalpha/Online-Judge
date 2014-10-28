import java.util.*;

public class Main7 {
	public static void main(String args[]) {
		Scanner cin = new Scanner(System.in);
		int n, x;
		String op;
		LinkedList<Integer> stackLeft = new LinkedList<Integer>();
		LinkedList<Integer> stackRight = new LinkedList<Integer>();

		n = cin.nextInt();
		for (int i = 0; i < n; i++) {
			op = cin.next();
			if (op.equals("PUSH")) {
				x = cin.nextInt();
				stackLeft.push(x);
			} else if (op.equals("POP")) {
				if (stackRight.isEmpty() == false) {
					System.out.println(stackRight.pop());
				} else {
					while (stackLeft.isEmpty() == false) {
						stackRight.push(stackLeft.pop());
					}
					if (stackRight.isEmpty() == false) {
						System.out.println(stackRight.pop());
					} else {
						System.out.println(-1);
					}
				}
			}
		}

		cin.close();
	}
}