package ios.ac.cn;

public class SortColors {
	public void sortColors(int[] A) {
		int[] colorN = new int[3];
		for (int i = 0; i < A.length; i++) {
			colorN[A[i]]++;
		}
		int k = 0;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < colorN[i]; j++) {
				A[k++] = i;
			}
		}
	}
}
