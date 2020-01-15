# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bi = ''

        while head:
            bi += str(head.val)
            head = head.next

        return int(bi, 2)
