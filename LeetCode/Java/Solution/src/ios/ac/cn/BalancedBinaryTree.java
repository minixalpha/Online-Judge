package ios.ac.cn;

public class BalancedBinaryTree {
	/**
	 * If root is a balanced tree, return it's height, 
	 * or return -1
	 * 
	 * @param root
	 * @return
	 */
	private int getHeight(TreeNode root) {
		if (root == null) {
			return 0;
		}

		int leftHeight = getHeight(root.left);
		if (leftHeight == -1) {
			return -1;
		}

		int rightHeight = getHeight(root.right);
		if (rightHeight == -1) {
			return -1;
		}

		if (Math.abs(leftHeight - rightHeight) <= 1) {
			return Math.max(leftHeight, rightHeight) + 1;
		} else {
			return -1;
		}
	}

	public boolean isBalanced(TreeNode root) {
		int height = getHeight(root);
		if (height >= 0) {
			return true;
		} else {
			return false;
		}
	}
}
