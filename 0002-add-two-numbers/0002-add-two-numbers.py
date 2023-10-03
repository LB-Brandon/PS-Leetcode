# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1, sum2 = 0, 0
        root = head = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            if carry:
                total += 1
                carry = 0
            print(total)
            if total >= 10:
                carry = 1
                total = total - 10

            head.next = ListNode(total)
            head = head.next

        return root.next
         
            
                



