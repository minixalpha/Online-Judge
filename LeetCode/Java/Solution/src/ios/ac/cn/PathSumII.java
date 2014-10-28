package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class PathSumII {
	public List<List<Integer>> pathSum(TreeNode root, int sum) {
		List<List<Integer>> result = new ArrayList<>();
		if (root == null) {
			return result;
		}

		if (root.left == null && root.right == null) {
			if (root.val == sum) {
				List<Integer> path = new ArrayList<>();
				path.add(root.val);
				result.add(path);
				return result;
			}
		}

		solveSub(result, root.left, sum, root.val);
		solveSub(result, root.right, sum, root.val);
		return result;
	}

	private void solveSub(List<List<Integer>> result, TreeNode son, int sum,
			int rootVal) {
		if (son != null) {
			List<List<Integer>> rightR = pathSum(son, sum - rootVal);
			for (List<Integer> r : rightR) {
				List<Integer> path = new ArrayList<>();
				path.add(rootVal);
				path.addAll(r);
				result.add(path);
			}
		}
	}
}
