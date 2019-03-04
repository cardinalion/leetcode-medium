class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        slow = fast = head
        
        for i in range(n):
            fast = fast.next
        
        if fast == None:
            return head.next
        
        while fast.next != None:
            slow, fast = slow.next, fast.next
        
        slow.next = slow.next.next
        
        return head
