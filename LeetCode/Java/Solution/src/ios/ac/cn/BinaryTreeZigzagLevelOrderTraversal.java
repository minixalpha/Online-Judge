package ios.ac.cn;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class BinaryTreeZigzagLevelOrderTraversal {
	public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
		List<List<Integer>> result = new ArrayList<>();
		boolean leftToRight = true;

		List<TreeNode> curLevel = new ArrayList<>();
		if (root != null) {
			curLevel.add(root);
		}
		while (curLevel.isEmpty() == false) {
			List<TreeNode> nextLevel = new ArrayList<>();

			for (TreeNode e : curLevel) {
				if (e.left != null)
					nextLevel.add(e.left);
				if (e.right != null)
					nextLevel.add(e.right);
			}

			LinkedList<Integer> curLevelResult = new LinkedList<>();
			if (leftToRight) {
				leftToRight = false;
				for (TreeNode e : curLevel) {
					curLevelResult.add(e.val);
				}

			} else {
				leftToRight = true;
				for (TreeNode e : curLevel) {
					curLevelResult.addFirst(e.val);
				}
			}
			result.add(curLevelResult);
			curLevel = nextLevel;
		}
		return result;
	}
}
