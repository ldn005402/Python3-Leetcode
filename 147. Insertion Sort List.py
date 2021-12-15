class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float('-inf'))
        if not head:
            return head
        dummy.next = head   
        head = head.next 
        dummy.next.next = None
        cur = dummy.next  
        while head:
            if cur.val<=head.val:
                cur.next = head 
                head = head.next 
                # maintain a sorted list 
                cur.next.next = None
                cur = cur.next                 
            else:
                # insert a sort list and scan from begining of the sorted list 
                start = dummy
                while(start and start.next.val<head.val):
                    start = start.next
                next_ = start.next
                tmp = head.next
                start.next = head 
                head.next = next_
                head = tmp
                
        return dummy.next
