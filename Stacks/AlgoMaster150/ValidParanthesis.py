'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

https://leetcode.com/problems/valid-parentheses/description/

Implementation:
1. Initialise a stack
2. If open brack, throw it in the stck.
3. If closing brack, get top of stack(if stack is not empty), if stack top element complements closing brack, remove top element from list.
4. If it doesnt complement, return False
5. At the end, if stack is empty - return True
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack_dict = { '}':'{', ')':'(', ']':'['}
        for char in s:
            if char in stack_dict:
                if stack and stack[-1] == stack_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True
        
