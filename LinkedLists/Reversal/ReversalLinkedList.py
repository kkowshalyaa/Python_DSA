'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

https://leetcode.com/problems/reverse-linked-list/description/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node = current.next  # Save the next node
            current.next = previous   # Reverse the link
            previous = current        # Move `previous` pointer one step
            current = next_node       # Move `current` pointer one step

        return previous  # New head of the reversed list
