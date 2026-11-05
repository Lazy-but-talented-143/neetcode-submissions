# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s1=[]
        curr=head
        while curr:
            s1.append(curr.val)
            curr=curr.next
        return s1==s1[::-1]  