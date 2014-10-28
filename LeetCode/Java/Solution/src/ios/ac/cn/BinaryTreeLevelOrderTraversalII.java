package ios.ac.cn;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class BinaryTreeLevelOrderTraversalII {
	public List<List<Integer>> levelOrderBottom(TreeNode root) {
		LinkedList<List<Integer>> result = new LinkedList<List<Integer>>();
		if (root == null) {
			return result;
		}

		List<TreeNode> curLevel = new ArrayList<TreeNode>();
		curLevel.add(root);

		while (curLevel.isEmpty() == false) {
			List<TreeNode> nextLevel = new ArrayList<TreeNode>();
			List<Integer> curList = new ArrayList<>();
			for (TreeNode e : curLevel) {
				if (e.left != null) {
					nextLevel.add(e.left);
				}
				if (e.right != null) {
					nextLevel.add(e.right);
				}
				curList.add(e.val);
			}
			result.addFirst(curList);
			curLevel = nextLevel;
		}
		return result;
	}
}
