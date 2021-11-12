class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        head_holder = ListNode(-1) #it can be any value you like, it ain't matter
        head_holder.next = head
        
        cur = head_holder
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head_holder.next
