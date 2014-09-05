package ios.ac.cn;

import java.util.LinkedList;
import java.util.List;

public class BinaryTreeInOrderTraversal {
	public List<Integer> inorderTraversalRecursive(TreeNode root) {
		List<Integer> list = new LinkedList<Integer>();
		if (root == null) {
			return list;
		}

		List<Integer> listLeft = this.inorderTraversalRecursive(root.left);
		list.addAll(listLeft);
		list.add(root.val);
		List<Integer> listRight = this.inorderTraversalRecursive(root.right);
		list.addAll(listRight);

		return list;
	}
	
	public List<Integer> inorderTraversalIter(TreeNode root) {
		List<Integer> list = new LinkedList<Integer>();
		if (root == null) {
			return list;
		}
		
		LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
		stack.push(root);
		
		while (stack.isEmpty() == false) {
			TreeNode top = stack.peek();
			if (top.left != null) {
				stack.push(top.left);
			} else if (top.right != null) {
				stack.push(top.right);
				list.add(top.val);
			} else {
				TreeNode preTop = stack.pop();
				list.add(preTop.val);
				while (stack.isEmpty() == false) {
					top = stack.peek();
					if (preTop == top.left) {
						list.add(top.val);
						if (top.right != null) {
							stack.push(top.right);
							break;
						}
					}
					preTop = stack.pop();
				}
			}
		}
		return list;
	}
}
