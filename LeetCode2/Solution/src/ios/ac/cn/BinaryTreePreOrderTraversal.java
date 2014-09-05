package ios.ac.cn;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class BinaryTreePreOrderTraversal {
	public List<Integer> preorderTraversalRecursive(TreeNode root) {
		List<Integer> list = new ArrayList<>();
		if (root == null) {
			return list;
		}

		list.add(root.val);
		List<Integer> listLeft = this.preorderTraversalRecursive(root.left);
		list.addAll(listLeft);
		List<Integer> listRight = this.preorderTraversalRecursive(root.right);
		list.addAll(listRight);

		return list;
	}

	private void pushAdd(List<Integer> list, LinkedList<TreeNode> stack,
			TreeNode node) {
		list.add(node.val);
		stack.push(node);
	}

	public List<Integer> preorderTraversalIter(TreeNode root) {
		List<Integer> list = new ArrayList<>();
		if (root == null) {
			return list;
		}

		LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
		pushAdd(list, stack, root);

		while (stack.isEmpty() == false) {
			TreeNode top = stack.peek();
			if (top.left != null) {
				pushAdd(list, stack, top.left);
			} else if (top.right != null) {
				pushAdd(list, stack, top.right);
			} else {
				TreeNode preTop = stack.pop();
				while (stack.isEmpty() == false) {
					top = stack.peek();
					if (preTop == top.left && top.right != null) {
						pushAdd(list, stack, top.right);
						break;
					} else {
						preTop = stack.pop();
					}
				}
			}
		}
		return list;
	}
}
