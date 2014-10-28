package ios.ac.cn;

class TreeLinkNode {
	int val;
	TreeLinkNode left, right, next;

	TreeLinkNode(int x) {
		val = x;
	}
}

/**
 * 
 * 1. 注意要求用常量空间，这意味着不能用递归，如果用迭代，也不能用栈， 否则，不能算是用了常量空间
 * 
 * 2. 基本思想：每次迭代开始时，本层的 next 构成一个链表， 在此链表上遍历，为下一层建立 next 链表，这样，就使用常量空间 完成对树的遍历。
 * 
 */
public class PopulatingNextRightPointersInEachNode {
	public void connect(TreeLinkNode root) {
		TreeLinkNode start = root;

		while (start != null) {
			TreeLinkNode cur = start;
			while (cur != null) {
				if (cur.left != null) {
					cur.left.next = cur.right;
				}
				if (cur.right != null && cur.next != null) {
					cur.right.next = cur.next.left;
				}
				cur = cur.next;
			}
			start = start.left;
		}
	}
}
