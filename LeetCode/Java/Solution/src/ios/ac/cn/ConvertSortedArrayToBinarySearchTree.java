package ios.ac.cn;

public class ConvertSortedArrayToBinarySearchTree {
	private TreeNode consBST(int[] num, int start, int end) {
		if (start > end) {
			return null;
		}

		int mid = start + ((end - start) >> 1);	
		TreeNode root = new TreeNode(num[mid]);
		root.left = consBST(num, start, mid - 1);
		root.right = consBST(num, mid + 1, end);
		return root;
	}

	public TreeNode sortedArrayToBST(int[] num) {
		if (num == null || num.length == 0) {
			return null;
		}
		return consBST(num, 0, num.length - 1);
	}
	
	public static void main(String[] args) {
		ConvertSortedArrayToBinarySearchTree cbst = new ConvertSortedArrayToBinarySearchTree();
		int[] num = {1, 3, 5};
		System.out.println(cbst.sortedArrayToBST(num).val);
	}
}
