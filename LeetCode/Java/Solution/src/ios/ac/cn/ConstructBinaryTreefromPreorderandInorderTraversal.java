package ios.ac.cn;

public class ConstructBinaryTreefromPreorderandInorderTraversal {
	public TreeNode buildTree(int[] preorder, int[] inorder) {
		return buildTree(preorder, 0, preorder.length - 1, inorder, 0,
				inorder.length - 1);
	}
	
	private TreeNode buildTree(int[] preorder, int preLow, int preHi, int[] inorder,
			int inLow, int inHi) {
		if (preLow > preHi) {
			return null;
		} else {
			TreeNode root = new TreeNode(preorder[preLow]);
			if (preLow < preHi) {
				int rootIndex = inLow;
				for (int i = inLow; i<= inHi; i++) {
					if (inorder[i] == preorder[preLow]) {
						rootIndex = i;
						break;
					}
				}
				
				TreeNode left = buildTree(preorder, preLow + 1, preLow + (rootIndex - inLow ),
						inorder, inLow, rootIndex - 1);
				TreeNode right = buildTree(preorder, preLow + rootIndex - inLow + 1, preHi,
						inorder, rootIndex + 1, inHi);
				root.left = left;
				root.right = right;
			}
			return root;
		}
	}
}
