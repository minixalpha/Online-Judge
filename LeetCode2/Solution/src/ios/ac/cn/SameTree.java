package ios.ac.cn;
public class SameTree {
	public boolean isSameTree(TreeNode p, TreeNode q) {
		if (p == null || q == null) {
			if (p == null && q == null) {
				return true;
			} else {
				return false;
			}
		}

		if (p.val != q.val) {
			return false;
		}

		if (this.isSameTree(p.left, q.left) == false) {
			return false;
		}

		if (this.isSameTree(p.right, q.right) == false) {
			return false;
		}

		return true;
	}
}
