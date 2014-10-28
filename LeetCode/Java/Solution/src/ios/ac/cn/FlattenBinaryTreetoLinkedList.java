package ios.ac.cn;

public class FlattenBinaryTreetoLinkedList {
	// 唯一需要注意的是，要把左子树置空
	public void flatten(TreeNode root) {
		while (root != null) {
			if (root.left != null) {
				TreeNode cur = root.left;
				while (cur.right != null) {
					cur = cur.right;
				}
				cur.right = root.right;
				root.right = root.left;
				root.left = null;
			}
			root = root.right;
		}
	}

	private TreeNode pre = new TreeNode(0);
	public void flattenRecursive(TreeNode root) {
		pre.right = root;
		pre.left = null;
		if (root == null) {
			return;
		}
		pre = root;
		TreeNode right = root.right;
		flatten(root.left);
		flatten(right);
	}

	public static void main(String[] args) {
		TreeNode root = new TreeNode(1);
		root.left = new TreeNode(2);
		root.right = new TreeNode(3);
		root.left.left = new TreeNode(4);
		new FlattenBinaryTreetoLinkedList().flatten(root);

		TreeNode cur = root;
		while (cur != null) {
			System.out.println(cur.val);
			cur = cur.right;
		}
	}
}
