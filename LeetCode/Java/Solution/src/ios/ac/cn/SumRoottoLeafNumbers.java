package ios.ac.cn;

public class SumRoottoLeafNumbers {
	private int sum = 0;

	public int sumNumbers(TreeNode root) {
		if (root != null) {
			sumNumbers(root, 0);
		}
		return sum;
	}

	public void sumNumbers(TreeNode root, int curSum) {
		if (isLeaf(root)) {
			sum += getNewSum(curSum, root.val);
		} else {
			if (root.left != null) {
				sumNumbers(root.left, getNewSum(curSum, root.val));
			}
			if (root.right != null) {
				sumNumbers(root.right, getNewSum(curSum, root.val));
			}
		}
	}

	private int getNewSum(int curSum, int curVal) {
		return 10 * curSum + curVal;
	}

	private boolean isLeaf(TreeNode root) {
		return root.left == null && root.right == null;
	}

	public static void main(String[] args) {
		TreeNode root = new TreeNode(1);
		root.left = new TreeNode(2);
		root.right = new TreeNode(3);
		System.out.println(new SumRoottoLeafNumbers().sumNumbers(root));
	}
}
