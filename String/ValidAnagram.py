'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Anagram - Characters and frequency of characters should be same.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false

https://leetcode.com/problems/valid-anagram/description/

Implementation - 
1. Create Dictionary for each string such that Dict Key - character, Value - No. of Times the Character occurs
2. Check if both the Dictonaries are equal.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.stringDict(s) == self.stringDict(t)

    def stringDict(self, str_1):
        op_dict = dict()
        for s in str_1:
            if s not in op_dict.keys():
                op_dict[s] = 1
            elif s in op_dict.keys():
                op_dict[s] += 1
        return op_dict
