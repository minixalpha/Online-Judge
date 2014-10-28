package ios.ac.cn;

public class ConstructBinaryTreefromInorderandPostorderTraversal {
	public TreeNode buildTree(int[] inorder, int[] postorder) {
		return buildTree(inorder, 0, inorder.length - 1, postorder, 0,
				postorder.length - 1);
	}

	private TreeNode buildTree(int[] inorder, int inLow, int inHi,
			int[] postorder, int postLow, int postHi) {
		TreeNode root = null;
		if (postLow <= postHi) {
			root = new TreeNode(postorder[postHi]);

			if (postLow < postHi) {
				int rootIndex = inLow;
				for (int i = inLow; i <= inHi; i++) {
					if (inorder[i] == postorder[postHi]) {
						rootIndex = i;
						break;
					}
				}
				TreeNode left = buildTree(inorder, inLow, rootIndex - 1,
						postorder, postLow, postLow + (rootIndex - 1 - inLow));
				TreeNode right = buildTree(inorder, rootIndex + 1, inHi,
						postorder, postLow + (rootIndex - inLow), postHi - 1);
				root.left = left;
				root.right = right;
			}
		}
		return root;
	}
}
