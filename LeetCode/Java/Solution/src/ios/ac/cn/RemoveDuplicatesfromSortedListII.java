package ios.ac.cn;

public class RemoveDuplicatesfromSortedListII {
	public ListNode deleteDuplicates(ListNode head) {
		ListNode result = new ListNode(0);
		ListNode tail = result;
		ListNode pre = null, cur = head;
		while (cur != null) {
			ListNode next = cur.next;

			if (notequal(cur, pre) && notequal(cur, next)) {
				tail = insertAfter(tail, cur);
			}

			pre = cur;
			cur = next;
		}
		return result.next;
	}

	private ListNode insertAfter(ListNode tail, ListNode cur) {
		cur.next = tail.next;
		tail.next = cur;
		return cur;
	}

	private boolean notequal(ListNode cur, ListNode neighbor) {
		if (cur == null && neighbor != null || cur != null && neighbor == null) {
			return true;
		}

		if (cur == neighbor || cur.val == neighbor.val) {
			return false;
		}

		return true;
	}
}
