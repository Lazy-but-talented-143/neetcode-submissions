# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_1=[]
        l_2=[]
        while l1:
            l_1.append(str(l1.val))
            l1=l1.next 
        while l2:
            l_2.append(str(l2.val))
            l2=l2.next
        num1 = int("".join(l_1[::-1]))  
        num2 = int("".join(l_2[::-1]))
        total=num1+num2
        total_str = str(total)[::-1]
        
        dummy = ListNode(0)
        current = dummy
        
        for char in total_str:
            current.next = ListNode(int(char))
            current = current.next
            
        return dummy.next
        


        