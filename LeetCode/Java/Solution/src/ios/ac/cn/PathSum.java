package ios.ac.cn;

public class PathSum {
	public boolean hasPathSum(TreeNode root, int sum) {
		if (root == null) {
			return false;
		}

		if (root.left == null && root.right == null) {
			return sum == root.val;
		}

		if (hasPathSum(root.left, sum - root.val)) {
			return true;
		}

		if (hasPathSum(root.right, sum - root.val)) {
			return true;
		}
		return false;
	}
}
