package ios.ac.cn;

public class RemoveElement {
	public int removeElement(int[] A, int elem) {
		if (A == null) {
			return 0;
		}

		int curLen = 0, curP = 0;
		while (curP < A.length) {
			if (A[curP] != elem) {
				A[curLen++] = A[curP];
			}
			curP++;
		}
		return curLen;
	}
}
