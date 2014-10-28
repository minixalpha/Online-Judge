package ios.ac.cn;

public class ReverseInteger {
	public int reverse(int x) {
		long posX = (x >= 0) ? x : -x;
		String strX = Long.toString(posX);
		String revStrX = new StringBuilder(strX).reverse().toString();
		long revPosX = Long.valueOf(revStrX);
		if (x < 0) {
			revPosX = -revPosX;
		}
		return (int) revPosX;
	}

	public int reverse2(int x) {
		long posX = (x >= 0) ? x : -x;
		long revX = 0;

		while (posX != 0) {
			revX = 10 * revX + posX % 10;
			posX /= 10;
		}
		return (int) ((x >= 0) ? revX : -revX);
	}
	
	public static void main(String[] args) {
		System.out.println(new ReverseInteger().reverse2(123));
		System.out.println(new ReverseInteger().reverse2(-123));
	}
}
