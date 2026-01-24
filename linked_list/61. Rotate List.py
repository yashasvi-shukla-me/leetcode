"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""

# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head

        tail = head
        length = 1

        # traverse to know length
        while tail.next:
            tail = tail.next
            length = length + 1

        k = k % length

        if k == 0:
            return head

        # make the list circular
        tail.next = head

        new_tail_index = length - k - 1
        new_tail = head

        for i in range(new_tail_index):
            new_tail = new_tail.next

        # assign new head and break the cycle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
