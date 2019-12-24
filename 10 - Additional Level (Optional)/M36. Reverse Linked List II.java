/**
 * Definition for ListNode
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param head: ListNode head is the head of the linked list
     * @param m: An integer
     * @param n: An integer
     * @return: The head of the reversed ListNode
     */
    public ListNode reverseBetween(ListNode head, int m, int n) {
        // write your code here
        if (m >= n || head == null) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        int i = 1;
        while (i < m && head != null) {
            prev = head;
            head = head.next;
            i++;
        }

        if (head == null) return null;

        prev.next = null;
        ListNode curr = head;
        while (i < n && curr != null) {
            curr = curr.next;
            i++;
        }

        if (curr == null) return null;
        ListNode next = curr.next;
        curr.next = null;
        prev.next = reverse(head);
        head.next = next;

        return dummy.next;
    }

    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
}

// Leetcode

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (m >= n || head == null) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        int i = 1;
        while (i < m && head != null) {
            prev = head;
            head = head.next;
            i++;
        }

        if (head == null) return null;
        prev.next = null;
        ListNode tail = head;
        while (i++ < n && head != null) {
            head = head.next;
        }

        if (head == null) return null;
        ListNode next = head.next;
        head.next = null;
        prev.next = reverse(tail);
        tail.next = next;


        return dummy.next;
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
