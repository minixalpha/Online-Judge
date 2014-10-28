package ios.ac.cn;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class BinaryTreeLevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
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
			result.add(curList);
			curLevel = nextLevel;
		}
		return result;
    }
}
