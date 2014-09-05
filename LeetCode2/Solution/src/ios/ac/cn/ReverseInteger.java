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
		return (int)revPosX;
	}
}
