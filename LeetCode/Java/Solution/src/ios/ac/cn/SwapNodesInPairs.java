package ios.ac.cn;

public class SwapNodesInPairs {
	private ListNode modify(ListNode start) {
		if (start == null || start.next == null) {
			return start;
		}

		ListNode startNext = start.next;
		start.next = startNext.next;
		startNext.next = start;
		return startNext;
	}

	public ListNode swapPairs(ListNode head) {
		head = modify(head);

		ListNode cur = head;
		while (cur != null && cur.next != null && cur.next.next != null) {
			ListNode next = modify(cur.next.next);
			cur.next.next = next;
			cur = next;
		}

		return head;
	}
}
