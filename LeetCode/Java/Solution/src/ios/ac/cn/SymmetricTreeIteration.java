package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class SymmetricTreeIteration {
	private boolean isSymList(List<TreeNode> list) {
		if (list == null) {
			return true;
		}
		for (int i = 0, j = list.size() - 1; i < j; i++, j--) {
			TreeNode left = list.get(i);
			TreeNode right = list.get(j);
			if (left != null && right != null && left.val != right.val) {
				return false;
			}
			if ((left == null || right == null) && (left != right)) {
				return false;
			}
		}
		return true;
	}

	public boolean isSymmetric(TreeNode root) {
		if (root == null) {
			return true;
		}

		List<TreeNode> curList = new ArrayList<>();
		List<TreeNode> nextList = new ArrayList<>();

		curList.add(root);
		while (curList.isEmpty() == false) {
			for (TreeNode e : curList) {
				if (e != null) {
					nextList.add(e.left);
					nextList.add(e.right);
				}
			}
			if (isSymList(nextList) == false) {
				return false;
			}
			curList = nextList;
			nextList = new ArrayList<>();
		}
		return true;
	}
}
