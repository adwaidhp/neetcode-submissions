# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow1,fast=head,head
        if head==None:
            return False
        while True:
            slow1=slow1.next
            if fast.next==None:
                return False
            if fast.next.next==None:
                return False

            fast=fast.next.next

            if slow1.next==fast.next:
                return True
        