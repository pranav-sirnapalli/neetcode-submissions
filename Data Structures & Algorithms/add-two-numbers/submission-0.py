# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        p, q = l1, l2
        while p or q or carry:
            x = p.val if p else 0
            y = q.val if q else 0
            res = x + y + carry
            carry = res // 10
            cur.next = ListNode(res%10)

            cur = cur.next
            p = p.next if p else 0
            q = q.next if q else 0
        return dummy.next
