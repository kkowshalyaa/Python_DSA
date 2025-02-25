'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
''''
This was using iterative method.
'''
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Base cases: when either list is empty, return the other list
    if not l1:
        return l2
    elif not l2:
        return l1
    
    # Compare the values at the head of l1 and l2
    if l1.val < l2.val:
        # If l1's node is smaller, it should be part of the merged list
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        # If l2's node is smaller or equal, it should be part of the merged list
        l2.next = mergeTwoLists(l1, l2.next)
        return l2
''''
This was using recursive method.
'''
