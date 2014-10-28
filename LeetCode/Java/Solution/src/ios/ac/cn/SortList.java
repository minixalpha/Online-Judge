package ios.ac.cn;

public class SortList {
	public ListNode sortList(ListNode head) {
		if (head == null || head.next == null) {
			return head;
		}

		ListNode[] heads = split(head);
		heads[0] = sortList(heads[0]);
		heads[1] = sortList(heads[1]);
		return merge(heads[0], heads[1]);
	}

	private ListNode[] split(ListNode head) {
		ListNode[] heads = new ListNode[2];
		ListNode h1 = head, h2 = head;

		h2 = skipTwo(h2);
		while (h2 != null) {
			h1 = h1.next;
			h2 = skipTwo(h2);
		}

		heads[0] = head;
		if (h1 != null) {
			heads[1] = h1.next;
			h1.next = null;
		} else {
			heads[1] = null;
		}
		return heads;
	}

	private ListNode skipTwo(ListNode head) {
		if (head == null) {
			return null;
		}
		head = head.next;
		if (head != null) {
			head = head.next;
		}
		return head;
	}

	private ListNode merge(ListNode head1, ListNode head2) {
		ListNode head = new ListNode(0);
		ListNode tail = head;

		ListNode h1 = head1, h2 = head2;
		while (h1 != null && h2 != null) {
			if (h1.val < h2.val) {
				tail.next = h1;
				tail = h1;
				h1 = h1.next;
			} else {
				tail.next = h2;
				tail = h2;
				h2 = h2.next;
			}
		}

		if (h1 != null) {
			tail.next = h1;
		} else {
			tail.next = h2;
		}

		return head.next;
	}
}
