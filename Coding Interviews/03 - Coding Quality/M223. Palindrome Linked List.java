/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;

        ListNode mid = findMid(head);
        ListNode next = mid.next;
        mid.next = null;

        next = reverse(next);

        while (next != null) {
            if (head.val != next.val)  return false;

            head = head.next;
            next = next.next;
        }

        return true;
    }

    private ListNode findMid(ListNode head) {
        if (head == null) return head;

        ListNode slow = head, fast = head.next;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }

    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }

        return prev;
    }
}
