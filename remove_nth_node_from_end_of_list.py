# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        temp = head
        count = 0
        while temp:
            count +=1
            temp = temp.next
        
        if count == n:
            head = head.next
            return head
            
        curr = head
        for i in range(count-n-1):
            curr = curr.next
            
        if curr.next.next == None:
            curr.next = None
            return head
        
        curr.next = curr.next.next
        return head
            