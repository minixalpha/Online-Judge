package ios.ac.cn;

import java.lang.Thread.State;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class BinaryTreePostorderTraversal {
	public List<Integer> postorderTraversal(TreeNode root) {
		List<Integer> list = new ArrayList<>();
		if (root == null) {
			return list;
		}

		List<Integer> left = postorderTraversal(root.left);
		List<Integer> right = postorderTraversal(root.right);
		list.addAll(left);
		list.addAll(right);
		list.add(root.val);
		return list;
	}

	public List<Integer> postorderTraversalIter(TreeNode root) {
		List<Integer> list = new ArrayList<>();
		if (root == null) {
			return list;
		}

		LinkedList<TreeNode> stack = new LinkedList<>();
		stack.add(root);
		while (stack.isEmpty() == false) {
			TreeNode top = stack.peek();
			if (top.left != null) {
				stack.push(top.left);
			} else if (top.right != null) {
				stack.push(top.right);
			} else {
				TreeNode preTop = stack.pop();
				list.add(preTop.val);

				while (stack.isEmpty() == false) {
					top = stack.peek();
					if (preTop == top.left && top.right != null) {
						stack.push(top.right);
						break;
					} else {
						preTop = stack.pop();
						list.add(preTop.val);
					}
				}
			}
		}
		return list;
	}
}
