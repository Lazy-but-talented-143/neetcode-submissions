# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s1=[]
        curr=head
        while curr:
            s1.insert(0,curr.val)
            curr=curr.next
        dummy=ListNode(0)
        curr=dummy
        for num in s1:
            curr.next=ListNode(num)
            curr=curr.next
        return dummy.next

        