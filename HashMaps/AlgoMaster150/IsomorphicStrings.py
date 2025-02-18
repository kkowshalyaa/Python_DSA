'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

https://leetcode.com/problems/isomorphic-strings/description/
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ans = dict()
        s_list, t_list = list(s), list(t)
        for index in range(0, len(s_list)):
            if s_list[index] not in ans:
                ans[s_list[index]] = t_list[index]
            elif s_list[index] in ans:
                if ans[s_list[index]] == t_list[index]:
                    continue
                else:
                    return False
        return True
'''
Didnt's work, because we have to check both ways - https://youtu.be/7yF-U1hLEqQ?si=6OVKAu83ojHeTJL8
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ans = dict()
        s_list, t_list = list(s), list(t)
        for index in range(0, len(s_list)):
            if s_list[index] not in ans:
                ans[s_list[index]] = t_list[index]
            elif s_list[index] in ans:
                if ans[s_list[index]] == t_list[index]:
                    continue
                else:
                    return False
        ans = dict()
        s_list, t_list = list(t), list(s)
        for index in range(0, len(s_list)):
            if s_list[index] not in ans:
                ans[s_list[index]] = t_list[index]
            elif s_list[index] in ans:
                if ans[s_list[index]] == t_list[index]:
                    continue
                else:
                    return False
        return True
