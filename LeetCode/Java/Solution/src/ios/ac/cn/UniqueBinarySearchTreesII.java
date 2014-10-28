package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class UniqueBinarySearchTreesII {
	public List<TreeNode> generateTrees(int n) {
		return generateTrees(1, n);
	}

	private List<TreeNode> generateTrees(int lo, int hi) {
		List<TreeNode> trees = new ArrayList<>();
		if (lo > hi) {
			trees.add(null);
		} else {
			for (int i = lo; i <= hi; i++) {
				List<TreeNode> leftTrees = generateTrees(lo, i - 1);
				List<TreeNode> rightTrees = generateTrees(i + 1, hi);
				for (TreeNode leftTree : leftTrees) {
					for (TreeNode rightTree : rightTrees) {
						TreeNode root = new TreeNode(i);
						root.left = leftTree;
						root.right = rightTree;
						trees.add(root);
					}
				}
			}
		}
		return trees;
	}
}
