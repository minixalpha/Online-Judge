package ios.ac.cn;

public class SingleNumber2 {
	public int singleNumber(int[] A) {
		int result = 0;

		for (int i = 0; i < 32; i++) {
			int curBitSum = 0;
			for (int j = 0; j < A.length; j++) {
				if ((A[j] & (1 << i)) != 0) {
					curBitSum += 1;
				}
			}
			if (curBitSum % 3 != 0) {
				result |= (1 << i);
			}
		}
		return result;
	}

	public static void main(String[] args) {
		SingleNumber2 sn2 = new SingleNumber2();
		int[] A = { -19, -46, -19, -46, -9, -9, -19, 17, 17, 17, -13, -13, -9,
				-13, -46, -28 };
		System.out.println(sn2.singleNumber(A));
	}
}
