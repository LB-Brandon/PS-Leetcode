# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sol1():
            back = None
            cur = head
            while cur:
                front = cur.next
                cur.next = back
                back = cur
                cur = front
            return back
        
        def sol2():
            def reverse(node, prev = None):
                if not node:
                    return prev
                next, node.next = node.next, prev
                return reverse(next, node)
            return reverse(head)



        return sol1()
        


        
