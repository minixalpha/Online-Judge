package ios.ac.cn;

public class ReorderList {
	public void reorderList(ListNode head) {
		ListNode mid = findMiddle(head);
		if (mid != null) {
			reverseList(mid);
			ListNode head2 = mid.next;
			mid.next = null;
			combine(head, head2);
		}
	}

	private ListNode findMiddle(ListNode head) {
		int listN = 0;
		ListNode cur = head;
		while (cur != null) {
			cur = cur.next;
			listN++;
		}

		int midN = (listN + 1) / 2;
		ListNode mid = head;
		for (int i = 1; i < midN; i++) {
			mid = mid.next;
		}
		return mid;
	}

	private void reverseList(ListNode head) {
		if (head == null) {
			return;
		}

		ListNode cur = head.next;
		head.next = null;
		while (cur != null) {
			ListNode next = cur.next;
			cur.next = head.next;
			head.next = cur;
			cur = next;

		}
	}

	private void combine(ListNode list1, ListNode list2) {
		ListNode c1 = list1, c2 = list2;
		while (c1 != null && c2 != null) {
			ListNode nc1 = c1.next;
			ListNode nc2 = c2.next;
			c2.next = c1.next;
			c1.next = c2;
			c1 = nc1;
			c2 = nc2;
		}
	}

	public static void main(String[] args) {
		ListNode head = new ListNode(1);
		head.next = new ListNode(2);
		head.next.next = new ListNode(3);
		head.next.next.next = new ListNode(4);

		new ReorderList().reorderList(head);
		ListNode cur = head;
		while (cur != null) {
			System.out.print(cur.val + " ");
			cur = cur.next;
		}
	}
}
