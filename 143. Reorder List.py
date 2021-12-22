class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = None
        while head:
            q = head.next
            head.next = p
            p = head
            head = q
        return p

    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = self.reverseList(slow.next)
        slow.next = None
        p = head
        q = head1
        while q:
            p_nxt = p.next
            q_nxt = q.next
            p.next = q
            q.next = p_nxt
            p = p_nxt
            q = q_nxt
