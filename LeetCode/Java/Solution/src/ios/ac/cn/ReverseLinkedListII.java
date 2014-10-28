package ios.ac.cn;

public class ReverseLinkedListII {
	public ListNode reverseBetween(ListNode head, int m, int n) {
		ListNode first = new ListNode(0);
		first.next = head;

		ListNode pre = first;
		for (int i = 1; i < m; i++) {
			pre = pre.next;
		}

		ListNode cur = pre.next;
		ListNode tail = cur;
		for (int i = m; i <= n; i++) {
			ListNode next = cur.next;
			cur.next = pre.next;
			pre.next = cur;
			cur = next;
		}
		tail.next = cur;
		return first.next;
	}
}
