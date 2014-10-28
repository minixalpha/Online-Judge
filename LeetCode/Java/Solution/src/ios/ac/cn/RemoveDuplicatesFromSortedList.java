package ios.ac.cn;

public class RemoveDuplicatesFromSortedList {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode cur = head;
        while (cur != null) {
        	ListNode next = cur.next;
        	if (next != null && cur.val == next.val) {
        		cur.next = next.next;
        	} else {
        		cur = next;
        	}
        }
        return head;
    }
}
