package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class ConvertSortedListtoBinarySearchTree {
	public TreeNode sortedListToBST2(ListNode head) {
		if (head == null) {
			return null;
		}
		TreeNode root = new TreeNode(head.val);
		ListNode cur = head.next;
		while (cur != null) {

			TreeNode insertPos = root;
			while (true) {
				if (cur.val < insertPos.val) {
					if (insertPos.left == null) {
						insertPos.left = new TreeNode(cur.val);
						break;
					} else {
						insertPos = insertPos.left;
					}
				} else {
					if (insertPos.right == null) {
						insertPos.right = new TreeNode(cur.val);
						break;
					} else {
						insertPos = insertPos.right;
					}
				}
			}

			cur = cur.next;
		}
		return root;
	}

	public TreeNode sortedListToBST(ListNode head) {
		List<ListNode> nodes = new ArrayList<>();
		ListNode cur = head;
		while (cur != null) {
			nodes.add(cur);
			cur = cur.next;
		}

		return sortedListToBST(nodes, 0, nodes.size() - 1);
	}

	private TreeNode sortedListToBST(List<ListNode> nodes, int lo, int hi) {
		if (lo > hi) {
			return null;
		} else if (lo == hi) {
			return new TreeNode(nodes.get(lo).val);
		} else {
			int mid = lo + (hi - lo) / 2;
			TreeNode root = new TreeNode(nodes.get(mid).val);
			TreeNode leftRoot = sortedListToBST(nodes, lo, mid - 1);
			TreeNode rightRoot = sortedListToBST(nodes, mid + 1, hi);
			root.left = leftRoot;
			root.right = rightRoot;
			return root;
		}
	}

}
