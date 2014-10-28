package ios.ac.cn;

public class PartitionList {
	public ListNode partition(ListNode head, int x) {
		ListNode start = new ListNode(0);
		ListNode end = new ListNode(0);

		ListNode startCur = start;
		ListNode endCur = end;

		ListNode cur = head;
		while (cur != null) {
			ListNode next = cur.next;
			if (cur.val < x) {
				startCur = insertAfter(startCur, cur);
			} else {
				endCur = insertAfter(endCur, cur);
			}
			cur = next;
		}
		startCur.next = end.next;
		return start.next;
	}

	private ListNode insertAfter(ListNode startCur, ListNode cur) {
		cur.next = startCur.next;
		startCur.next = cur;
		startCur = cur;
		return startCur;
	}
}
