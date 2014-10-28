package ios.ac.cn;

public class MinimumDepthofBinaryTree {
	public int minDepth(TreeNode root) {
		if (root == null) {
			return 0;
		}
		
		// 这里很关键，如果不检查 root 是不是个叶结点，最后会返回 Integer.MAX_VALUE + 1
		if (root.left == null && root.right == null) {
			return 1;
		}
		
		int leftMinDepth = Integer.MAX_VALUE;
		if (root.left != null) {
			leftMinDepth = minDepth(root.left);
		}
		int rightMinDepth = Integer.MAX_VALUE;
		if (root.right != null) {
			rightMinDepth = minDepth(root.right);
		}
		return Math.min(leftMinDepth, rightMinDepth) + 1;
	}
}
