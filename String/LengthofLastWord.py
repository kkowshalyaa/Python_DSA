'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

https://leetcode.com/problems/length-of-last-word/description/
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(' ')
        return len(words[-1])


'''
1. strip():- This method is used to delete all the leading and trailing characters mentioned in its argument. Ex. str.lstrip('-')
2. lstrip():- This method is used to delete all the leading characters mentioned in its argument.
3. rstrip():- This method is used to delete all the trailing characters mentioned in its argument.
'''
