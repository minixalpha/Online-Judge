package ios.ac.cn;
public class SingleNumber {
	public int singleNumber(int[] A) {
		int result = 0;
		for (int i = 0; i < A.length; i++) {
			result ^= A[i];
		}
		return result;
	}

	public static void main(String[] args) {
		SingleNumber singleNumber = new SingleNumber();
		int[] A = { 1, 2, 3, 1, 3 };
		System.out.println(singleNumber.singleNumber(A));
	}
}
