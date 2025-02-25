'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
https://leetcode.com/problems/intersection-of-two-linked-lists/description/

Method 1 - Using hashmap
Method 2 - Pointers, no extra memory 

Using two pointers, we can equalize the effective traversal length of both lists by 
redirecting them to start from the beginning of the other list once they hit the end of their respective lists. 
This means that if there is an intersection, the pointers will meet at the intersection node after at most two passes over each list.
'''

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        current = headA
        Adict = dict()
        while current:
            Adict[current] = True
            current = current.next
        current = headB
        while current:
            if current in Adict:
                return current
            current = current.next
        return None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
                return None
            
            # Initialize two pointers at the start of each list
        pointerA, pointerB = headA, headB
        
        # Traverse both lists
        while pointerA != pointerB:
            # Move to the next node in list A, or switch to head of list B
            pointerA = pointerA.next if pointerA else headB
            # Move to the next node in list B, or switch to head of list A
            pointerB = pointerB.next if pointerB else headA
        
        # When they meet, it's the intersection node or None if no intersection
        return pointerA
