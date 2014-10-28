package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class SymmetricTree {
	private List<Integer> leftFirst = new ArrayList<Integer>();
	private List<Integer> rightFirst = new ArrayList<Integer>();

	private void leftFirstTraversal(TreeNode root) {
		if (root == null) {
			leftFirst.add(null);
			return;
		}
		leftFirst.add(root.val);
		leftFirstTraversal(root.left);
		leftFirstTraversal(root.right);

	}

	private void rightFirstTraversal(TreeNode root) {
		if (root == null) {
			rightFirst.add(null);
			return;
		}
		rightFirst.add(root.val);
		rightFirstTraversal(root.right);
		rightFirstTraversal(root.left);
	}

	private boolean isSame(List<Integer> leftFirst, List<Integer> rightFirst) {
		if (leftFirst.size() != rightFirst.size()) {
			return false;
		}

		for (int i = 0; i < leftFirst.size(); i++) {
			if (leftFirst.get(i) != rightFirst.get(i)) {
				return false;
			}
		}
		return true;
	}

	public boolean isSymmetric(TreeNode root) {
		leftFirstTraversal(root);
		rightFirstTraversal(root);
		return isSame(leftFirst, rightFirst);
	}
}
