'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

https://leetcode.com/problems/is-subsequence/description/

Solution using hashmap: https://github.com/AlgoMaster-io/leetcode-solutions/blob/main/python/is-subsequence.md
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s, pointer_t = 0, 0
        
        while pointer_s < len(s) and pointer_t < len(t):
            # Check if current character in both strings match
            if s[pointer_s] == t[pointer_t]:
                # Move the pointer for string s
                pointer_s += 1
            # Always move the pointer for string t
            pointer_t += 1
        
        # If we've traversed all of s, it's a subsequence of t
        return pointer_s == len(s)
