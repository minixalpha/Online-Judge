package ios.ac.cn;

public class Sqrt {
	public int sqrt(int x) {
        if (x < 0) {
			throw new IllegalArgumentException();
		}
		long t = x;
		while (t * t > x) {
			t = (t * t + x) / (2 * t);
		}
		return (int)t;
	}
	
	public static void main(String[] args) {
		Sqrt t = new Sqrt();
		System.out.println(t.sqrt(4));
	}
}
