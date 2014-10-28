package ios.ac.cn;

public class LinkedListCycleII {
	public ListNode detectCycle(ListNode head) {
		if (head == null || head.next == null) {
			return null;
		}

		ListNode slow = head;
		ListNode fast = head;

		do {
			fast = fast.next;
			if (fast != null) {
				fast = fast.next;
			}
			slow = slow.next;
		} while (fast != null && fast != slow);

		if (fast == null) {
			return null;
		} else {
			slow = head;
			while (slow != fast) {
				slow = slow.next;
				fast = fast.next;
			}
			return slow;
		}
	}

	public static void main(String[] args) {
		ListNode n = new ListNode(1);
		ListNode n1 = new ListNode(0);
		n.next = n1;
		n1.next = n;
		System.out.println(new LinkedListCycleII().detectCycle(n).val);
	}
}
