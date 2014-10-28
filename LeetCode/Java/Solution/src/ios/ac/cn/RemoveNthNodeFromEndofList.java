package ios.ac.cn;

public class RemoveNthNodeFromEndofList {
	/*
	 * 凡是删除链表中的结点，都需要考虑是否能应对删除头结点
	 */
	public ListNode removeNthFromEnd(ListNode head, int n) {
		ListNode senti = new ListNode(0);
		senti.next = head;

		ListNode first = senti;
		int i;
		for (i = 0; i < n && first.next != null; i++) {
			first = first.next;
		}

		if (i == n) {
			ListNode second = senti;
			while (first.next != null) {
				first = first.next;
				second = second.next;
			}
			second.next = second.next.next;
		}
		return senti.next;
	}
}
