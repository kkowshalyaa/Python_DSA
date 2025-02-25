'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

https://leetcode.com/problems/middle-of-the-linked-list/description/

Implementation using -
Floyd’s Cycle-Finding Algorithm commonly used for loop detection in linked lists. We use two pointers at different speeds:

A slow pointer that moves one step at a time.
A fast pointer that moves two steps at a time.
When the fast pointer reaches the end of the list, the slow pointer will have reached the middle.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
    
        # Move slow by 1 step and fast by 2 steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # When loop breaks, slow will be at the middle node
        return slow
