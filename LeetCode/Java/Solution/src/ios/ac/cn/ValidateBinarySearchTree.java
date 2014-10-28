package ios.ac.cn;

public class ValidateBinarySearchTree {
	class Pair {
		Integer max = Integer.MIN_VALUE;
		Integer min = Integer.MAX_VALUE;
	}

	public boolean isValidBST(TreeNode root) {
		Pair pair = getLimit(root);
		return pair != null;
	}

	/**
	 * 求出当前树的最大值及最小值，如果不是二叉搜索树，则返回空
	 * 
	 * @param root
	 *            当前树根
	 * @return 如果是二叉搜索树，返回最大值，最小值，否则，返回空
	 */
	private Pair getLimit(TreeNode root) {
		if (root == null) {
			return new Pair();
		}

		Pair pairLeft = new Pair(), pairRight = new Pair();
		if (root.left != null) {
			pairLeft = getLimit(root.left);
			if (pairLeft == null) {
				return null;
			}
		}
		if (root.right != null) {
			pairRight = getLimit(root.right);
			if (pairRight == null) {
				return null;
			}
		}

		if (!(pairLeft.max < root.val && pairRight.min > root.val)) {
			return null;
		}

		Pair pair = new Pair();
		pair.min = Math.min(Math.min(pairLeft.min, pairRight.min), root.val);
		pair.max = Math.max(Math.max(pairLeft.max, pairRight.max), root.val);
		return pair;
	}
}
