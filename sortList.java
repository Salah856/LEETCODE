class Solution {
public ListNode sortList(ListNode head) {
        PriorityQueue<ListNode> q = new PriorityQueue<>((a, b) -> a.val - b.val);
        ListNode current = head;
        while (current != null) {
            q.add(current);
            current = current.next;
        }
        
        ListNode newHead = q.poll();
        current = newHead;
        while (!q.isEmpty() || current != null) {
            current.next = q.poll();
            current = current.next;
        }
        return newHead;
    }
    
}
