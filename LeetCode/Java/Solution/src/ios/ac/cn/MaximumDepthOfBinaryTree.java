package ios.ac.cn;

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode(int x) {
		val = x;
	}
}

public class MaximumDepthOfBinaryTree {
	public int maxDepth(TreeNode root) {
		if (root == null) {
			return 0;
		}

		int leftMaxDepth = this.maxDepth(root.left);
		int rightMaxDepth = this.maxDepth(root.right);
		int sonMaxDepth = (leftMaxDepth > rightMaxDepth) ? leftMaxDepth
				: rightMaxDepth;
		return sonMaxDepth + 1;
	}
}
