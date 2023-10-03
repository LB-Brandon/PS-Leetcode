# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def sol1(l1, l2):
            current = dummy = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            if l1: current.next = l1
            elif l2: current.next = l2
        
            return dummy.next
        
        def sol2(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            
            if l1.val < l2.val:
                l1.next = sol2(l1.next, l2)
                return l1
            else:
                l2.next = sol2(l1, l2.next)
                return l2

        return sol2(l1, l2)