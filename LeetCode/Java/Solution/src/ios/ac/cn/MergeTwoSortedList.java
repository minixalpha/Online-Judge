package ios.ac.cn;

public class MergeTwoSortedList {
	public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
		ListNode head = new ListNode(0);
		ListNode end = head;
		while (l1 != null && l2 != null) {
			if (l1.val < l2.val) {
				end.next = l1;
				end = l1;
				l1 = l1.next;
			} else {
				end.next = l2;
				end = l2;
				l2 = l2.next;
			}
		}

		if (l1 != null) {
			end.next = l1;
		}
		if (l2 != null) {
			end.next = l2;
		}

		return head.next;
	}

	public static void main(String[] args) {

	}
}
