'''
Given two strings s and p, return an array of all the start indices of p's
anagrams in s. You may return the answer in any order.
Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

https://leetcode.com/problems/find-all-anagrams-in-a-string/

Implementation:
1. Create a frequency dict for p
2. Iterate through s, consider substring of len(p)
3. Create a frequency dict of each substring and compare it to that of p, return index if matches
'''


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_freq = self.createFrequencyDict(p)
        an_index = []
        for index in range(0, (len(s) - len(p)) + 1):
            if p_freq == self.createFrequencyDict(s[index:(index + (len(p)))]):
                an_index.append(index)
            else:
                continue
        return an_index

    def createFrequencyDict(self, temp_str):
        f_dict = dict()
        for char in temp_str:
            if char not in f_dict.keys():
                f_dict[char] = 1
            elif char in f_dict.keys():
                f_dict[char] += 1
        return f_dict

[!! TIME LIMIT EXCEEDS, NEED OPTIMISED SOLUTION !!]
