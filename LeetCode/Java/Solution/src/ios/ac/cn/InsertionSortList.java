package ios.ac.cn;

public class InsertionSortList {
	public ListNode insertionSortList(ListNode head) {
		if (head == null) {
			return null;
		}

		ListNode senti = new ListNode(0);
		senti.next = head;

		ListNode cur = head;
		while (cur.next != null) {
			if (cur.val > cur.next.val) {
				ListNode next = cur.next;
				cur.next = next.next;
				insertInSortList(senti, next);
			} else {
				cur = cur.next;
			}
		}
		return senti.next;
	}

	private void insertInSortList(ListNode senti, ListNode cur) {
		ListNode p = senti;
		while (cur.val > p.next.val) {
			p = p.next;
		}
		cur.next = p.next;
		p.next = cur;
	}
}
