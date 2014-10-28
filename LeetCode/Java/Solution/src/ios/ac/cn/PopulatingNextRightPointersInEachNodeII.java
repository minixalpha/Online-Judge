package ios.ac.cn;

public class PopulatingNextRightPointersInEachNodeII {
	public void connect(TreeLinkNode root) {
		TreeLinkNode start = root;
		boolean hasRemain = true;
		while (hasRemain) {
			TreeLinkNode cur = start;

			hasRemain = false;
			while (cur != null) {
				TreeLinkNode next = findNext(cur.next);
				TreeLinkNode nextChild = getNonNullChild(next);
				if (cur.left != null || cur.right != null) {
					hasRemain = true;
					if (cur.left != null && cur.right != null) {
						cur.left.next = cur.right;
						cur.right.next = nextChild;
					} else if (cur.left != null) {
						cur.left.next = nextChild;
					} else if (cur.right != null) {
						cur.right.next = nextChild;
					}
				}

				cur = next;
			}

			start = getNonNullChild(findNext(start));
		}
	}

	private TreeLinkNode getNonNullChild(TreeLinkNode cur) {
		if (cur == null) {
			return null;
		}
		if (cur.left != null) {
			return cur.left;
		} else {
			return cur.right;
		}
	}

	private TreeLinkNode findNext(TreeLinkNode cur) {
		while (cur != null) {
			if (cur.left != null || cur.right != null) {
				return cur;
			}
			cur = cur.next;
		}
		return null;
	}
}
