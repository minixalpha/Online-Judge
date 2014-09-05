package ios.ac.cn;
class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
		next = null;
	}
}

public class LinkedListCycle {
	public boolean hasCycle(ListNode head) {
		if (head == null) {
			return false;
		}

		ListNode fast = head.next;
		ListNode slow = head;

		while (fast != null && fast != slow) {
			fast = fast.next;
			if (fast != null) {
				fast = fast.next;
			}
			slow = slow.next;
		}

		if (fast != null && fast == slow) {
			return true;
		} else {
			return false;
		}
	}
}
