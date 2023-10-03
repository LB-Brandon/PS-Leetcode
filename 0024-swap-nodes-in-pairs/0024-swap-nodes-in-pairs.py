# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sol1():
            root = prev = ListNode(None)
            prev.next = head

            while head and head.next:
                b = head.next
                head.next = b.next
                b.next = head

                prev.next = b

                head = head.next
                prev = prev.next.next
            return root.next

        def sol2():
            while head and head.next:
                tmp = head.next
                head.next = self.swapPairs(tmp.next)
                tmp.next = head
                return tmp
            return head

        return sol2()
